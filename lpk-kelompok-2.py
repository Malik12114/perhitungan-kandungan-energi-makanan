import streamlit as st
import pandas as pd
import altair as alt  # Menggunakan altair untuk grafik

# Judul aplikasi
st.title("Kalkulator Diet dan Kandungan Energi Makanan")

# Deskripsi aplikasi
st.markdown("""
Aplikasi ini akan membantu Anda menghitung kebutuhan kalori harian untuk diet, serta kandungan energi dari makanan yang Anda konsumsi.
""")

# Input pengguna untuk berat badan, tinggi badan, usia, dan tingkat aktivitas
st.header("Masukkan Data Pribadi Anda")
berat_badan = st.number_input("Berat Badan (kg):", min_value=0.0, value=60.0, step=0.1)
tinggi_badan = st.number_input("Tinggi Badan (cm):", min_value=0.0, value=165.0, step=1.0)  # Ubah min_value ke 0.0 untuk konsistensi tipe data float
usia = st.number_input("Usia (tahun):", min_value=0, value=30, step=1)
jenis_kelamin = st.selectbox("Jenis Kelamin:", ["Pria", "Wanita"])

# Pilihan tingkat aktivitas
st.header("Tingkat Aktivitas Fisik")
aktivitas = st.selectbox("Pilih tingkat aktivitas fisik:", [
    "Tidak aktif (sedentari)",
    "Aktif ringan (olahraga ringan 1-3 hari/minggu)",
    "Aktif sedang (olahraga sedang 3-5 hari/minggu)",
    "Aktif berat (olahraga intens 6-7 hari/minggu)",
    "Sangat aktif (pekerjaan fisik berat atau latihan intensif)"
])

# Perhitungan BMR dengan rumus Harris-Benedict
def hitung_bmr(berat, tinggi, usia, jenis_kelamin):
    if jenis_kelamin == "Pria":
        bmr = 66.5 + (13.75 * berat) + (5.003 * tinggi) - (6.75 * usia)
    else:
        bmr =  655.1 + (9.563 * berat) + (1.850 * tinggi) - (4.676 * usia)
    return bmr

bmr = hitung_bmr(berat_badan, tinggi_badan, usia, jenis_kelamin)

# Faktor aktivitas (TDEE multiplier)
aktivitas_faktor = {
    "Tidak aktif (sedentari)": 1.2,
    "Aktif ringan (olahraga ringan 1-3 hari/minggu)": 1.375,
    "Aktif sedang (olahraga sedang 3-5 hari/minggu)": 1.55,
    "Aktif berat (olahraga intens 6-7 hari/minggu)": 1.725,
    "Sangat aktif (pekerjaan fisik berat atau latihan intensif)": 1.9
}

tdee = bmr * aktivitas_faktor[aktivitas]

# Pilihan tujuan diet
st.header("Pilih Tujuan Diet Anda")
tujuan_diet = st.selectbox("Apa tujuan diet Anda?", ["Menurunkan Berat Badan", "Menjaga Berat Badan", "Menambah Massa Otot"])

# Menentukan kalori defisit atau surplus
kalori_target = tdee
if tujuan_diet == "Menurunkan Berat Badan":
    kalori_target -= 500  # Defisit kalori untuk penurunan berat badan (500 kalori defisit)
elif tujuan_diet == "Menambah Massa Otot":
    kalori_target += 500  # Surplus kalori untuk penambahan massa otot (500 kalori surplus)

# Menampilkan hasil
st.header("Hasil Perhitungan")
st.write(f"BMR (Basal Metabolic Rate) Anda: {bmr:.2f} kalori/hari")
st.write(f"TDEE (Total Daily Energy Expenditure): {tdee:.2f} kalori/hari")
st.write(f"Kalori harian yang disarankan untuk tujua
