# Menampilkan hasil dengan saran kalori yang harus dibakar
st.header("Saran Kalori yang Harus Dibakar")

# Menentukan kalori yang perlu dibakar
if tujuan_diet == "Menurunkan Berat Badan":
    kalori_bakar = tdee - 500  # Defisit kalori
    st.write(f"Saran kalori yang harus dibakar untuk penurunan berat badan: {int(kalori_bakar)} kalori per hari")
    st.write("Saran aktivitas: Berolahraga dengan intensitas sedang (seperti berjalan cepat atau jogging) selama 30-60 menit per hari.")

elif tujuan_diet == "Menjaga Berat Badan":
    st.write(f"Saran kalori yang harus dibakar untuk menjaga berat badan: {int(tdee)} kalori per hari")
    st.write("Saran aktivitas: Lakukan aktivitas fisik ringan hingga sedang secara teratur (seperti berjalan cepat atau bersepeda).")

elif tujuan_diet == "Menambah Massa Otot":
    kalori_bakar = tdee + 500  # Surplus kalori
    st.write(f"Saran kalori yang harus dibakar untuk menambah massa otot: {int(kalori_bakar)} kalori per hari")
    st.write("Saran aktivitas: Fokus pada latihan kekuatan (strength training) dan makan lebih banyak kalori yang sehat.")
