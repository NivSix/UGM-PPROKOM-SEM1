# Memanggil modul dari fitur Analisis Udara
import udara 

# Fungsi untuk memanggil fitur Analisis Udara
def menu_udara():
    city = input("Masukkan nama kota: ").upper()

    # Cek apakah kota ada di daftar
    if city in udara.kota_provinsi:
        state = udara.kota_provinsi[city]
        while True:
            udara.data_kota(city, state)
    else:
        print("Maaf, data untuk kota tersebut belum tersedia.")