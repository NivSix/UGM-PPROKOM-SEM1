# Deklarasi variabel daftar barang dan harga dalam bentuk list.
barang_belanjaan = []
harga = []
harga_total = []

# Program untuk menampilkan menu.
def tampilkan_menu():
    print("\n====================================================")
    print("=              Menu Kalkulator Belanja             =")
    print("====================================================")
    print("= 1. Tambahkan barang belanjaan beserta harganya   =")
    print("= 2. Tampilkan semua barang belanjaan              =")
    print("= 3. Tampilkan jumlah barang belanjaan             =")
    print("= 4. Tampilkan total harga belanjaan               =")
    print("= 5. Keluar                                        =")
    print("====================================================")

# Program untuk menambah barang.
def tambah_barang():
    barang = input("Tambahkan barang belanjaan: ")
    barang_belanjaan.append(barang)
    print("=" * 52)

    try:
        harga_barang = float(input(f"Berapa harga {barang}: Rp. "))
        harga.append(harga_barang)
        print("=" * 52)

        banyak_barang = int(input(f"Berapa banyak {barang} yang akan dibeli: "))
        print("=" * 52)

        total_harga_per_barang = banyak_barang * harga_barang
        harga_total.append(total_harga_per_barang)
       
        print("Barang telah ditambahkan:", barang_belanjaan)
        print("=" * 52)
    except ValueError: # Kembali ke awal pengulangan jika pilihan atau angka yang dimasukkan pengguna salah.
        print("INPUT TIDAK VALID! Pastikan memasukkan angka yang benar untuk harga dan jumlah.")
        print("=" * 52)

# Program untuk menampilkan semua barang.
def tampilkan_semua_barang():
    if barang_belanjaan:
        print("Semua barang belanjaan:", barang_belanjaan)
    else:
        print("Barang belanjaan belum ditambahkan.")
    print("=" * 52)

# Program untuk jumlah barang
def tampilkan_jumlah_barang():
    if barang_belanjaan:
        print("Jumlah barang belanjaan:", len(barang_belanjaan))
    else:
        print("Barang belanjaan belum ditambahkan.")
    print("=" * 52)

# Program untuk menampilkan total harga
def tampilkan_total_harga():
    if harga_total:
        total_harga_semua = sum(harga_total)
        print("Total harga semua barang belanjaan: Rp.",round(total_harga_semua))
    else:
        print("Barang belanjaan belum ditambahkan.")
    print("=" * 52)

# Pengulangan program (PROGRAM DIMULAI!)
while True:
    tampilkan_menu()
    try:
        pilihan = int(input("Masukkan pilihan: "))
    except ValueError:
        print("PILIHAN TIDAK VALID! Masukkan angka antara 1-5.")
        print("=" * 52)
        continue  # Kembali ke awal pengulangan jika pilihan pengguna salah.

    print("=" * 52)

    if pilihan == 1:
        tambah_barang()
    elif pilihan == 2:
        tampilkan_semua_barang()
    elif pilihan == 3:
        tampilkan_jumlah_barang()
    elif pilihan == 4:
        tampilkan_total_harga()
    elif pilihan == 5:
        print("Terima kasih telah menggunakan Kalkulator Belanja!")
        print("=" * 52)
        break
    else:
        print("PILIHAN TIDAK VALID! Masukkan angka antara 1-5.")
        print("=" * 52)