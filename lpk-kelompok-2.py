import streamlit as st

# Judul aplikasi
st.title("Kalkulator Kalori")

# Deskripsi aplikasi
st.write(
    "Masukkan data di bawah ini untuk mendapatkan jumlah kalori dan memperhitungkan kebutuhan kalori Anda."
)

# Form input data pengguna
with st.form("form_kalkulator"):
    usia = st.number_input("Usia", min_value=0, value=0, step=1)
    jenis_kelamin = st.selectbox("Jenis kelamin", ["Pria", "Wanita"])
    
    col1, col2 = st.columns(2)
    with col1:
        berat_badan = st.number_input("Berat Badan Saat Ini", min_value=0.0, value=0.0, step=0.1)
        satuan_berat = st.selectbox("Satuan Berat", ["Kg", "Pounds"])
    with col2:
        tinggi_badan = st.number_input("Tinggi Badan", min_value=0.0, value=0.0, step=0.1)
        satuan_tinggi = st.selectbox("Satuan Tinggi", ["cm", "ft/in"])
    
    aktivitas = st.selectbox(
        "Aktivitas Kegiatan",
        ["Tidak banyak bergerak", "Aktif ringan", "Aktif sedang", "Aktif berat", "Sangat aktif"]
    )
    
    # Tombol submit
    submit = st.form_submit_button("Hitung")

# Fungsi untuk menghitung BMR
def hitung_bmr(berat, tinggi, usia, jenis_kelamin):
    if jenis_kelamin == "Pria":
        return (10 * berat) + (6.25 * tinggi) - (5 * usia) + 5
    else:
        return (10 * berat) + (6.25 * tinggi) - (5 * usia) - 161

# Faktor aktivitas
aktivitas_faktor = {
    "Tidak banyak bergerak": 1.2,
    "Aktif ringan": 1.375,
    "Aktif sedang": 1.55,
    "Aktif berat": 1.725,
    "Sangat aktif": 1.9
}

# Konversi satuan berat dan tinggi jika diperlukan
if satuan_berat == "Pounds":
    berat_badan = berat_badan * 0.453592  # Convert pounds to kg
if satuan_tinggi == "ft/in":
    tinggi_badan = tinggi_badan * 30.48  # Convert feet to cm

# Perhitungan jika tombol submit ditekan
if submit:
    bmr = hitung_bmr(berat_badan, tinggi_badan, usia, jenis_kelamin)
    tdee = bmr * aktivitas_faktor[aktivitas]
    
    # Tampilkan hasil
    st.subheader("Hasil Perhitungan")
    st.write(f"**BMR (Basal Metabolic Rate):** {int(bmr)} kalori/hari")
    st.write(f"**TDEE (Total Daily Energy Expenditure):** {int(tdee)} kalori/hari")
    
    # Penjelasan hasil dalam bentuk opsional (expandable)
    with st.expander("Klik untuk penjelasan lebih lanjut"):
        st.write(
            """
            **BMR (Basal Metabolic Rate)** adalah jumlah kalori yang dibutuhkan tubuh Anda untuk menjalankan fungsi dasar 
            seperti pernapasan, pencernaan, dan peredaran darah saat Anda tidak melakukan aktivitas fisik. 
            Ini adalah jumlah kalori yang dibakar tubuh Anda hanya untuk bertahan hidup.
            
            **TDEE (Total Daily Energy Expenditure)** adalah jumlah kalori yang dibakar tubuh Anda dalam sehari 
            berdasarkan tingkat aktivitas fisik Anda. Ini memperhitungkan kegiatan sehari-hari seperti berjalan, berolahraga, 
            dan aktivitas lainnya.
            
            - Jika tujuan Anda adalah **menurunkan berat badan**, Anda harus mengonsumsi kalori lebih sedikit dari TDEE.
            - Jika tujuan Anda adalah **menambah berat badan**, Anda perlu mengonsumsi lebih banyak kalori dari TDEE.
            - Jika tujuan Anda adalah **menjaga berat badan**, cobalah untuk mengonsumsi kalori yang seimbang dengan TDEE Anda.
            """
        )
    st.write("Gunakan nilai ini untuk menyesuaikan konsumsi kalori Anda sesuai tujuan diet.")

# Footer
st.write("---")
st.caption("Dibuat oleh [kelompok 2 kelas 2G Nanoteknologi Pangan], dengan rumus Mifflin-St Jeor")
