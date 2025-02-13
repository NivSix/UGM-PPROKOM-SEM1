# Daftar barang (kode: [nama, harga per unit])
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

# Fungsi untuk menghitung total dan diskon
def hitung_total_dan_diskon(keranjang):
    total_harga = sum([daftar_barang[kode][1] * jumlah for kode, jumlah in keranjang])
    if total_harga > 100000:
        diskon = 0.20
    elif total_harga > 50000:
        diskon = 0.15
    elif total_harga > 20000:
        diskon = 0.10
    else:
        diskon = 0
    total_setelah_diskon = total_harga * (1 - diskon)
    return total_harga, total_setelah_diskon, diskon * 100

# Fungsi utama untuk proses pembelian
def proses_pembelian():
    cetak_daftar_barang()
    keranjang = []
    jenis_barang = int(input("Berapa jenis barang yang akan dibeli? "))
    
    for _ in range(jenis_barang):
        while True:
            kode = input("Masukkan kode barang: ")
            if kode in daftar_barang:
                break
            else:
                print("Kode barang tidak valid, silakan masukkan ulang.")
        
        jumlah = int(input(f"Berapa banyak {daftar_barang[kode][0]} yang akan dibeli? "))
        keranjang.append((kode, jumlah))

    total_harga, total_setelah_diskon, diskon = hitung_total_dan_diskon(keranjang)

    print("\n======== STRUK BELANJA ========")
    for i, (kode, jumlah) in enumerate(keranjang, start=1):
        print(f"Barang {i}: Rp {daftar_barang[kode][1] * jumlah}")
    print(f"\nTotal harga: Rp {total_harga}")
    print(f"Diskon {int(diskon)}%: Rp {total_harga - total_setelah_diskon}")
    print(f"Total yang harus dibayar: Rp {total_setelah_diskon}")
    print("\nTerima kasih telah berbelanja!")

# Menjalankan program
proses_pembelian()
