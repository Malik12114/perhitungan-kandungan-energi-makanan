import streamlit as st

# Judul aplikasi
st.title("Kalkulator Kalori Harian")

# Input pengguna untuk berat badan, tinggi badan, usia, jenis kelamin, dan aktivitas
berat_badan = st.number_input("Berat Badan (kg):", min_value=0, value=60, step=1)
tinggi_badan = st.number_input("Tinggi Badan (cm):", min_value=0, value=165, step=1)
usia = st.number_input("Usia (tahun):", min_value=0, value=30, step=1)
jenis_kelamin = st.selectbox("Jenis Kelamin:", ["Pria", "Wanita"])
aktivitas = st.selectbox("Tingkat Aktivitas Fisik:", [
    "Tidak aktif", "Aktif ringan", "Aktif sedang", "Aktif berat", "Sangat aktif"
])

# Rumus BMR (Basal Metabolic Rate) Harris-Benedict
def hitung_bmr(berat, tinggi, usia, jenis_kelamin):
    if jenis_kelamin == "Pria":
        return 66.5 + (13.75 * berat) + (5.003 * tinggi) - (6.75 * usia)
    else:
        return 655.1 + (9.563 * berat) + (1.850 * tinggi) - (4.676 * usia)

# Faktor aktivitas fisik (TDEE multiplier)
aktivitas_faktor = {
    "Tidak aktif": 1.2,
    "Aktif ringan": 1.375,
    "Aktif sedang": 1.55,
    "Aktif berat": 1.725,
    "Sangat aktif": 1.9
}

# Hitung BMR dan TDEE
bmr = hitung_bmr(berat_badan, tinggi_badan, usia, jenis_kelamin)
tdee = bmr * aktivitas_faktor[aktivitas]

# Pilihan tujuan diet
tujuan_diet = st.selectbox("Tujuan Diet:", ["Menurunkan Berat Badan", "Menjaga Berat Badan", "Menambah Massa Otot"])

# Sesuaikan kalori berdasarkan tujuan diet
kalori_target = tdee
if tujuan_diet == "Menurunkan Berat Badan":
    kalori_target -= 500
elif tujuan_diet == "Menambah Massa Otot":
    kalori_target += 500

# Menampilkan hasil perhitungan
st.subheader("Hasil Perhitungan Kalori")
st.write(f"BMR (Basal Metabolic Rate): {int(bmr)} kalori/hari")
st.write(f"TDEE (Total Daily Energy Expenditure): {int(tdee)} kalori/hari")
st.write(f"Kalori yang disarankan untuk tujuan diet '{tujuan_diet}': {int(kalori_target)} kalori/hari")

# Saran kalori yang harus dibakar berdasarkan tujuan diet
st.subheader("Saran Aktivitas Fisik")
if tujuan_diet == "Menurunkan Berat Badan":
    st.write(f"Saran kalori yang harus dibakar: {int(tdee - 500)} kalori per hari")
elif tujuan_diet == "Menambah Massa Otot":
    st.write(f"Saran kalori yang harus dibakar: {int(tdee + 500)} kalori per hari")
else:
    st.write(f"Saran kalori yang harus dibakar: {int(tdee)} kalori per hari")
