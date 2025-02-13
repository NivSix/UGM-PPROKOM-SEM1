import random

# Fungsi untuk menentukan pemenang
def tentukan_pemenang(pengguna, komputer):
    if pengguna == komputer:
        return "Seri!"
    elif (pengguna == "batu" and komputer == "gunting") or \
         (pengguna == "gunting" and komputer == "kertas") or \
         (pengguna == "kertas" and komputer == "batu"):
        return "Anda Menang!"
    else:
        return "Komputer Menang!"

# Daftar pilihan yang valid
pilihan = ["batu", "kertas", "gunting"]

# Input pilihan pengguna
pengguna = input("Pilih batu, kertas, atau gunting: ").lower()

# Pilihan acak komputer
komputer = random.choice(pilihan)

# Menampilkan pilihan komputer
print(f"Komputer memilih: {komputer}")

# Tentukan dan tampilkan hasil
hasil = tentukan_pemenang(pengguna, komputer)
print(hasil)
