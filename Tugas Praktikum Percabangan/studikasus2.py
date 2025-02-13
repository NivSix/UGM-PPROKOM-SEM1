# Program untuk memeriksa apakah suatu tahun adalah tahun kabisat atau bukan

# Masukkan tahun dari pengguna
tahun = int(input("Masukkan tahun: "))

# Memeriksa apakah tahun kabisat
if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")