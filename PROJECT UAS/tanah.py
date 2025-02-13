# PROGRAM 1 Analisis Tanah
import os # Memanggil modul OS
import time # Memanggil modul Time
def analisis_tanah():
    print("Analisis Kesuburan Tanah")
    print("=" * 90)
    def tanya_ya_tidak(pertanyaan):
        # Fungsi untuk memastikan input pengguna hanya menerima 'ya' atau 'tidak'
        while True:
            jawaban = input(pertanyaan + " (ya/tidak): ").strip().lower()
            if jawaban in ["ya", "tidak"]:
                print("=" * 90)
                return jawaban
            else:
                print("Input salah. Harap masukkan 'ya' atau 'tidak'.")
                print("=" * 90)

    def cek_kesuburan_tanah():
        # Input dari pengguna untuk setiap karakteristik tanah dengan validasi
        warna = tanya_ya_tidak("Apakah warna tanah gelap?")
        tekstur = tanya_ya_tidak("Apakah tekstur tanah gembur?")
        kelembaban = tanya_ya_tidak("Apakah tanah lembab?")
    
        # Validasi untuk pH agar tetap berada dalam rentang 0 - 14
        while True:
            try:
                pH = float(input("Berapa pH tanah? (0-14): "))
                if 0 <= pH <= 14:
                    print("=" * 90)
                    break
                else:
                    print("Input salah. Harap masukkan angka antara 0 dan 14.")
                    print("=" * 90)
            except ValueError:
                print("Input salah. Harap masukkan angka antara 0 dan 14.")
                print("=" * 90)
               
        # Kriteria kesuburan tanah
        kriteria_kesuburan_tanah = [
            warna == "ya",
            tekstur == "ya",
            kelembaban == "ya",
            6.0 <= pH <= 7.5,
        ]
    
        # Menyimpan rekomendasi jika ada kriteria yang tidak terpenuhi
        rekomendasi_solusi = []
        # Menentukan rekomendasi yang akan menjadi output
        if warna != "ya":
            rekomendasi_solusi.append("Tambahkan kompos atau bahan organik untuk meningkatkan kandungan humus sehingga warna \n  tanah menjadi lebih gelap.")
        
        if tekstur != "ya":
            rekomendasi_solusi.append("Tambahkan bahan organik seperti serbuk gergaji, pupuk kandang dan kompos untuk \n  memperbaiki tekstur tanah agar lebih gembur.")
        
        if kelembaban != "ya":
            rekomendasi_solusi.append("Perbaiki kadar air pada tanah dengan menambahkan bahan organik, atau lakukan penyiraman \n  secara rutin untuk menjaga kelembaban.")
        
        if not (6.0 <= pH <= 7.5):
            if pH < 6.0:
                rekomendasi_solusi.append("pH tanah terlalu asam. Tambahkan kapur pertanian (dolomit) untuk menetralkan pH.")
            else:
                rekomendasi_solusi.append("pH tanah terlalu basa. Tambahkan sulfur atau pupuk asam untuk menurunkan pH.")

        # Menentukan hasil kesuburan tanah dan memberikan output
        if all(kriteria_kesuburan_tanah):
            print("Tanah ini sangat subur! Cocok untuk pertumbuhan tanaman.")

        elif len(rekomendasi_solusi) <= 2:
            print("Tanah ini cukup subur, tetapi ada beberapa hal yang dapat ditingkatkan:")
            for rekomendasi in rekomendasi_solusi:
                print(f"- {rekomendasi}")
        else:
            print("Tanah ini kurang subur. Berikut beberapa rekomendasi untuk memperbaiki kesuburan tanah:")
            for rekomendasi in rekomendasi_solusi:
                print(f"- {rekomendasi}")
        print("=" * 90)

    # Memanggil fungsi untuk cek kesuburan tanah
    cek_kesuburan_tanah()

    # Fungsi untuk kembali ke menu
    kembali = input("ENTER untuk kembali ke menu!").lower
    if kembali == True:
        print()
    time.sleep(0.5)
    os.system("cls")