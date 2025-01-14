import streamlit as st

# Fungsi untuk menghitung BMR (Basal Metabolic Rate)
def hitung_bmr(jenis_kelamin, berat, tinggi, usia):
    if jenis_kelamin == "Pria":
        return 88.36 + (13.4 * berat) + (4.8 * tinggi) - (5.7 * usia)
    elif jenis_kelamin == "Wanita":
        return 447.6 + (9.2 * berat) + (3.1 * tinggi) - (4.3 * usia)

# Fungsi untuk menghitung total kebutuhan kalori harian
def hitung_kalori_harian(bmr, tingkat_aktivitas):
    aktivitas = {
        "Sedentary (Tidak Aktif)": 1.2,
        "Light (Aktivitas Ringan)": 1.375,
        "Moderate (Aktivitas Sedang)": 1.55,
        "Active (Aktivitas Tinggi)": 1.725,
        "Very Active (Sangat Aktif)": 1.9,
    }
    return bmr * aktivitas.get(tingkat_aktivitas, 1.2)

# Fungsi untuk memberikan rekomendasi kalori berdasarkan tujuan
def rekomendasi_diet(kalori_harian, tujuan):
    if tujuan == "Turun Berat Badan":
        return kalori_harian - 500
    elif tujuan == "Naik Berat Badan":
        return kalori_harian + 500
    elif tujuan == "Stabil":
        return kalori_harian

# Judul aplikasi
st.title("Aplikasi Perhitungan Kebutuhan Kalori dan Rekomendasi Diet")

# Input data pengguna
st.header("Masukkan Data Anda:")
jenis_kelamin = st.radio("Jenis Kelamin:", ["Pria", "Wanita"])
berat = st.number_input("Berat Badan (kg):", min_value=1.0, step=0.1)
tinggi = st.number_input("Tinggi Badan (cm):", min_value=1.0, step=0.1)
usia = st.number_input("Usia (tahun):", min_value=1, step=1)
tingkat_aktivitas = st.selectbox(
    "Tingkat Aktivitas:",
    [
        "Sedentary (Tidak Aktif)",
        "Light (Aktivitas Ringan)",
        "Moderate (Aktivitas Sedang)",
        "Active (Aktivitas Tinggi)",
        "Very Active (Sangat Aktif)",
    ],
)
tujuan = st.selectbox("Tujuan Diet:", ["Turun Berat Badan", "Naik Berat Badan", "Stabil"])

# Tombol untuk menghitung
if st.button("Hitung Kebutuhan Kalori"):
    # Hitung BMR
    bmr = hitung_bmr(jenis_kelamin, berat, tinggi, usia)
    # Hitung kebutuhan kalori harian
    kalori_harian = hitung_kalori_harian(bmr, tingkat_aktivitas)
    # Rekomendasi kalori berdasarkan tujuan diet
    target_kalori = rekomendasi_diet(kalori_harian, tujuan)

    # Tampilkan hasil
    st.subheader("Hasil Perhitungan:")
    st.write(f"*Kebutuhan Kalori Harian (BMR):* {bmr:.2f} kalori")
    st.write(f"*Total Kebutuhan Kalori (Berdasarkan Aktivitas):* {kalori_harian:.2f} kalori")
    st.write(f"*Rekomendasi Kalori Harian (Berdasarkan Tujuan):* {target_kalori:.2f} kalori")

    # Input tambahan untuk menghitung kalori yang perlu dibakar
    asupan = st.number_input("Masukkan Asupan Kalori Harian Anda (opsional):", min_value=0.0, step=1.0)
    if asupan > 0:
        kalori_dibakar = target_kalori - asupan
        st.write(f"*Kalori yang Perlu Dibakar untuk Mencapai Target:* {kalori_dibakar:.2f} kalori")
