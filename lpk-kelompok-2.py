import streamlit as st

# Judul aplikasi
st.title("Pemantauan Kalori Harian")
st.subheader("Aplikasi untuk Bulking atau Diet")

# Input data kalori
st.sidebar.header("Masukkan Data")
kalori_masuk = st.sidebar.number_input("Kalori yang dikonsumsi (kcal):", min_value=0.0, step=1.0)
kalori_bakar = st.sidebar.number_input("Kalori yang dibakar (kcal):", min_value=0.0, step=1.0)

# Perhitungan surplus/defisit kalori
if kalori_masuk and kalori_bakar:
    surplus_defisit = kalori_masuk - kalori_bakar
    if surplus_defisit > 0:
        status = "Bulking (Surplus Kalori)"
    elif surplus_defisit < 0:
        status = "Diet (Defisit Kalori)"
    else:
        status = "Netral (Kalori Seimbang)"
    
    # Output hasil
    st.write("### Hasil Pemantauan")
    st.write(f"**Kalori Masuk:** {kalori_masuk} kcal")
    st.write(f"**Kalori Dibakar:** {kalori_bakar} kcal")
    st.write(f"**Surplus/Defisit Kalori:** {surplus_defisit} kcal")
    st.write(f"**Status:** {status}")
else:
    st.write("Masukkan data pada sidebar untuk melihat hasil.")

# Grafik tren kalori (opsional)
import matplotlib.pyplot as plt

if kalori_masuk and kalori_bakar:
    labels = ['Kalori Masuk', 'Kalori Dibakar']
    values = [kalori_masuk, kalori_bakar]

    fig, ax = plt.subplots()
    ax.bar(labels, values, color=['blue', 'red'])
    ax.set_title('Perbandingan Kalori')
    ax.set_ylabel('Jumlah Kalori (kcal)')

    st.pyplot(fig)
