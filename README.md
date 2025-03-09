# 🚲 Bike Sharing Dashboard

Dashboard interaktif berbasis Streamlit untuk menganalisis pola penyewaan sepeda berdasarkan waktu, pengaruh cuaca, dan RFM Analysis.

---

## 📊 Fitur Dashboard

1. Pola Penyewaan Sepeda: Analisis penyewaan berdasarkan waktu dalam sehari.
2. Pengaruh Cuaca terhadap Penyewaan: Visualisasi dampak kondisi cuaca pada jumlah penyewaan.
3. Analisis RFM: Segmentasi pengguna berdasarkan kebiasaan penyewaan sepeda.

---

## 📂 Dataset
Dataset yang digunakan terdapat di dalam repository ini. Pastikan Anda telah mengunduhnya sebelum menjalankan aplikasi

   **Pastikan File Terunduh Sebelum Diproses**
   ```python
   import pandas as pd
   day_df = pd.read_csv('day.csv')
   hour_df = pd.read_csv('hour.csv')
   ```

---

## 🚀 Cara Menjalankan

### 1. **Persyaratan**
Pastikan Anda sudah menginstal **Python 3.7+** dan memiliki paket yang dibutuhkan:

```sh
pip install streamlit pandas matplotlib seaborn
```

### 2. **Menjalankan Dashboard Secara Lokal**
1. Clone repositori ini atau unduh file sumbernya:
   ```sh
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```
2. Jalankan Streamlit:
   ```sh
   streamlit run dashboard.py
   ```
3. Buka browser dan akses **`http://localhost:8503`**.

---

## 🌍 Menjalankan di Streamlit Cloud
Jika ingin melakukan **deploy ke Streamlit Cloud**, ikuti langkah ini:

1. **Tambahkan file `requirements.txt`** di GitHub:
   ```
   streamlit==1.42.2
   pandas==2.2.3
   matplotlib==3.10.1
   seaborn==0.13.2

   ```

2. **Push ke GitHub**, deploy di [Streamlit Cloud](https://share.streamlit.io/).

3. Jika ada perubahan di repository, **restart aplikasi** melalui dashboard Streamlit Cloud agar pembaruan diterapkan.

---

## 👤 Author
**Mohamad Farrel Aryansyah MC-27**
