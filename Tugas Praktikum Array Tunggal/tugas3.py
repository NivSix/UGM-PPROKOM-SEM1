# Fungsi untuk memeriksa apakah suatu bilangan adalah bilangan prima
def is_prima(angka):
    if angka < 2:
        return False
    for i in range(2, int(angka ** 0.5) + 1):
        if angka % i == 0:
            return False
    return True

# Array input
array = [4, 5, 11, 12, 14, 16, 16, 19]

# Mencari bilangan prima dalam array
prima_list = [angka for angka in array if is_prima(angka)]

# Mengembalikan array bilangan prima dan jumlah bilangan prima
print("Bilangan prima dalam array:", prima_list)
print("Jumlah bilangan prima:", len(prima_list))