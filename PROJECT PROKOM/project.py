barang_belanjaan = []
harga = []
harga_total = []

while True:
    print("\nMenu:")
    print("1. Tambahkan barang belanjaan beserta harganya")
    print("2. Tampilkan semua barang belanjaan")
    print("3. Tampilkan jumlah barang belanjaan")
    print("4. Tampilkan total harga belanjaan")
    print("5. Keluar")
    pilihan = int(input("Masukkan pilihan: "))

    if pilihan == 1:
        barang = (input("Tambahkan barang belanjaan: "))
        barang_belanjaan.append(barang)
        print("Barang telah ditambahkan:", barang_belanjaan)
        harga = float(input(f'Berapa harga {barang}: '))
        banyak_barang = int(input(f'Berapa banyak {barang_belanjaan} yang akan dibeli '))
        harga_total = banyak_barang * harga
        print(f'Total harga {barang_belanjaan}', int(harga_total))

    elif pilihan == 2:
        if barang_belanjaan:
            print("Semua barang belanjaan:", barang_belanjaan)
        else:
            print("Barang belanjaan belum di tambahkan")

    elif pilihan == 3:
        if barang_belanjaan:
            print("Jumlah barang belanjaan:", len(barang_belanjaan)) 
        else:    
            print("Data nilai mahasiswa masih kosong")
    
    elif pilihan == 4:
        if harga_total:
            total_harga = sum(harga_total)
            print('Total harga semua barang belanjaan: Rp', total_harga)

    elif pilihan == 5:
        break
    
    else:
        print("Pilihan tidak valid")