def analisis_air():
    print("Analisis Kualitas Air Minum")
    print("="*30)

    # Input data kualitas air
    warna = input("Masukkan warna air (jernih, kuning, hijau, biru, merah, hitam): ").lower()
    bau = input("Apakah air berbau? (ya/tidak): ").lower()
    ph = float(input("Masukkan nilai pH air (0-14): "))

    # Analisis berdasarkan warna
    if warna == "jernih":
        aman_warna = True
    elif warna in ["kuning", "hijau", "biru", "merah", "hitam"]:
        aman_warna = False
    else:
        print("Warna tidak dikenali, dianggap tidak aman.")
        aman_warna = False

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
            if warna == "kuning" or warna == "coklat":
                alasan_kontaminasi.append("Air berwarna kuning atau cokelat, kemungkinan karena zat besi atau bahan organik.")
            elif warna == "hijau":
                alasan_kontaminasi.append("Air berwarna hijau, mungkin mengandung alga atau kontaminasi biologis.")
            elif warna == "biru":
                alasan_kontaminasi.append("Air berwarna biru, bisa jadi mengandung tembaga atau logam berat lainnya.")
            elif warna == "merah" or warna == "jingga":
                alasan_kontaminasi.append("Air berwarna merah atau jingga, mungkin ada zat besi tinggi atau bakteri tertentu.")
            elif warna == "hitam":
                alasan_kontaminasi.append("Air berwarna hitam, ini menunjukkan kemungkinan kontaminasi berat atau bahan organik yang terurai.")

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
        print("\nAlasan air tidak layak konsumsi:")
        for alasan in alasan_kontaminasi:
            print("- " + alasan)

# Menjalankan program
analisis_air()
