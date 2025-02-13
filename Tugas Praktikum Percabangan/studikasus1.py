# Program untuk menentukan jenis segitiga berdasarkan tiga sisi

# Masukkan panjang tiga sisi
sisi1 = float(input('Masukkan panjang sisi pertama: '))
sisi2 = float(input('Masukkan panjang sisi kedua: '))
sisi3 = float(input('Masukkan panjang sisi ketiga: '))

# Fungsi untuk menentukan jenis segitiga
if sisi1 == sisi2 == sisi3:
    print('Segitiga sama sisi')
elif sisi1 == sisi2 or sisi1 == sisi3 or sisi2 == sisi3:
    print('Segitiga sama kaki')
else:
    print('Segitiga sembarang')