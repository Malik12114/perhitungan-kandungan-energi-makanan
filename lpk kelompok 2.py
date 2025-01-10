import streamlit as st
import pandas as pd

# Judul aplikasi
st.title("Kalkulator Kandungan Energi Makanan")

# Deskripsi aplikasi
st.markdown("""
Aplikasi ini dapat membantu Anda untuk menghitung kandungan energi dari makanan yang Anda konsumsi.
""")

# Input pengguna
st.header("Masukkan Data Berat Makanan Yang Anda Konsumsi")
karbohidrat = st.number_input("Karbohidrat (gram):", min_value=0.0, value=0.0, step=0.1)
protein = st.number_input("Protein (gram):", min_value=0.0, value=0.0, step=0.1)
lemak = st.number_input("Lemak (gram):", min_value=0.0, value=0.0, step=0.1)

# Perhitungan energi
def hitung_kalori(karbo, prot, lemak):
    energi_karbo = karbo * 4  # 4 kalori per gram
    energi_protein = prot * 4  # 4 kalori per gram
    energi_lemak = lemak * 9  # 9 kalori per gram
    total_energi = energi_karbo + energi_protein + energi_lemak
    return energi_karbo, energi_protein, energi_lemak, total_energi

energi_karbo, energi_protein, energi_lemak, total_energi = hitung_kalori(karbohidrat, protein, lemak)

# Tampilkan hasil dalam tabel
st.header("Hasil Perhitungan Energi")
data = {
    "Komponen": ["Karbohidrat", "Protein", "Lemak", "Total"],
    "Energi (kkal)": [energi_karbo, energi_protein, energi_lemak, total_energi]
}
df = pd.DataFrame(data)
st.table(df)

# Grafik Pie Chart (opsional)
if st.checkbox("Tampilkan Grafik Pie Chart"):
    import matplotlib.pyplot as plt

    # Data untuk pie chart
    labels = ["Karbohidrat", "Protein", "Lemak"]
    values = [energi_karbo, energi_protein, energi_lemak]
    colors = ["#FF9999", "#99FF99", "#9999FF"]

    # Plot grafik
    plt.figure(figsize=(6, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", colors=colors, startangle=140)
    plt.title("Distribusi Energi Makanan")
    st.pyplot(plt)

# Footer
st.write("---")
st.caption("Dibuat oleh [kelompok 2 kelas 2G Nanoteknologi Pangan]")
