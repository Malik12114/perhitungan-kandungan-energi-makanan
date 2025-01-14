import streamlit as st

# Judul aplikasi
st.title("Kalkulator Kalori Harian (Rumus Mifflin-St Jeor)")

# Penjelasan aplikasi
st.write("""
Aplikasi ini menggunakan rumus **Mifflin-St Jeor** untuk menghitung kebutuhan kalori harian Anda berdasarkan berat badan, tinggi badan, usia, dan tingkat aktivitas fisik.
""")

# Input data pengguna
usia = st.number_input("Usia (tahun):", min_value=0, value=0, step=1)
jenis_kelamin = st.selectbox("Jenis Kelamin:", ["Pria", "Wanita"])
berat_badan = st.number_input("Berat Badan (kg):", min_value=0, value=0, step=1)
tinggi_badan = st.number_input("Tinggi Badan (cm):", min_value=0, value=0, step=1)
aktivitas = st.selectbox(
    "Tingkat Aktivitas Fisik:",
    ["Tidak banyak bergerak", "Aktif ringan", "Aktif sedang", "Aktif berat", "Sangat aktif"]
)

# Rumus Mifflin-St Jeor
def hitung_bmr_mifflin(berat, tinggi, usia, jenis_kelamin):
    if jenis_kelamin == "Pria":
        return (10 * berat) + (6.25 * tinggi) - (5 * usia) + 5
    else:
        return (10 * berat) + (6.25 * tinggi) - (5 * usia) - 161

# Faktor aktivitas fisik
aktivitas_faktor = {
    "Tidak banyak bergerak": 1.2,
    "Aktif ringan": 1.375,
    "Aktif sedang": 1.55,
    "Aktif berat": 1.725,
    "Sangat aktif": 1.9
}

# Hitung BMR dan TDEE
bmr = hitung_bmr_mifflin(berat_badan, tinggi_badan, usia, jenis_kelamin)
tdee = bmr * aktivitas_faktor[aktivitas]

# Tujuan diet
tujuan_diet = st.selectbox("Tujuan Diet:", ["Menurunkan Berat Badan", "Menjaga Berat Badan", "Menambah Berat Badan"])

# Sesuaikan kalori berdasarkan tujuan diet
kalori_target = tdee
if tujuan_diet == "Menurunkan Berat Badan":
    kalori_target -= 500
elif tujuan_diet == "Menambah Berat Badan":
    kalori_target += 500

# Hasil perhitungan
st.subheader("Hasil Perhitungan Kalori Harian")
st.write(f"BMR (Basal Metabolic Rate): {int(bmr)} kalori/hari")
st.write(f"TDEE (Total Daily Energy Expenditure): {int(tdee)} kalori/hari")
st.write(f"Kalori yang disarankan untuk tujuan '{tujuan_diet}': {int(kalori_target)} kalori/hari")

# Saran aktivitas fisik atau konsumsi
st.subheader("Saran Diet dan Aktivitas")
if tujuan_diet == "Menurunkan Berat Badan":
    st.write(f"Kurangi asupan kalori harian sebesar 500 kalori dari kebutuhan TDEE Anda ({int(tdee)} kalori/hari).")
    st.write("Disarankan untuk meningkatkan aktivitas fisik seperti olahraga rutin.")
elif tujuan_diet == "Menambah Berat Badan":
    st.write(f"Tambahkan asupan kalori harian sebesar 500 kalori dari kebutuhan TDEE Anda ({int(tdee)} kalori/hari).")
    st.write("Konsumsilah makanan tinggi kalori seperti protein dan karbohidrat kompleks.")
else:
    st.write("Anda berada pada keseimbangan kalori. Pertahankan pola makan dan aktivitas fisik Anda.")
