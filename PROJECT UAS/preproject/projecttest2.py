def tampilkan_menu():
    print("\n==========================================================================================")
    print("=                            Menu Analisis TIGA ELEMEN DASAR                             =")
    print("==========================================================================================")
    print("= 1. Analisis Kesuburan Tanah                                                            =")
    print("= 2. Analisis Kelayakan Air                                                              =")
    print("= 3. Analisis Kelayakan Angin                                                            =")
    print("= 4. Keluar                                                                              =")
    print("==========================================================================================")

def analisis_tanah():
    print("Analisis Kesuburan Tanah")
    print("=" * 90)
    def tanya_ya_tidak(pertanyaan):
        # Fungsi untuk memastikan input pengguna hanya menerima 'ya' atau 'tidak'
        while True:
            jawaban = input(pertanyaan + " (ya/tidak): ").strip().lower()
            print("=" * 90)
            if jawaban in ["ya", "tidak"]:
                return jawaban
            else:
                print("Input salah. Harap masukkan 'ya' atau 'tidak'.")
           

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
                    break
                else:
                    print("Input salah. Harap masukkan angka antara 0 dan 14.")
                    print("=" * 90)
            except ValueError:
                print("Input salah. Harap masukkan angka antara 0 dan 14.")
                print("=" * 90)
               
        # Kriteria kesuburan
        kriteria_kesuburan_tanah = [
            warna == "ya",
            tekstur == "ya",
            kelembaban == "ya",
            6.0 <= pH <= 7.5,
        ]
    
        # Menyimpan rekomendasi jika ada kriteria yang tidak terpenuhi
        rekomendasi_solusi = []
    
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
            print("\nTanah ini sangat subur! Cocok untuk pertumbuhan tanaman.")
            print("=" * 90)
        elif len(rekomendasi_solusi) <= 2:
            print("\nTanah ini cukup subur, tetapi ada beberapa hal yang dapat ditingkatkan:")
            for rekomendasi in rekomendasi_solusi:
                print(f"- {rekomendasi}")
        else:
            print("\nTanah ini kurang subur. Berikut beberapa rekomendasi untuk memperbaiki kesuburan tanah:")
            for rekomendasi in rekomendasi_solusi:
                print(f"- {rekomendasi}")
        print("=" * 90)
    
    # Memanggil fungsi untuk cek kesuburan tanah
    cek_kesuburan_tanah()

# PROGRAM 2
def analisis_air():
    print("Analisis Kualitas Air Minum")
    print("=" * 90)

    # Input data kualitas air dengan validasi
    warna = ""
    while warna not in ["jernih", "kuning", "hijau", "biru", "merah", "hitam", "warna lain"]:
        warna = input("Masukkan warna air (jernih, kuning, hijau, biru, merah, hitam, warna lain): ").lower()
        print("=" * 90)
        if warna not in ["jernih", "kuning", "hijau", "biru", "merah", "hitam", "warna lain",]:
            print("Input salah. Masukkan warna yang valid.")
            print("=" * 90)

    bau = ""
    while bau not in ["ya", "tidak"]:
        bau = input("Apakah air berbau? (ya/tidak): ").lower()
        print("=" * 90)
        if bau not in ["ya", "tidak"]:
            print("Input salah. Masukkan 'ya' atau 'tidak'.")
            print("=" * 90)

    ph = -1
    while ph < 0 or ph > 14:
        try:
            ph = float(input("Masukkan nilai pH air (0-14): "))
            if ph < 0 or ph > 14:
                print("Input salah. Masukkan nilai pH antara 0 dan 14.")
                print("=" * 90)
        except ValueError:
            print("Input salah. Masukkan nilai numerik untuk pH.")
            print("=" * 90)

    # Analisis berdasarkan warna
    aman_warna = warna == "jernih"

    # Analisis berdasarkan bau
    aman_bau = bau == "tidak"

    # Analisis berdasarkan pH
    aman_ph = 6.5 <= ph <= 8.5

    # Menentukan hasil analisis
    if aman_warna and aman_bau and aman_ph:
        print("\nAir aman untuk dikonsumsi.")
        print("Semua kriteria aman terpenuhi: warna jernih, tidak berbau, dan pH normal.")
    else:
        print("\nAir tidak aman untuk dikonsumsi.")
        
        # Menilai tingkat kontaminasi dan memberikan alasan spesifik
        tingkat_kontaminasi = 0
        alasan_kontaminasi = []

        if not aman_warna:
            tingkat_kontaminasi += 1
            if warna == "kuning":
                alasan_kontaminasi.append("Air berwarna kuning, kemungkinan karena zat besi atau bahan organik.")
            elif warna == "hijau":
                alasan_kontaminasi.append("Air berwarna hijau, mungkin mengandung alga atau kontaminasi biologis.")
            elif warna == "biru":
                alasan_kontaminasi.append("Air berwarna biru, bisa jadi mengandung tembaga atau logam berat lainnya.")
            elif warna == "merah":
                alasan_kontaminasi.append("Air berwarna merah, mungkin ada zat besi tinggi atau bakteri tertentu.")
            elif warna == "hitam":
                alasan_kontaminasi.append("Air berwarna hitam, ini menunjukkan kemungkinan kontaminasi berat atau terdapat bahan \n  organik yang terurai.")
            elif warna == "warna lain":
                alasan_kontaminasi.append("Jika air berwarna selain dari menu yang disediakan, ini menujunkan kemungkinan kontaminasi dari bahan-bahan lain")
        if not aman_bau:
            tingkat_kontaminasi += 1
            alasan_kontaminasi.append("Air memiliki bau yang tidak sedap, bisa jadi ada kontaminan organik atau zat kimia.")

        if not aman_ph:
            tingkat_kontaminasi += 1
            if ph < 6.5:
                alasan_kontaminasi.append(f"pH air ({ph}) terlalu rendah, air bersifat asam dan bisa merusak saluran pencernaan.")
            elif ph > 8.5:
                alasan_kontaminasi.append(f"pH air ({ph}) terlalu tinggi, air bersifat basa dan bisa menimbulkan efek negatif.")

        # Menampilkan tingkat kontaminasi
        if tingkat_kontaminasi == 1:
            print("Tingkat kontaminasi: Rendah")
        elif tingkat_kontaminasi == 2:
            print("Tingkat kontaminasi: Sedang")
        elif tingkat_kontaminasi == 3:
            print("Tingkat kontaminasi: Tinggi")

        # Menampilkan alasan mengapa air tidak aman
        print("\nAlasan air kurang atau tidak layak konsumsi:")
        for alasan in alasan_kontaminasi:
            print("- " + alasan)
        print("\n!PENTING!------------KRITERIA AIR YANG BAIK UNTUK DIKONSUMSI ADALAH--------------- \n--------------AIR YANG TIDAK BERWARNA, BERBAU, DAN BERASA---------------!PENTING!")

while True:
    tampilkan_menu()
    try:
        pilihan = int(input("Masukkan pilihan: "))
    except ValueError:
        print("PILIHAN TIDAK VALID! Masukkan angka antara 1-3.")
        print("=" *90)
        continue  # Kembali ke awal pengulangan jika pilihan pengguna salah.

    print("=" * 90)

    if pilihan == 1:
        analisis_tanah()
    elif pilihan == 2:
        analisis_air()
    elif pilihan == 4:
        print("Terima kasih telah menggunakan Menu Analisis TIGA ELEMEN DASAR!")
        print("=" * 90)
        break
    else:
        print("PILIHAN TIDAK VALID! Masukkan angka antara 1-3.")
        print("=" * 90)