# Meminta pengguna untuk memasukkan jumlah elemen dalam array
jumlah_elemen = int(input("Masukkan jumlah elemen dalam array: "))

# Mengisi array dengan bilangan dari 1 hingga jumlah elemen yang dimasukkan
data_array = list(range(1, jumlah_elemen + 1))

# Menampilkan array yang sudah diisi
print("Data Array:", data_array)

# Meminta pengguna untuk memasukkan bilangan yang digunakan untuk mencari kelipatan
kelipatan = int(input("Masukkan kelipatan yang ingin ditampilkan: "))

# Mencari elemen-elemen yang merupakan kelipatan dari bilangan tersebut
kelipatan_array = [angka for angka in data_array if angka % kelipatan == 0]

# Menampilkan elemen-elemen yang merupakan kelipatan
if kelipatan_array:
    print("Elemen yang merupakan kelipatan dari", kelipatan, ":", kelipatan_array)
else:
    print("Tidak ada elemen yang merupakan kelipatan dari", kelipatan)