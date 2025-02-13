# Mendeklarasikan list untuk menyimpan 5 angka
angka_list = []

# Meminta pengguna memasukkan angka sebanyak 5 kali
for i in range(1, 6):
    angka = float(input("Masukkan angka ke-" + str(i) + " : "))
    angka_list.append(angka)
    print(angka_list)

# Menghitung jumlah total data yang telah dimasukkan
jumlah_total = sum(angka_list)

# Memberikan opsi kepada pengguna
pilihan = input("Anda ingin melihat hasil jumlah atau rata-rata? : ").lower()

if pilihan == "jumlah":
    print("Jumlah dari nilai datanya adalah : ", jumlah_total)
elif pilihan == "rata-rata":
    rata_rata = jumlah_total / len(angka_list)
    print("rata-rata dari nilai datanya adalah : ", round(rata_rata, 2))
else:
    print('Pilihan tidak valid. Tolong tuliskan "jumlah" atau "rata-rata".')