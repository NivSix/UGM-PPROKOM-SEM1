# Meminta pengguna untuk menentukan jumlah data
n = int(input("Masukkan jumlah data: "))
# Inisialisasi variabel untuk menyimpan total nilai
total = 0
# Loop untuk meminta input data sebanyak 'n' kali
for i in range(1, n + 1):
    nilai = float(input("Masukkan data ke-" + str(i) + ": "))
    total += nilai

# Menghitung rata-rata
rata_rata = total / n
# Menampilkan hasil rata-rata
print("Rata-rata dari " + str(n) + " data adalah: " + str(rata_rata))