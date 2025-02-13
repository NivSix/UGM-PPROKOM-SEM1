# Memanggil modul dari fitur-fitur utama
import menu_utama # Memanggil modul Menu Utama 
import tanah # Memanggil modul Analisis Udara
import air # Memanggil modul Analisis Air
import udara # Memanggil modul Analisis Udara

# Melakukan pengulangan program dengan validasi
while True:
    menu_utama.tampilkan_menu()
    try:
        pilihan = int(input("Masukkan pilihan: "))
    except ValueError:
        print("PILIHAN TIDAK VALID! Masukkan angka antara 1-3.")
        print("=" *90)
        continue  # Kembali ke awal pengulangan jika pilihan pengguna salah.
  
    # Fungsi untuk memanggil fitu-fitur utama
    if pilihan == 1:
        print("=" * 90)
        tanah.analisis_tanah()  
    elif pilihan == 2:
        print("=" * 90)
        air.analisis_air()
    elif pilihan == 3:
        print("=" * 90)
        udara.analisis_udara()
    elif pilihan == 4:
        print("=" * 90)
        print("Terima kasih telah menggunakan ECO ANALYZER!")
        break
    else:
        print("PILIHAN TIDAK VALID! Masukkan angka antara 1-3.")
        print("=" * 90)