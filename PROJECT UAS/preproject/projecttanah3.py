def tanya_ya_tidak(pertanyaan):
    """Fungsi untuk memastikan input pengguna hanya menerima 'ya' atau 'tidak'."""
    while True:
        jawaban = input(pertanyaan + " (ya/tidak): ").strip().lower()
        if jawaban in ["ya", "tidak"]:
            return jawaban
        else:
            print("Input salah. Harap masukkan 'ya' atau 'tidak'.")

def check_soil_fertility():
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
        except ValueError:
            print("Input salah. Harap masukkan angka antara 0 dan 14.")
    
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
        rekomendasi_solusi.append("Tambahkan kompos atau bahan organik untuk meningkatkan kandungan humus sehingga warna tanah menjadi lebih gelap.")
        
    if tekstur != "ya":
        rekomendasi_solusi.append("Tambahkan bahan organik atau pasir kasar untuk memperbaiki tekstur tanah agar lebih gembur.")
        
    if kelembaban != "ya":
        rekomendasi_solusi.append("Perbaiki retensi air tanah dengan menambahkan bahan organik, atau lakukan penyiraman secara rutin untuk menjaga kelembaban.")
        
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
        for rekomendasi_solusi in rekomendasi_solusi:
            print(f"- {rekomendasi_solusi}")
    else:
        print("Tanah ini kurang subur. Berikut adalah beberapa rekomendasi untuk memperbaiki kesuburan tanah:")
        for rekomendasi_solusi in rekomendasi_solusi:
            print(f"- {rekomendasi_solusi}")

# Menjalankan fungsi analisis tanah
check_soil_fertility()
