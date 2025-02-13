# Mendeklarasikan list untuk menyimpan 5 angka
angka_list = []

# Meminta pengguna memasukkan angka sebanyak 5 kali
for i in range(1, 6):
    angka = float(input(f"Masukkan angka ke-{i} : "))
    angka_list.append(angka)
    print(angka_list)

# Menghitung jumlah total data yang telah dimasukkan
jumlah_total = sum(angka_list)

# Memberikan opsi kepada pengguna
pilihan = input("ingin melihat hasil jumlah atau rata-rata : ").lower()

if pilihan == "jumlah":
    print(f"Jumlah dari nilai datanya adalah : {jumlah_total}")
elif pilihan == "rata-rata":
    rata_rata = jumlah_total / len(angka_list)
    print(f"rata-rata dari nilai datanya adalah : {rata_rata:.2f}")
else:
    print('Pilihan tidak valid. Harap tuliskan "jumlah" atau "rata-rata".')