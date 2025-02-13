barang_belanjaan = []
harga = []
jumlah_barang = []
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
        barang = input("Tambahkan barang belanjaan: ")
        barang_belanjaan.append(barang)

        harga_barang = float(input(f'Berapa harga {barang}: Rp. '))
        harga.append(harga_barang)

        banyak_barang = int(input(f'Berapa banyak {barang} yang akan dibeli: '))
        jumlah_barang.append(banyak_barang)

        total_per_barang = banyak_barang * harga_barang
        harga_total.append(total_per_barang)

        print("Barang telah ditambahkan:", barang_belanjaan)

    elif pilihan == 2:
        if barang_belanjaan:
            print("Semua barang belanjaan:", barang_belanjaan)
        else:
            print("Barang belanjaan belum ditambahkan.")

    elif pilihan == 3:
        if barang_belanjaan:
            print("Jumlah barang belanjaan:", len(barang_belanjaan))
        else:
            print("Barang belanjaan belum ditambahkan.")

    elif pilihan == 4:
        if harga_total:
            total_harga_semua = sum(harga_total)
            print("Total harga semua barang belanjaan: Rp.", round(total_harga_semua))
        else:
            print("Barang belanjaan belum ditambahkan.")

    elif pilihan == 5:
        print("Terima kasih telah berbelanja!")
        break
    
    else:
        print("Pilihan tidak valid.")
