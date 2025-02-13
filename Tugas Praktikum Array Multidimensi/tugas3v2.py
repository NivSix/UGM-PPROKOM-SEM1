# Inisialisasi matriks 2x3 dengan nilai kosong
matriks = [[0 for k in range(3)] for b in range(2)]

# Meminta input dari pengguna untuk mengisi elemen matriks
for b in range(2):
    for k in range(3):
        matriks[b][k] = int(input(f"Masukkan nilai ke-[{b}][{k}] "))
        if k == 2:
            print("-" * 20)

# Menampilkan matriks asli
print("Matriks Asli:")
for b in range(2):
    for k in range(3):
        print(matriks[b][k], end=" ")
    print()

# Inisialisasi matriks transpose 3x2
transpose = [[0 for b in range(2)] for k in range(3)]

# Proses transpose matriks (menggunakan nested loop)
for b in range(2):
    for k in range(3):
        transpose[k][b] = matriks[b][k]

# Menampilkan matriks hasil transpose
print("Matriks Transpose:")
for b in range(3):
    for k in range(2):
        print(transpose[b][k], end=" ")
    print()
