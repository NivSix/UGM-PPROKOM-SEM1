import tugas2
while True:
    tugas2.menu()
    pilihan = input('Masukkan pilihan Anda: ')
    if pilihan == '1':
        tugas2.persegi()
    elif pilihan == '2':
        tugas2.lingkaran()
    elif pilihan == '3':    
        tugas2.segitiga()
    elif pilihan == '4':
        exit()
        break
    else:
        print('Pilihan Anda tidak valid!')