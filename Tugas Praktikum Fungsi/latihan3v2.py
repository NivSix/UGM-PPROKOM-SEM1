buku = []  # Variabel global untuk menyimpan data Buku

def show_data():  # Fungsi untuk menampilkan semua data
    if len(buku) <= 0:
        print("BELUM ADA DATA")
    else:
        for indeks in range(len(buku)):
            print("[%d] %s" % (indeks, buku[indeks]))

def insert_data():  # Fungsi untuk menambah data
    buku_baru = input("Judul Buku: ")
    buku.append(buku_baru)
    print("Data berhasil ditambahkan!")

def edit_data():  # Fungsi untuk edit data
    show_data()
    try:
        indeks = int(input("Inputkan ID buku: "))
        if indeks < 0 or indeks >= len(buku):
            print("ID salah")
        else:
            judul_baru = input("Judul baru: ")
            buku[indeks] = judul_baru
            print("Data berhasil diubah!")
    except ValueError:
        print("ID harus berupa angka.")

def delete_data():  # Fungsi untuk menghapus data
    show_data()
    try:
        indeks = int(input("Inputkan ID buku: "))
        if indeks < 0 or indeks >= len(buku):
            print("ID salah")
        else:
            buku.pop(indeks)
            print("Data berhasil dihapus!")
    except ValueError:
        print("ID harus berupa angka.")

def show_menu():  # Fungsi untuk menampilkan menu
    print("\n")
    print("----------- MENU ----------")
    print("[1] Show Data")
    print("[2] Insert Data")
    print("[3] Edit Data")
    print("[4] Delete Data")
    print("[5] Exit")
    try:
        menu = int(input("PILIH MENU> "))
        print("\n")
        if menu == 1:
            show_data()
        elif menu == 2:
            insert_data()
        elif menu == 3:
            edit_data()
        elif menu == 4:
            delete_data()
        elif menu == 5:
            exit()
        else:
            print("Salah pilih!")
    except ValueError:
        print("Pilihan harus berupa angka.")

if __name__ == "__main__":
    while True:
        show_menu()
