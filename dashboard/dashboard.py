import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

st.header('Bike Sharing :🚲')

# Load data
day_df = pd.read_csv("all_data.csv")
day_df["dteday"] = pd.to_datetime(day_df["dteday"])
day_df["month"] = day_df["dteday"].dt.month
day_df["year"] = day_df["dteday"].dt.year

# Menambahkan kolom nama bulan
month_names = {1: "Januari", 2: "Februari", 3: "Maret", 4: "April", 5: "Mei", 6: "Juni",
               7: "Juli", 8: "Agustus", 9: "September", 10: "Oktober", 11: "November", 12: "Desember"}
day_df["month_name"] = day_df["month"].map(month_names)

# Menentukan rentang tanggal minimum dan maksimum
min_date_days = day_df["dteday"].min()
max_date_days = day_df["dteday"].max()

# Sidebar untuk memilih rentang waktu
with st.sidebar:
    st.image("https://png.pngtree.com/thumb_back/fw800/background/20220428/pngtree-bicycle-rent-isometric-background-with-bike-parking-and-map-vector-illustration-image_1104660.jpg")
    start_date, end_date = st.date_input(
        label='Rentang Waktu',
        min_value=min_date_days,
        max_value=max_date_days,
        value=[min_date_days, max_date_days]
    )

# Mengonversi tanggal dari date ke datetime untuk perbandingan
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Menyaring data berdasarkan rentang waktu yang dipilih
main_df_days = day_df[(day_df["dteday"] >= start_date) & (day_df["dteday"] <= end_date)]

# Lanjutkan dengan analisis dan visualisasi data sesuai kode yang sebelumnya.
# Misalnya, sebagai contoh bagian awal:
# 1. Bulan dengan Penyewaan Sepeda Terbanyak dan Tersedikit
monthly_rentals = main_df_days.groupby("month_name")["count"].sum().reset_index().sort_values(by="count", ascending=False)
most_rented_month = monthly_rentals.iloc[0]
least_rented_month = monthly_rentals.iloc[-1]

st.subheader("1. Bulan dengan Penyewaan Sepeda Terbanyak dan Tersedikit")
st.write(f"Bulan dengan penyewaan terbanyak: {most_rented_month['month_name']} dengan jumlah penyewaan {most_rented_month['count']}")
st.write(f"Bulan dengan penyewaan tersedikit: {least_rented_month['month_name']} dengan jumlah penyewaan {least_rented_month['count']}")
fig, ax = plt.subplots(1, 2, figsize=(20, 8))
sns.barplot(x="month_name", y="count", data=monthly_rentals.head(5), palette="Blues", ax=ax[0])
ax[0].set_title("Top 5 Bulan dengan Penyewaan Terbanyak")
ax[0].set_xlabel("Bulan")
ax[0].set_ylabel("Jumlah Penyewaan")
sns.barplot(x="month_name", y="count", data=monthly_rentals.tail(5).sort_values(by="count", ascending=True), palette="Reds", ax=ax[1])
ax[1].set_title("Top 5 Bulan dengan Penyewaan Tersedikit")
ax[1].set_xlabel("Bulan")
ax[1].set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# 2. Performa Penyewaan Sepeda dalam Beberapa Tahun Terakhir
year_counts = main_df_days.groupby("year")["count"].max().reset_index()

st.subheader("2. Performa Penyewaan Sepeda dalam Beberapa Tahun Terakhir")
fig, ax = plt.subplots(figsize=(25, 5))
ax.plot(year_counts["year"], year_counts["count"], marker='o', color="#90CAF9", label='Jumlah Maksimum per Tahun')
ax.set_xlabel("Tahun")
ax.set_ylabel("Jumlah Penyewaan Maksimum")
ax.set_title("Grafik Jumlah Penyewaan Maksimum per Tahun")
ax.legend()
st.pyplot(fig)

# 3. Musim dengan Penyewaan Sepeda Tersedikit
seasonal_rentals = main_df_days.groupby("season")["count"].sum().reset_index().sort_values(by="count", ascending=True)

st.subheader("3. Musim dengan Penyewaan Sepeda Tersedikit")
colors = ["#66B3FF", "#FFCC99"]
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(x="season", y="count", data=seasonal_rentals, palette=colors)
ax.set_title("Grafik Jumlah Penyewaan per Musim")
ax.set_xlabel("Musim")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

# 4. Perbandingan Penyewa Sepeda: Registered vs Casual
total_casual = main_df_days['casual'].sum()
total_registered = main_df_days['registered'].sum()

st.subheader("4. Perbandingan Penyewa Sepeda: Registered vs Casual")
labels = ['Casual', 'Registered']
sizes = [total_casual, total_registered]
colors = ["#FFCC99", "#66B3FF"]
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
ax.axis('equal')
st.pyplot(fig)
