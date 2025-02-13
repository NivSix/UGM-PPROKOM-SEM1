# Daftar barang
daftar_barang = {
    "1": ["Bayam", 5000],
    "2": ["Terong", 4500],
    "3": ["Kubis", 6000],
    "4": ["Labu", 7000],
    "5": ["Brokoli", 8000]
}

# Fungsi untuk mencetak daftar barang
def cetak_daftar_barang():
    print("=" * 40)
    print("SELAMAT DATANG DI KASIR")
    print("=" * 40)
    print("Kode | Nama Barang | Harga")
    print("=" * 40)
    for kode, (nama, harga) in daftar_barang.items():
        print(f"{kode}    | {nama:<10} | {harga}")
    print("=" * 40)

# Fungsi untuk menghitung diskon
def hitung_diskon(total):
    if total > 100000:
        return 0.20
    elif total > 50000:
        return 0.15
    elif total > 20000:
        return 0.10
    return 0

# Fungsi untuk menjalankan kasir
def kasir():
    cetak_daftar_barang()
    total = 0
    jenis_barang = int(input("Berapa jenis barang yang akan dibeli? "))

    for _ in range(jenis_barang):
        kode = input("Masukkan kode barang: ")
        while kode not in daftar_barang:
            print("Kode barang tidak valid, silakan masukkan ulang.")
            kode = input("Masukkan kode barang: ")
        jumlah = int(input(f"Berapa banyak {daftar_barang[kode][0]} yang akan dibeli? "))
        total += daftar_barang[kode][1] * jumlah

    diskon = hitung_diskon(total)
    total_diskon = total * diskon
    total_bayar = total - total_diskon

    print("\n======== STRUK BELANJA ========")
    print(f"Total harga: Rp {total}")
    print(f"Diskon {int(diskon*100)}%: Rp {total_diskon}")
    print(f"Total yang harus dibayar: Rp {total_bayar}")
    print("Terima kasih telah berbelanja!")

# Menjalankan program
kasir()