# PROGRAM 2 Analisis Air
import os # Memanggil modul OS
import time # Memanggil modul Time

def analisis_air():
    print("Analisis Kualitas Air Minum")
    print("=" * 90) # Pembatas

    # Input data kualitas air dengan validasi
    # Input data warna
    warna = ""
    while warna not in ["jernih", "kuning", "hijau", "biru", "merah", "hitam", "warna lain"]:
        warna = input("Masukkan warna air (jernih, kuning, hijau, biru, merah, hitam, warna lain): ").lower()
        if warna not in ["jernih", "kuning", "hijau", "biru", "merah", "hitam", "warna lain",]:
            print("Input salah. Masukkan warna yang valid.")
            print("=" * 90)

    # Input data bau
    bau = ""
    while bau not in ["ya", "tidak"]:
        print("=" * 90)
        bau = input("Apakah air berbau? (ya/tidak): ").lower()
        if bau not in ["ya", "tidak"]:
            print("Input salah. Masukkan 'ya' atau 'tidak'.")

    # Input data pH
    ph = -1
    while ph < 0 or ph > 14:
        try:
            print("=" * 90)
            ph = float(input("Masukkan nilai pH air (0-14): "))
            if ph < 0 or ph > 14:
                print("Input salah. Masukkan nilai pH antara 0 dan 14.")
        except ValueError:
            print("Input salah. Masukkan nilai numerik untuk pH.")

    # Analisis berdasarkan warna
    aman_warna = warna == "jernih"
    # Analisis berdasarkan bau
    aman_bau = bau == "tidak"
    # Analisis berdasarkan pH
    aman_ph = 6.5 <= ph <= 8.5

    # Menentukan hasil analisis
    print("=" * 90)
    if aman_warna and aman_bau and aman_ph:
        print("AIR AMAN UNTUK DIKONSUMSI!")
        print("=" * 90)
        print("Semua kriteria aman terpenuhi: warna jernih, tidak berbau, dan pH normal.")
        print("=" * 90)
    else:
        print("- AIR TIDAK AMAN UNTUK DIKONSUMSI!")
        
        # Menilai tingkat kontaminasi dan memberikan alasan spesifik kontaminasi
        tingkat_kontaminasi = 0
        alasan_kontaminasi = []

        # Alasan kontaminasi warna
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
        
        # Alasan kontaminasi bau
        if not aman_bau:
            tingkat_kontaminasi += 1
            alasan_kontaminasi.append("Air memiliki bau yang tidak sedap, bisa jadi ada kontaminan organik atau zat kimia.")
        
        # Alasan kontaminasi pH
        if not aman_ph:
            tingkat_kontaminasi += 1
            if ph < 6.5:
                alasan_kontaminasi.append(f"pH air ({ph}) terlalu rendah, air bersifat asam dan bisa merusak saluran pencernaan.")
            elif ph > 8.5:
                alasan_kontaminasi.append(f"pH air ({ph}) terlalu tinggi, air bersifat basa dan bisa menimbulkan efek negatif.")

        # Menampilkan tingkat kontaminasi
        print("=" * 90)
        if tingkat_kontaminasi == 1:
            print("- Tingkat kontaminasi: RENDAH!")
        elif tingkat_kontaminasi == 2:
            print("- Tingkat kontaminasi: SEDANG!")
        elif tingkat_kontaminasi == 3:
            print("- Tingkat kontaminasi: TINGGI!")
        print("=" * 90)

        # Menampilkan alasan mengapa air tidak aman
        print("Alasan air kurang atau tidak layak konsumsi:")
        for alasan in alasan_kontaminasi:
            print("- " + alasan)
        print("=" * 90)
        print("!PENTING!------------KRITERIA AIR YANG BAIK UNTUK DIKONSUMSI ADALAH-----------------------\n-----------------------AIR YANG TIDAK BERWARNA, BERBAU, DAN BERASA---------------!PENTING!")
        print("=" * 90)

    # Fungsi untuk kembali ke menu
    kembali = input("ENTER untuk kembali ke menu!").lower
    if kembali == True:
        print()
    time.sleep(0.5)
    os.system("cls")