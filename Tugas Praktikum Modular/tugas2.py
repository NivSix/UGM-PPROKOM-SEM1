#Mencetak Menu
def menu():
    print('Pilih Bentuk 2D')
    print()
    print('1. Persegi Panjang')
    print('2. Lingkaran')
    print('3. Segitiga')
    print('4. Keluar')

def persegi():
    print('Menghitung Luas Persegi Panjang')
    p = float(input('Masukkan Panjang : '))
    l = float(input('Masukkan Lebar : '))
    luas = p*l
    print('Luas Persegi Panjang adalah ',luas)
    print
    print('Coba lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()

def lingkaran():
    print('Menghitung Luas Lingkaran')
    r = float(input('Masukkan Jari-Jari : '))
    luas = 3.14*(r**2)
    print('Luas Lingkaran adalah ',luas)
    print()
    print('Coba lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()

def segitiga():
    print('Menghitung Luas Segitiga')
    a = float(input('Masukkan Alas : '))
    t = float(input('Masukkan Tinggi : '))
    luas = (a*t)/2
    print('Luas Segitiga adalah ',luas)
    print()
    print('Coba lagi [Y/N]? ')
    back = input().upper()
    if back == 'Y':
        menu()
    else:
        exit()