import streamlit as st

# Judul aplikasi
st.title("Kalkulator Kalori")

# Deskripsi aplikasi
st.write(
    "Kalkulator kalori ini menghitung kalori yang perlu Anda konsumsi sehubungan dengan tujuan kesehatan dan kebugaran Anda termasuk pemeliharaan berat badan, penurunan berat badan, dan penambahan otot. "
    "Dapatkan jumlah kalori dan masukkan ke dalam rencana diet Anda dengan mempertimbangkan berat badan Anda saat ini."
)

# Form input data pengguna
with st.form("form_kalkulator"):
    usia = st.number_input("Usia", min_value=0, value=20, step=1)
    jenis_kelamin = st.selectbox("Jenis kelamin", ["Jantan", "Betina"])
    rumus = st.selectbox("Rumus", ["Revised Harris-Benedict", "Mifflin-St Jeor", "Katch-McArdle"])
    
    col1, col2 = st.columns(2)
    with col1:
        berat_badan = st.number_input("Berat Badan Saat Ini", min_value=0, value=54, step=1)
        satuan_berat = st.selectbox(" ", ["Kg", "Pounds"])
    with col2:
        tinggi_badan = st.number_input("Ketinggian", min_value=0, value=9, step=1)
        satuan_tinggi = st.selectbox(" ", ["cm", "ft/in"])
    
    aktivitas = st.selectbox(
        "Pilih Level Aktivitas",
        ["Tidak banyak bergerak", "Aktif ringan", "Aktif sedang", "Aktif berat", "Sangat aktif"]
    )
    satuan_hasil = st.selectbox("Satuan Hasil", ["Kalori", "Kilojoule"])
    
    # Tombol submit
    submit = st.form_submit_button("Hitung")

# Hasil output jika tombol submit ditekan
if submit:
    st.write("Hasil perhitungan akan muncul di sini. (Fitur perhitungan bisa ditambahkan sesuai rumus pilihan.)")
