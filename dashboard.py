import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
@st.cache_data
def load_data():
    day_df = pd.read_csv("day.csv")
    hour_df = pd.read_csv("hour.csv")
    
    # Convert date column
    day_df["date"] = pd.to_datetime(day_df["dteday"])
    hour_df["date"] = pd.to_datetime(hour_df["dteday"])

    return day_df, hour_df

day_df, hour_df = load_data()

# Sidebar (Filter Rentang Waktu)
min_date = day_df["date"].min()
max_date = day_df["date"].max()

with st.sidebar:
    st.image("https://raw.githubusercontent.com/farrelaryansyah/dashboard_streamlit/refs/heads/main/foto.jpeg")

    # Input rentang tanggal
    start_date, end_date = st.date_input(
        label="📅 Rentang Waktu",
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Filter data berdasarkan rentang tanggal yang dipilih
filtered_day_df = day_df[(day_df["date"] >= pd.Timestamp(start_date)) & (day_df["date"] <= pd.Timestamp(end_date))]
filtered_hour_df = hour_df[(hour_df["date"] >= pd.Timestamp(start_date)) & (hour_df["date"] <= pd.Timestamp(end_date))]

# Header
st.title("🚲 Bike Sharing Dashboard")
st.write("""
         Analisis pola penyewaan sepeda berdasarkan Waktu, Pengaruh Cuaca, dan Analisis Clustering.
         - Bagaimana pola penyewaan sepeda berdasarkan waktu dalam sehari?
         - Seberapa besar pengaruh cuaca terhadap pola penyewaan sepeda?
         """)
st.markdown("---")


# 1. Pola Penyewaan Sepeda Berdasarkan Waktu dalam Sehari
st.header("📊 Pola Penyewaan Sepeda Berdasarkan Waktu dalam Sehari")

# Agregasi data per jam setelah filter
hourly_rentals = filtered_hour_df.groupby("hr")["cnt"].mean()

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_rentals.index, y=hourly_rentals.values, marker="o", linewidth=2, color="b")

