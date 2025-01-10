import streamlit as st

# Judul aplikasi
st.title("Kalkulator Kalori Harian")

# Deskripsi aplikasi
st.markdown("""
Aplikasi ini membantu Anda menghitung kalori yang harus dikonsumsi dan dibakar setiap harinya berdasarkan data pribadi dan tujuan diet Anda.
""")

# Input pengguna untuk berat badan, tinggi badan, usia, dan jenis kelamin
st.header("Masukkan Data Pribadi Anda")
berat_badan = st.number_input("Berat Badan (kg):", min_value=0.0, value=60.0, step=0.1)
tinggi_badan = st.number_input("Tinggi Badan (cm):", min_value=0.0, value=165.0, step=1.0)
usia = st.number_input("Usia (tahun):", min_value=0, value=30, step=1)
jenis_kelamin = st.selectbox("Jenis Kelamin:", ["Pria", "Wanita"])

# Pilihan tingkat aktivitas
aktivitas = st.selectbox("Pilih tingkat aktivitas fisik:", [
    "Tidak aktif",
    "Aktif ringan",
    "Aktif sedang",
    "Aktif berat"
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
    "Tidak aktif": 1.2,
    "Aktif ringan": 1.375,
    "Aktif sedang": 1.55,
    "Aktif berat": 1.725
}

tdee = bmr * aktivitas_faktor[aktivitas]

# Pilihan tujuan diet
st.header("Pilih Tujuan Diet Anda")
tujuan_diet = st.selectbox("Tujuan Diet:", ["Menurunkan Berat Badan", "Menjaga Berat Badan", "Menambah Massa Otot"])

# Menentukan kalori target
kalori_target = tdee
if tujuan_diet == "Menurunkan Berat Badan":
    kalori_target -= 500  # Defisit kalori
elif tujuan_diet == "Menambah Massa Otot":
    kalori_target += 500  # Surplus kalori

# Menampilkan hasil
st.header("Hasil Perhitungan Kalori")
st.write(f"BMR: {round(bmr)} kalori/hari")
st.write(f"TDEE: {round(tdee)} kalori/hari")
st.write(f"Kalori yang disarankan untuk diet '{tujuan_diet}': {round(kalori_target)} kalori/hari")

# Input makanan yang dikonsumsi
st.header("Masukkan Data Makanan yang Dikonsumsi")
karbohidrat = st.number_input("Karbohidrat (gram):", min_value=0.0, value=0.0, step=0.1)
protein = st.number_input("Protein (gram):", min_value=0.0, value=0.0, step=0.1)
lemak = st.number_input("Lemak (gram):", min_value=0.0, value=0.0, step=0.1)

# Perhitungan kalori dari makanan yang dikonsumsi
kalori_makanan = karbohidrat * 4 + protein * 4 + lemak * 9

# Menampilkan hasil perhitungan kalori makanan
st.header("Kalori yang Dikonsumsi dari Makanan")
st.write(f"Karbohidrat: {karbohidrat * 4} kalori")
st.write(f"Protein: {protein * 4} kalori")
st.write(f"Lemak: {lemak * 9} kalori")
st.write(f"Total kalori dari makanan: {round(kalori_makanan)} kalori")

# Perbandingan kalori
st.header("Perbandingan Kalori Masuk dan Dibakar")
st.write(f"Kalori Masuk: {round(kalori_makanan)} kalori")
st.write(f"Kalori Dibakar (TDEE): {round(tdee)} kalori")
