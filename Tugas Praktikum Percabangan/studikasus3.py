# Program untuk memeriksa apakah suatu karakter adalah huruf besar, huruf kecil, atau bukan huruf

# Input karakter dari pengguna
karakter = input("Masukkan satu karakter: ")

# Memeriksa apakah karakter merupakan huruf besar
if len(karakter)==1:
    if karakter.isupper():
        print(karakter, "adalah huruf besar.")
# Memeriksa apakah karakter merupakan huruf kecil
    elif karakter.islower():
        print(karakter, "adalah huruf kecil.")
# Memeriksa apakah karakter bukan huruf (simbol atau angka)
    elif not karakter.isalpha():
        print(karakter, "bukan huruf.")
# Kasus lainnya (untuk input lebih dari satu karakter)
else:
    print("Anda memasukkan lebih dari satu karakter! \nTolong masukkan satu karakter saja!")