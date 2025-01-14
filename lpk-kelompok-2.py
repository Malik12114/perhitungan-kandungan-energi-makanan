import streamlit as st

# Judul aplikasi
st.title("Kalkulator Kalori dan Diet Harian")

# Input data pengguna
berat_badan = st.number_input("Berat Badan (kg):", min_value=0, value=0, step=1)
tinggi_badan = st.number_input("Tinggi Badan (cm):", min_value=0, value=0, step=1)
usia = st.number_input("Usia (tahun):", min_value=0, value=0, step=1)
jenis_kelamin = st.selectbox("Jenis Kelamin:", ["Pria", "Wanita"])
aktivitas = st.selectbox("Tingkat Aktivitas Fisik:", ["Tidak aktif", "Aktif ringan", "Aktif sedang", "Aktif berat", "Sangat aktif"])

# Rumus BMR (Basal Metabolic Rate) Harris-Benedict
def hitung_bmr(berat, tinggi, usia, jenis_kelamin):
    if jenis_kelamin == "Pria":
        return 66 + (13.7 * berat) + (5 * tinggi) - (6.8 * usia)
    else:
        return 655 + (9.6 * berat) + (1.8 * tinggi) - (4.7 * usia)

# Faktor aktivitas fisik
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

# Input makanan yang dikonsumsi
st.header("Masukkan Kalori Makanan Yang Anda Konsumsi")
karbohidrat = st.number_input("Karbohidrat (gram):", min_value=0, value=0, step=1)
protein = st.number_input("Protein (gram):", min_value=0, value=0, step=1)
lemak = st.number_input("Lemak (gram):", min_value=0, value=0, step=1)

# Menghitung kalori yang dikonsumsi
kalori_karbo = karbohidrat * 4
kalori_protein = protein * 4
kalori_lemak = lemak * 9
kalori_makanan = kalori_karbo + kalori_protein + kalori_lemak

# Menampilkan hasil perhitungan kalori yang dikonsumsi
st.subheader("Hasil Kalori yang Dikonsumsi")
st.write(f"Kalori dari Karbohidrat: {int(kalori_karbo)} kalori")
st.write(f"Kalori dari Protein: {int(kalori_protein)} kalori")
st.write(f"Kalori dari Lemak: {int(kalori_lemak)} kalori")
st.write(f"Total Kalori yang Dikonsumsi: {int(kalori_makanan)} kalori")

# Menampilkan hasil perhitungan kalori harian
st.subheader("Hasil Perhitungan Kalori Harian")
st.write(f"BMR: {int(bmr)} kalori/hari")
st.write(f"TDEE: {int(tdee)} kalori/hari")
st.write(f"Kalori yang disarankan untuk tujuan diet '{tujuan_diet}': {int(kalori_target)} kalori/hari")

# Saran pengurangan kalori
st.subheader("Saran Pengurangan Kalori")
kalori_dikurangi = kalori_makanan - kalori_target
if kalori_dikurangi > 0:
    st.write(f"Untuk mencapai tujuan diet Anda, kurangi asupan sekitar {int(kalori_dikurangi)} kalori per hari.")
else:
    st.write("Kalori yang Anda konsumsi sudah sesuai dengan tujuan diet Anda.")
