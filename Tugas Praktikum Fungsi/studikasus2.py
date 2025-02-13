
# Nama: MUSA ADI WIBOWO
# NIM: 24/534704/SV/24082

import math

def penjumlahan(a, b):
    return a + b

def pengurangan(a, b):
    return a - b

def perkalian(a, b):
    return a * b

def pembagian(a, b):
    if b != 0:
        return a / b
    else:
        return "Tidak bisa membagi dengan nol"

def perpangkatan(a, b):
    return a ** b

def akar_kuadrat(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Tidak bisa mencari akar kuadrat dari bilangan negatif"

def tampilkan_menu():
    print("\n===== KALKULATOR MATEMATIKA =====")
    print("Nama: Musa Adi Wibowo           =")
    print("NIM: 24/534704/SV/24082         =")
    print("Menu:                           =")
    print("1. Penjumlahan                  =")
    print("2. Pengurangan                  =")
    print("3. Perkalian                    =")
    print("4. Pembagian                    =")
    print("5. Perpangkatan                 =")
    print("6. Akar Kuadrat                 =")
    print("7. Keluar                       =")
    print("=================================")

while True:
    tampilkan_menu()
    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print("Hasil penjumlahan: ", penjumlahan(a, b))

    elif pilihan == 2:
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print("Hasil pengurangan: ", pengurangan(a, b))

    elif pilihan == 3:
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print("Hasil perkalian: ", perkalian(a, b))

    elif pilihan == 4:
        a = float(input("Masukkan bilangan pertama: "))
        b = float(input("Masukkan bilangan kedua: "))
        print("Hasil pembagian: ", pembagian(a, b))

    elif pilihan == 5:
        a = float(input("Masukkan bilangan: "))
        b = float(input("Masukkan pangkat: "))
        print("Hasil perpangkatan: ", perpangkatan(a, b))

    elif pilihan == 6:
        a = float(input("Masukkan bilangan: "))
        print("Hasil akar kuadrat: ", akar_kuadrat(a))

    elif pilihan == 7:
        print("Terima kasih telah menggunakan kalkulator ini!")
        break

    else:
        print("Pilihan tidak valid, silakan coba lagi.")