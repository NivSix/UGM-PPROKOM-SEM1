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
# Fungsi untuk menampilkan simbol batu, kertas, dan gunting
def tampilkan_simbol(pilihan):
    if pilihan == "batu":
        return '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''
    elif pilihan == "kertas":
        return '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''
    elif pilihan == "gunting":
        return '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    else:
        return "Pilihan tidak valid."

# Daftar pilihan yang valid
pilihan = ["batu", "kertas", "gunting"]
# Input pilihan pengguna
pengguna = input("Pilih batu, kertas, atau gunting: ").lower()
# Pilihan acak komputer
komputer = random.choice(pilihan)
# Menampilkan pilihan pengguna dan komputer dengan simbol
print(f"Anda memilih:\n{tampilkan_simbol(pengguna)}")
print(f"Komputer memilih:\n{tampilkan_simbol(komputer)}")
# Tentukan dan tampilkan hasil
hasil = tentukan_pemenang(pengguna, komputer)
print(hasil)