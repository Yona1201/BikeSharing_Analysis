Berikut `README.md` yang lebih lengkap untuk proyek ini:

---

# Submission Dicoding "Belajar Analisis Data dengan Python"

![SS Deploy](https://dicoding-web-img.sgp1.cdn.digitaloceanspaces.com/original/academy/dos-68705e63ee0ef9422542d4e4ec2de35320241029223707.png)

Proyek ini menganalisis data penyewaan sepeda dengan tujuan memahami pola dan tren dalam penggunaan layanan berbagi sepeda. Proses mencakup pembersihan data, analisis mendalam, dan visualisasi hasil menggunakan dashboard interaktif berbasis Streamlit. Aplikasi Streamlit dapat diakses [di sini](https://bikesharinganalysis-yonaa.streamlit.app/).

## Struktur Direktori

- **/data**: Berisi data mentah dalam format .csv, yaitu `day.csv` dan `hour.csv`.
- **/dashboard**: Berisi `dashboard.py` untuk membuat dashboard hasil analisis, serta data yang telah dibersihkan.
- **notebook.ipynb**: File ini digunakan untuk analisis data, eksplorasi, dan visualisasi.

## Extract Zip

Ekstrak file zip proyek sebelum menjalankan kode.

## Setup Environment

### Menggunakan Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

### Menggunakan Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Menjalankan Aplikasi Streamlit
```
streamlit run dashboard.py
```

--- 

Pastikan semua dependensi yang tercantum di `requirements.txt` sudah terpasang untuk menjalankan proyek ini dengan lancar.
