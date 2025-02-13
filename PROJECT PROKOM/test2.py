barang_belanjaan = []
harga = []
jumlah_barang = []
harga_total = []

while True:
    print("\n====================================================")
    print("=                  Menu Belanja                    =")
    print("====================================================")
    print("= 1. Tambahkan barang belanjaan beserta harganya   =")
    print("= 2. Tampilkan semua barang belanjaan              =")
    print("= 3. Tampilkan jumlah barang belanjaan             =")
    print("= 4. Tampilkan total harga belanjaan               =")
    print("= 5. Keluar                                        =")
    print("====================================================")
    
    pilihan = int(input("Masukkan pilihan: "))
    print("=" * 52)

    if pilihan == 1:
        barang = input("Tambahkan barang belanjaan: ")
        barang_belanjaan.append(barang)
        print("=" * 52)

        harga_barang = float(input(f"Berapa harga {barang}: Rp. "))
        harga.append(harga_barang)
        print("=" * 52)

        banyak_barang = int(input(f"Berapa banyak {barang} yang akan dibeli: "))
        jumlah_barang.append(banyak_barang)
        print("=" * 52)

        total_per_barang = banyak_barang * harga_barang
        harga_total.append(total_per_barang)
       
        print("Barang telah ditambahkan:", barang_belanjaan)
        print("=" * 52)

    elif pilihan == 2:
        if barang_belanjaan:
            print("Semua barang belanjaan:", barang_belanjaan)
            print("=" * 52)
        else:
            print("Barang belanjaan belum ditambahkan.")
            print("=" * 52)


    elif pilihan == 3:
        if barang_belanjaan:
            print("Jumlah barang belanjaan:", len(barang_belanjaan))
            print("=" * 52)
        else:
            print("Barang belanjaan belum ditambahkan.")
            print("=" * 52)

    elif pilihan == 4:
        if harga_total:
            total_harga_semua = sum(harga_total)
            print("Total harga semua barang belanjaan: Rp. ",round(total_harga_semua))
            print("=" * 52)
        else:
            print("Barang belanjaan belum ditambahkan.")
            print("=" * 52)

    elif pilihan == 5:
        print("Terima kasih telah berbelanja!")
        print("=" * 52)
        break
    
    else:
        print("PILIHAN TIDAK VALID!")
        print("=" * 52)
