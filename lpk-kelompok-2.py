import streamlit as st

# Judul aplikasi
st.title("Kalkulator Kalori dan Rekomendasi Kegiatan")

# Deskripsi aplikasi
st.write(
    "Masukkan data di bawah ini untuk mendapatkan jumlah kalori, memperhitungkan kebutuhan kalori Anda, dan rekomendasi kegiatan untuk mencapai tujuan Anda."
)

# Form input data pengguna
with st.form("form_kalkulator"):
    usia = st.number_input("Usia", min_value=0, value=0, step=1)
    jenis_kelamin = st.selectbox("Jenis kelamin", ["Pria", "Wanita"])
    
    col1, col2 = st.columns(2)
    with col1:
        berat_badan = st.number_input("Berat Badan Saat Ini (kg)", min_value=0, value=0, step=1)
    with col2:
        tinggi_badan = st.number_input("Tinggi Badan (cm)", min_value=0, value=0, step=1)
    
    aktivitas = st.selectbox(
        "Aktivitas Kegiatan",
        ["Tidak banyak bergerak", "Aktif ringan", "Aktif sedang", "Aktif berat", "Sangat aktif"]
    )
    
    tujuan = st.selectbox(
        "Tujuan Anda",
        ["Menurunkan berat badan", "Menambah berat badan", "Menjaga berat badan"]
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

# Perhitungan jika tombol submit ditekan
if submit:
    bmr = hitung_bmr(berat_badan, tinggi_badan, usia, jenis_kelamin)
    tdee = bmr * aktivitas_faktor[aktivitas]
    
    # Hitung kebutuhan kalori berdasarkan tujuan
    if tujuan == "Menurunkan berat badan":
        target_kalori = tdee - 500  # Defisit kalori 500/hari
    elif tujuan == "Menambah berat badan":
        target_kalori = tdee + 500  # Surplus kalori 500/hari
    else:  # Menjaga berat badan
        target_kalori = tdee
    
    # Tampilkan hasil
    st.subheader("Hasil Perhitungan")
    st.write(f"**BMR (Basal Metabolic Rate):** {int(bmr)} kalori/hari")
    st.write(f"**TDEE (Total Daily Energy Expenditure):** {int(tdee)} kalori/hari")
    st.write(f"**Kebutuhan Kalori Harian (sesuai tujuan):** {int(target_kalori)} kalori/hari")
    
    # Rekomendasi kegiatan
    st.subheader("Rekomendasi Kegiatan")
    if tujuan == "Menurunkan berat badan":
        st.write(
            """
            - **Olahraga kardio** seperti lari, bersepeda, atau berenang selama 30-60 menit per hari.
            - **Latihan kekuatan** (strength training) 2-3 kali per minggu untuk menjaga massa otot.
            - Kurangi konsumsi makanan tinggi gula dan lemak jenuh.
            - Perbanyak konsumsi sayuran, buah-buahan, dan protein rendah lemak.
            """
        )
    elif tujuan == "Menambah berat badan":
        st.write(
            """
            - **Latihan kekuatan** (strength training) 4-5 kali per minggu untuk membangun otot.
            - Tambahkan kalori dari sumber yang sehat seperti kacang-kacangan, alpukat, dan minyak zaitun.
            - Konsumsi lebih banyak protein seperti daging, telur, dan produk susu.
            - Pastikan tidur cukup (7-9 jam per malam) untuk pemulihan tubuh.
            """
        )
    else:  # Menjaga berat badan
        st.write(
            """
            - Pertahankan **rutin olahraga** seperti berjalan, yoga, atau bersepeda 3-5 kali per minggu.
            - Jaga pola makan seimbang dengan memperhatikan proporsi karbohidrat, protein, dan lemak.
            - Hindari kebiasaan makan berlebihan atau kekurangan kalori.
            - Lakukan monitoring berat badan secara rutin untuk menjaga stabilitas.
            """
        )
    
    # Penjelasan hasil dalam bentuk opsional (expandable)
    with st.expander("Klik untuk penjelasan lebih lanjut"):
        st.write(
            """
            **BMR (Basal Metabolic Rate)** adalah jumlah kalori yang dibutuhkan tubuh Anda untuk menjalankan fungsi dasar 
            seperti pernapasan, pencernaan, dan peredaran darah saat Anda tidak melakukan aktivitas fisik. 
            
            **TDEE (Total Daily Energy Expenditure)** adalah jumlah kalori yang dibakar tubuh Anda dalam sehari 
            berdasarkan tingkat aktivitas fisik Anda. Ini memperhitungkan kegiatan sehari-hari seperti berjalan, berolahraga, 
            dan aktivitas lainnya.
            """
        )

# Footer
st.write("---")
st.caption("Dibuat oleh [kelompok 2 kelas 2G Nanoteknologi Pangan], dengan rumus Mifflin-St Jeor")
