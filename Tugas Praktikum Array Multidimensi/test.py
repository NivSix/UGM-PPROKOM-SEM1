# Inisialisasi matriks 2x3 dengan nilai kosong
matriks = [[0 for k in range(3)] for b in range(2)]

# Meminta input dari pengguna untuk mengisi elemen matriks
for b in range(2):
    for k in range(3):
        print("Masukkan nilai ke-[", b, "][", k, "]", sep="")
        matriks[b][k] = int(input())

# Menampilkan matriks
print("-" * 20)
for b in range(2):
    for k in range(3):
        print(matriks[b][k], end=" ")
    print()