# Daftar angka yang diberikan
array = [1, 5, 4, 6, 7, 12, 45, 9, 99, 55, 100, 88, 75, 60]

# Memisahkan angka genap dan ganjil menggunakan list comprehension
genap = [angka for angka in array if angka % 2 == 0]
ganjil = [angka for angka in array if angka % 2 != 0]

# Menampilkan hasil pemisahan
print(array)

# Menampilkan angka genap dan jumlahnya
print("Ini adalah angka genap :", genap)
print("Jumlah angka genap     :", len(genap), "angka")

# Menampilkan angka ganjil dan jumlahnya
print("Ini adalah angka ganjil:", ganjil)
print("Jumlah angka ganjil    :", len(ganjil), "angka")