# Inisialisasi matriks 2x3 dengan nilai kosong
matriks = [[0 for j in range(3)] for i in range(2)]

# Meminta input dari pengguna untuk mengisi elemen matriks
for i in range(2):
    for j in range(3):
        print("Masukkan nilai ke-[", i, "][", j, "]", sep="")
        matriks[i][j] = int(input())

# Menampilkan matriks asli
print("\nMatriks Asli:")
for i in range(2):
    for j in range(3):
        print(matriks[i][j], end=" ")
    print()

# Inisialisasi matriks transpose 3x2
transpose = [[0 for i in range(2)] for j in range(3)]

# Proses transpose matriks (menggunakan nested loop)
for i in range(2):
    for j in range(3):
        transpose[j][i] = matriks[i][j]

# Menampilkan matriks hasil transpose
print("\nMatriks Transpose:")
for i in range(3):
    for j in range(2):
        print(transpose[i][j], end=" ")
    print()
