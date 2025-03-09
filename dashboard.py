import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===================== #
# Load Data
# ===================== #
@st.cache_data
def load_data():
    day_df = pd.read_csv("day.csv")
    hour_df = pd.read_csv("hour.csv")
    
    # Convert date column
    day_df["date"] = pd.to_datetime(day_df["dteday"])
    hour_df["date"] = pd.to_datetime(hour_df["dteday"])

    return day_df, hour_df

day_df, hour_df = load_data()

# ===================== #
# Sidebar (Filter Rentang Waktu)
# ===================== #
min_date = day_df["date"].min()
max_date = day_df["date"].max()

with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("/Users/user/Documents/Dashboard/foto.jpeg")

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

# ===================== #
# Header
# ===================== #
st.title("🚲 Bike Sharing Dashboard")
st.write("Analisis pola penyewaan sepeda berdasarkan waktu, pengaruh cuaca, dan RFM Analysis.")
st.markdown("---")

# ===================== #
# 1️⃣ Pola Penyewaan Sepeda Berdasarkan Waktu dalam Sehari
# ===================== #
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
ax.grid(True)

st.pyplot(fig)

st.write("""
📌 **Insight:**  
- **Puncak Penyewaan pada Pagi & Sore Hari**  
  Terdapat dua puncak utama sekitar pukul **7-9 pagi** dan **17-19 sore**.
- **Penyewaan Rendah di Tengah Malam & Dini Hari**  
  Jam **0-5 pagi** memiliki penyewaan sangat rendah.  
- **Penyewaan Stabil di Siang Hari**  
  Setelah puncak pagi, penyewaan menurun tetapi tetap cukup stabil dari pukul **10 pagi hingga 15 sore**.  
""")

# ===================== #
# 2️⃣ Pengaruh Cuaca terhadap Penyewaan Sepeda (Diperbaiki)
# ===================== #
st.header("🌤️ Pengaruh Cuaca terhadap Penyewaan Sepeda")

# Agregasi data per kondisi cuaca setelah filter (menggunakan hour_df)
weather_rentals = filtered_hour_df.groupby("weathersit")["cnt"].mean()

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=weather_rentals.index, y=weather_rentals.values, palette=["#92BCEA", "#D3D3D3", "#E6A189", "#8B0000"])

