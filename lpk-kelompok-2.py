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
tinggi_badan = st.number_input("Tinggi Badan (cm):", min_value=0.0, value=165.0, step=1.0)
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

# Input makanan yang dikonsumsi
st.header("Masukkan Data Berat Makanan Yang Anda Konsumsi")
karbohidrat = st.number_input("Karbohidrat (gram):", min_value=0.0, value=0.0, step=0.1)
protein = st.number_input("Protein (gram):", min_value=0.0, value=0.0, step=0.1)
lemak = st.number_input("Lemak (gram):", min_value=0.0, value=0.0, step=0.1)

# Perhitungan energi makanan yang dikonsumsi
def hitung_kalori(karbo, prot, lemak):
    energi_karbo = karbo * 4  # 4 kalori per gram
    energi_protein = prot * 4  # 4 kalori per gram
    energi_lemak = lemak * 9  # 9 kalori per gram
    total_energi = energi_karbo + energi_protein + energi_lemak
    return energi_karbo, energi_protein, energi_lemak, total_energi

energi_karbo, energi_protein, energi_lemak, total_energi = hitung_kalori(karbohidrat, protein, lemak)

# Gabungkan semua hasil perhitungan dalam satu tabel (bulatkan hasil ke bilangan bulat)
data = {
    "Komponen": [
        "BMR (Basal Metabolic Rate)", 
        "TDEE (Total Daily Energy Expenditure)", 
        "Kalori Target (Diet)", 
        "Karbohidrat", 
        "Protein", 
        "Lemak", 
        "Total Energi Makanan"
    ],
    "Hasil Perhitungan (kkal)": [
        round(bmr), 
        round(tdee), 
        round(kalori_target), 
        round(energi_karbo), 
        round(energi_protein), 
        round(energi_lemak), 
        round(total_energi)
    ]
}

df = pd.DataFrame(data)

# Menampilkan tabel hasil perhitungan diet dan energi makanan
st.header("Tabel Hasil Perhitungan Diet dan Energi Makanan")
st.dataframe(df)  # Tabel interaktif

# Data diet untuk ditampilkan di bawah tabel energi makanan
st.subheader("Tujuan Diet Anda: " + tujuan_diet)
st.write(f"BMR (Basal Metabolic Rate): {round(bmr)} kalori/hari")
st.write(f"TDEE (Total Daily Energy Expenditure): {round(tdee)} kalori/hari")
st.write(f"Kalori harian yang disarankan untuk tujuan diet '{tujuan_diet}': {round(kalori_target)} kalori/hari")

# Grafik Bar Chart (menggunakan Altair)
if st.checkbox("Tampilkan Grafik Bar Chart"):
    # Data untuk bar chart
    data_chart = pd.DataFrame({
        'Komponen': ["Karbohidrat", "Protein", "Lemak"],
        'Energi (kkal)': [energi_karbo, energi_protein, energi_lemak]
    })
    
    # Membuat bar chart menggunakan Altair
    chart = alt.Chart(data_chart).mark_bar().encode(
        x='Komponen',
        y='Energi (kkal)',
        color='Komponen',
        tooltip=['Komponen', 'Energi (kkal)']
    ).properties(
        title="Distribusi Energi Makanan"
    )
    
    # Menampilkan chart
    st.altair_chart(chart, use_container_width=True)

# Footer
st.write("---")
st.caption("Dibuat oleh [kelas 2G Nanoteknologi Pangan]")
