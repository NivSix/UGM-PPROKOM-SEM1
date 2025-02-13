# Program untuk menampilkan siswa yang lulus atau tidak lulus berdasarkan nilai

# Jumlah data siswa
jumlah_siswa = 5

# Loop untuk meminta input data setiap siswa
for i in range(jumlah_siswa):
    # Input nama siswa
    nama = input(f"Masukkan nama siswa ke-{i+1}: ")
    
    # Input nilai siswa
    nilai = int(input(f"Masukkan nilai {nama}: "))
    
    # Menentukan status kelulusan
    if nilai >= 70:
        print(f"{nama} Lulus.")
    else:
        print(f"{nama} Tidak Lulus.")
    
    print()  
    
print("Proses penilaian selesai.")