ax.set_xlabel("Kategori Cuaca", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan Sepeda", fontsize=12)
ax.set_title("Pengaruh Cuaca terhadap Penyewaan Sepeda", fontsize=14)
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(["Cerah", "Mendung", "Hujan Ringan", "Hujan Deras"])
ax.grid(axis="y")

st.pyplot(fig)

st.write("""
📌 **Insight:**  
- **Cuaca Cerah Meningkatkan Penyewaan**  
  Penyewaan sepeda tertinggi saat cuaca cerah. Ini menunjukkan bahwa orang lebih suka bersepeda saat kondisi cuaca mendukung.  
- **Penurunan Saat Mendung dan Hujan Ringan**  
  Saat cuaca mendung atau hujan ringan, terjadi penurunan penyewaan yang cukup signifikan. Pengguna mungkin lebih berhati-hati atau memilih moda transportasi lain.  
- **Hujan Deras = Penyewaan Sangat Rendah**  
  Saat hujan deras, penyewaan sepeda menjadi paling rendah, menunjukkan bahwa pengguna cenderung menghindari bersepeda dalam kondisi ekstrem.   
""")

# ===================== #
# 3️⃣ RFM Analysis
# ===================== #
st.header("📈 RFM Analysis untuk Penyewaan Sepeda")

# Data RFM (dummy, silakan ganti dengan perhitungan RFM yang sesuai)
rfm_hour = pd.DataFrame({
    "hr": range(24),
    "RFM_Score": ["121", "111", "111", "111", "111", "111", "212", "223", "224", "223", "222",
                  "222", "333", "344", "343", "343", "344", "344", "434", "434", "433", "432", "432", "432"],
    "Monetary": [39130, 24164, 16352, 8174, 4428, 14261, 55132, 154171, 261001, 159438, 126257, 151320, 184414,
                 184919, 175652, 183149, 227748, 336860, 309772, 226789, 164550, 125445, 95612, 63941]
})

# Heatmap RFM Analysis berdasarkan waktu dalam sehari
fig, ax = plt.subplots(figsize=(12, 6))
sns.heatmap(rfm_hour.pivot(index="hr", columns="RFM_Score", values="Monetary"),
            cmap="coolwarm", annot=True, fmt=".0f", linewidths=0.5)

ax.set_title("RFM Analysis: Pola Penyewaan Sepeda Berdasarkan Waktu dalam Sehari", fontsize=14)
ax.set_xlabel("RFM Score")
ax.set_ylabel("Jam dalam Sehari")
ax.grid(True, linestyle='--', alpha=0.7)

st.pyplot(fig)

st.write("""
📌 **Insight:**  
- **Jam Sibuk dengan Nilai Monetary Tinggi**  
  Pukul 07:00 - 09:00 & 16:00 - 18:00 memiliki nilai Monetary tertinggi, menunjukkan bahwa jam-jam ini adalah peak hours penyewaan sepeda, kemungkinan karena aktivitas commuting (berangkat & pulang kerja/sekolah).
- **Jam Sepi dengan Nilai Monetary Rendah**  
  Pukul 00:00 - 05:00 memiliki Monetary yang sangat rendah, menunjukkan bahwa sangat sedikit orang yang menyewa sepeda di malam hingga dini hari.
- **Pola Konsisten Sepanjang Hari**  
  Penyewaan tetap cukup tinggi di siang hari (12:00 - 15:00), yang kemungkinan digunakan untuk rekreasi atau perjalanan santai.
""")

# ===================== #
# Visualisasi RFM Analysis berdasarkan Cuaca
# ===================== #
st.header("🌦️ RFM Analysis: Pengaruh Cuaca terhadap Penyewaan Sepeda")

# Contoh data RFM berdasarkan cuaca (silakan ganti dengan data aktual)
rfm_weather = pd.DataFrame({
    "weather_cond": [1, 2, 3],
    "RFM_Score": [144, 322, 411],
    "Monetary": [2257952, 996858, 37869]
})

# Plot heatmap
fig, ax = plt.subplots(figsize=(8, 5))
sns.heatmap(rfm_weather.pivot(index="weather_cond", columns="RFM_Score", values="Monetary"),
            cmap="coolwarm", annot=True, fmt=".0f", linewidths=0.5)

ax.set_title("RFM Analysis: Pengaruh Cuaca terhadap Penyewaan Sepeda", fontsize=14)
ax.set_xlabel("RFM Score")
ax.set_ylabel("Kondisi Cuaca")
ax.grid(True, linestyle='--', alpha=0.7)

st.pyplot(fig)
st.write("""
📌 **Insight:**  
- **Cuaca Cerah (Kategori 1) Mendominasi**  
  - Cuaca cerah memiliki nilai Monetary tertinggi, menunjukkan bahwa sebagian besar penyewaan sepeda terjadi saat cuaca mendukung.  
  - Skor RFM menunjukkan kombinasi frekuensi dan nilai transaksi tinggi, yang berarti pengguna aktif lebih sering menyewa di kondisi ini.  
- **Penyewaan Menurun Saat Cuaca Buruk**  
  - Saat kondisi cuaca memburuk (kategori 2: mendung, kategori 3: hujan ringan), nilai Monetary dan frekuensi penyewaan menurun drastis.  
  - Penyewaan paling sedikit terjadi saat hujan ringan atau lebih buruk, menunjukkan dampak besar kondisi cuaca terhadap jumlah pengguna.  
""")

# ===================== #
# Footer
# ===================== #
st.markdown("---")