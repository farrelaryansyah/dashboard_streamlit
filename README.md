# 🚲 Bike Sharing Dashboard

Dashboard interaktif berbasis Streamlit untuk menganalisis pola penyewaan sepeda berdasarkan waktu, pengaruh cuaca, dan Analisis RFM.

---

## 📊 Fitur Dashboard
1. **Pola Penyewaan Sepeda**: Analisis penyewaan berdasarkan waktu dalam sehari.
2. **Pengaruh Cuaca terhadap Penyewaan**: Visualisasi dampak kondisi cuaca pada jumlah penyewaan.
3. **Analisis RFM**: Segmentasi pengguna berdasarkan kebiasaan penyewaan sepeda.

---

## 📁 Dataset
Dataset yang digunakan dalam proyek ini terdiri dari dua file utama:
- **day.csv**: Data penyewaan harian sepeda.
- **hour.csv**: Data penyewaan sepeda per jam.

Pastikan dataset telah diunduh sebelum menjalankan aplikasi.

```python
import pandas as pd
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')
```

---

## 🌐 Setup Environment

Untuk memastikan lingkungan pengembangan siap digunakan, lakukan langkah berikut:

1. **Buat Virtual Environment (Opsional tetapi Disarankan)**
   ```sh
   python -m venv env
   source env/bin/activate  # Untuk macOS/Linux
   env\Scripts\activate  # Untuk Windows
   ```

2. **Instal Dependensi**
   ```sh
   pip install -r requirements.txt
   ```

3. **Pastikan Semua Dependensi Terinstal dengan Benar**
   ```sh
   python -c "import streamlit, pandas, matplotlib, seaborn)"
   ```
### Menggunakan Google Colab
1.⁠ ⁠Unduh proyek notebook.ipynb dan dataset.
2.⁠ ⁠Buka Google Colab di browser Anda.
3.⁠ ⁠Buat notebook baru.
4.⁠ ⁠Upload file notebook.ipynb⁠ dan dataset.
5.⁠ ⁠Hubungkan ke runtime yang tersedia.
6.⁠ ⁠Jalankan sel-sel kode.

---

## 🚀 Cara Menjalankan

### 1. **Persyaratan**
Pastikan Anda sudah menginstal **Python 3.7+** dan memiliki paket yang dibutuhkan:

```sh
pip install -r requirements.txt
```

Atau, jika ingin menginstal secara manual:

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
3. Buka browser dan akses **`http://localhost:8501`**.

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

2. **Push ke GitHub**, kemudian deploy di [Streamlit Cloud](https://share.streamlit.io/).

3. Jika ada perubahan di repository, **restart aplikasi** melalui dashboard Streamlit Cloud agar pembaruan diterapkan.

---

## 👤 Author
**Mohamad Farrel Aryansyah MC-27**