ax.set_xlabel("Jam dalam Sehari", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan Sepeda", fontsize=12)
ax.set_title("Pola Penyewaan Sepeda Berdasarkan Waktu dalam Sehari", fontsize=14)
ax.set_xticks(range(0, 24))
ax.grid(True, linestyle='--', alpha=0.8)

st.pyplot(fig)

st.write("""
📌 **Insight:**  
- **Puncak Penyewaan pada Pagi & Sore Hari**  
  Terdapat dua puncak utama sekitar pukul 7-9 pagi dan 17-19 sore.
- **Penyewaan Rendah di Tengah Malam & Dini Hari**  
  Jam 0-5 pagi memiliki penyewaan sangat rendah.  
- **Penyewaan Stabil di Siang Hari**  
  Setelah puncak pagi, penyewaan menurun tetapi tetap cukup stabil dari pukul 10 pagi hingga 15 sore.  
""")
st.markdown("---")


# 2. Pengaruh Cuaca terhadap Penyewaan Sepeda
st.header("🌤️ Pengaruh Cuaca terhadap Penyewaan Sepeda")

# Agregasi data per kondisi cuaca setelah filter
weather_rentals = filtered_hour_df.groupby("weathersit")["cnt"].mean()

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
sns.lineplot(
    x=["Cerah", "Mendung", "Hujan Ringan", "Hujan Deras"],  # Label kategori
    y=weather_rentals.values,
    marker="o",
    linestyle="-",
    color="b"
)

ax.set_xlabel("Kategori Cuaca", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan Sepeda", fontsize=12)
ax.set_title("Pengaruh Cuaca terhadap Penyewaan Sepeda", fontsize=14)
ax.grid(True, linestyle='--', alpha=0.8)

st.pyplot(fig)

st.write("""
📌 **Insight:**  
- **Cuaca Cerah Meningkatkan Penyewaan**  
  Penyewaan sepeda tertinggi saat cuaca cerah. Ini menunjukkan bahwa orang lebih suka bersepeda saat kondisi cuaca mendukung.  
- **Penurunan Saat Mendung dan Hujan Ringan**  
  Saat mendung, jumlah penyewaan sepeda mulai menurun, meskipun tidak drastis. Pengguna mungkin lebih berhati-hati atau memilih moda transportasi lain.
- **Penyewaan Drastis Turun saat Hujan Ringan & Hujan Deras**  
  Hujan ringan menyebabkan penurunan signifikan dalam jumlah penyewaan sepeda. Hujan deras memiliki penyewaan sepeda terendah, menunjukkan bahwa pengguna menghindari bersepeda saat kondisi basah dan licin.   
""")
st.markdown("---")


# 3. Clustering Waktu Perhari
st.header("🕒 Analisis Lanjutan Pola Penyewaan Sepeda Harian dengan Clustering Manual")

# Kategorisasi waktu dalam sehari secara langsung tanpa menambah kolom baru
time_labels = ['Dini Hari', 'Pagi Hari', 'Siang Hari', 'Sore Hari', 'Malam Hari']
hour_bins = [0, 6, 12, 16, 19, 24]

# Buat kategori langsung saat agregasi
hour_df["time_category"] = pd.cut(hour_df["hr"], bins=hour_bins, labels=time_labels, right=False)

# Agregasi data berdasarkan kategori waktu
time_trend = hour_df.groupby("time_category")["cnt"].mean().reindex(time_labels)

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
time_trend.plot(kind='bar', color=['blue', 'orange', 'green', 'red', 'purple'], ax=ax)

ax.set_title("Pola Penyewaan Sepeda Berdasarkan Waktu dalam Sehari", fontsize=14)
ax.set_xlabel("Waktu dalam Sehari", fontsize=12)
ax.set_ylabel("Total Penyewaan Sepeda", fontsize=12)
ax.set_xticklabels(time_trend.index, rotation=0)
ax.grid(linestyle="--", alpha=0.8)

st.pyplot(fig)

st.write("""
📌 **Insight:**  
- **Puncak Penyewaan pada Pagi & Sore Hari**  
  Penyewaan meningkat tajam saat pagi (07:00 - 09:00) dan sore (17:00 - 19:00), kemungkinan besar karena jam kerja dan sekolah.
- **Penyewaan Stabil di Siang Hari**  
  Siang hari memiliki jumlah penyewaan yang relatif stabil, pengguna mungkin menggunakan sepeda untuk rekreasi atau aktivitas santai.  
- **Penyewaan Terendah di Dini Hari & Malam Hari**  
  Jumlah penyewaan paling rendah terjadi pada dini hari (00:00 - 04:00) dan mulai menurun kembali setelah malam (20:00 - 23:00), mencerminkan aktivitas yang lebih sedikit pada jam-jam tersebut. 
""")
st.markdown("---")


# 4. Clustering Cuaca
st.header("🌦️ Analisis Lanjutan Pola Penyewaan Sepeda Berdasarkan Kategori Cuaca dengan Clustering Manual")

# Mapping kondisi cuaca ke kategori yang lebih mudah dipahami
weather_mapping = {1: "Cerah", 2: "Mendung", 3: "Hujan Ringan", 4: "Hujan Deras"}
hour_df["weather_category"] = hour_df["weathersit"].map(weather_mapping)

# Agregasi data berdasarkan kategori cuaca
weather_trend = hour_df.groupby("weather_category")["cnt"].mean().reindex(['Cerah', 'Mendung', 'Hujan Ringan', 'Hujan Deras'])

# Plot
fig, ax = plt.subplots(figsize=(10, 5))
colors = ['skyblue', 'lightgray', 'steelblue', 'coral']  
weather_trend.plot(kind='bar', color=colors, ax=ax)

ax.set_title("Pola Penyewaan Sepeda Berdasarkan Kategori Cuaca", fontsize=14)
ax.set_xlabel("Kategori Cuaca", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan Sepeda", fontsize=12)
ax.set_xticklabels(weather_trend.index, rotation=0)
ax.grid(linestyle="--", alpha=0.8)

st.pyplot(fig)

st.write("""
📌 **Insight:**  
- **Cuaca Cerah Mendorong Penyewaan Tertinggi**  
  Jumlah penyewaan sepeda paling tinggi saat cuaca cerah, menunjukkan bahwa pengguna lebih nyaman bersepeda saat kondisi cuaca mendukung. Ini terutama berlaku bagi pengguna yang menggunakan sepeda untuk rekreasi atau perjalanan santai.
- **Penyewaan Menurun Saat Cuaca Mendung**  
  Saat mendung, penyewaan sepeda mulai berkurang, kemungkinan karena ketidakpastian kondisi cuaca (potensi hujan). Meskipun demikian, jumlah penyewaan tidak turun drastis, yang berarti masih ada pengguna yang tetap menggunakan sepeda.
- **Hujan Ringan & Hujan Deras Menghambat Penyewaan**  
  Hujan ringan menyebabkan penurunan penyewaan yang cukup signifikan. Hujan deras memiliki jumlah penyewaan paling rendah, menunjukkan bahwa kondisi basah dan licin sangat mengurangi minat pengguna.  
""")

# Footer
st.markdown("---")