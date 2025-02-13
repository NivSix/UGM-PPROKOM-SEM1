# Program Persyaratan SIM
umur = int(input("Masukan Umur Anda = "))
nilai = int(input("Masukan Nilai Tes Anda = "))

lulus = "Selamat! Anda Berhak Mendapatkan SIM."
gagal = "Maaf, Anda tidak berhak mendapatkan SIM.\nSilakan coba lagi bulan atau tahun depan."

# Cek apakah umur lebih dari 17 tahun
if umur >= 17:
    # Cek apakah nilai tes memenuhi syarat (>=60)
    if nilai >= 60:
        print(lulus)
    else:
        print(gagal)
else:
    print(gagal)
