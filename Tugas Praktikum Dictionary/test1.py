# Daftar barang (kode: [nama, harga per unit])
daftar_barang = {
    "001": ["Beras", 10000],
    "002": ["Gula", 8000],
    "003": ["Minyak", 15000],
    "004": ["Teh", 5000],
    "005": ["Susu", 12000]
}

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
    keranjang = []
    jenis_barang = int(input("Berapa jenis barang yang ingin dibeli? "))
    
    for _ in range(jenis_barang):
        while True:
            kode = input("Masukkan kode barang: ")
            if kode in daftar_barang:
                break
            else:
                print("Kode barang tidak valid, silakan coba lagi.")
        
        jumlah = int(input(f"Masukkan jumlah {daftar_barang[kode][0]}: "))
        keranjang.append((kode, jumlah))

    total_harga, total_setelah_diskon, diskon = hitung_total_dan_diskon(keranjang)

    print("\n--- Struk Belanja ---")
    for kode, jumlah in keranjang:
        print(f"{daftar_barang[kode][0]} x {jumlah}: Rp{daftar_barang[kode][1] * jumlah}")
    print(f"\nTotal Harga: Rp{total_harga}")
    print(f"Diskon: {diskon}%")
    print(f"Total Setelah Diskon: Rp{total_setelah_diskon}")

# Menjalankan program
proses_pembelian()
