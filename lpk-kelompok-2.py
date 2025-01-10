import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Kalkulator Diet dan Kandungan Energi Makanan")

# Deskripsi aplikasi
st.markdown("""
Aplikasi ini akan membantu Anda menghitung kebutuhan kalori harian untuk diet, serta kandungan energi dari makanan yang Anda konsumsi.
""")

# Input pengguna untuk berat badan, tinggi badan, usia, dan tingkat aktivitas
st.header("Masukkan Data Pribadi Anda")
berat_badan = st.number_input("Berat Badan (kg):", min_value=0, value=60, step=1)
tinggi_badan = st.number_input("Tinggi Badan (cm):", min_value=0, value=165, step=1)
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

# Menampilkan hasil perhitungan
st.header("Hasil Perhitungan Kalori")
st.write(f"BMR (Basal Metabolic Rate) Anda: {int(bmr)} kalori/hari")
st.write(f"TDEE (Total Daily Energy Expenditure): {int(tdee)} kalori/hari")
st.write(f"Kalori harian yang disarankan untuk tujuan diet '{tujuan_diet}': {int(kalori_target)} kalori/hari")

# Saran kalori yang harus dibakar
st.header("Saran Kalori yang Harus Dibakar")
if tujuan_diet == "Menurunkan Berat Badan":
    kalori_bakar = tdee - 500  # Defisit kalori
    st.write(f"Saran kalori yang harus dibakar untuk penurunan berat badan: {int(kalori_bakar)} kalori per hari")
    st.write("Saran aktivitas: Berolahraga dengan intensitas sedang (seperti berjalan cepat atau jogging) selama 30-60 menit per hari.")
elif tujuan_diet == "Menjaga Berat Badan":
    st.write(f"Saran kalori yang harus dibakar untuk menjaga berat badan: {int(tdee)} kalori per hari")
    st.write("Saran aktivitas: Lakukan aktivitas fisik ringan hingga sedang secara teratur (seperti berjalan cepat atau bersepeda).")
elif tujuan_diet == "Menambah Massa Otot":
    kalori_bakar = tdee + 500  # Surplus kalori
    st.write(f"Saran kalori yang harus dibakar untuk menambah massa otot: {int(kalori_bakar)} kalori per hari")
    st.write("Saran aktivitas: Fokus pada latihan kekuatan (strength training) dan makan lebih banyak kalori yang sehat.")
