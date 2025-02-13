# PROGRAM 1 Analisis Udara
import requests # Memanggil modul Request
import os # Memanggil modul OS
import time # Memanggil modul Time

def analisis_udara():
    kota_provinsi = {
        "JAKARTA": "Jakarta",
        "SURABAYA": "East Java",
        "BANDUNG": "West Java",
        "YOGYAKARTA": "Yogyakarta",
        "DENPASAR": "Bali",
        "MEDAN": "North Sumatra",
        "MAKASSAR": "South Sulawesi",
        "SEMARANG": "Central Java",
        "MALANG": "East Java",
        "PALEMBANG": "South Sumatra",
        "BALIKPAPAN": "East Kalimantan",
        "BATAM": "Riau Islands",
        "BOGOR": "West Java",
        "PADANG": "West Sumatra",
        "PEKANBARU": "Riau",
        "SAMARINDA": "East Kalimantan",
        "BANJARMASIN": "South Kalimantan",
        "SURAKARTA": "Central Java",
        "MANADO": "North Sulawesi",
        "PONTIANAK": "West Kalimantan"
    }

    def aqi_category(aqi):
        if aqi <= 50:
            return "Baik", "Tidak ada anjuran khusus."
        elif 51 <= aqi <= 100:
            return "Sedang", "Anjuran untuk kelompok sensitif: kurangi aktivitas luar ruangan."
        elif 101 <= aqi <= 150:
            return "Tidak Sehat bagi Kelompok Sensitif", "Kelompok sensitif disarankan mengurangi aktivitas luar ruangan."
        elif 151 <= aqi <= 200:
            return "Tidak Sehat", "Disarankan untuk menghindari aktivitas luar ruangan bagi semua orang."
        elif 201 <= aqi <= 300:
            return "Sangat Tidak Sehat", "Semua orang sebaiknya tidak beraktivitas di luar ruangan."
        else:
            return "Berbahaya", "Hindari semua aktivitas luar ruangan, tetap di dalam ruangan."

    def data_kota(city, state):
        url = f"http://api.airvisual.com/v2/city?city={city}&state={state}&country=indonesia&key=3865a01d-21ba-4334-9d8e-b7b6628db439"
        
        response = requests.get(url) 
        data = response.json()
        
        temperature = data['data']['current']['weather']['tp']
        humidity = data['data']['current']['weather']['hu'] 
        wind_speed = data['data']['current']['weather']['ws']
        pollution_data = data['data']['current']['pollution']
        aqi = pollution_data['aqius']
        main_pollutant = pollution_data['mainus']
        
        # Menentukan kategori AQI
        category, advice = aqi_category(aqi)

        print(f"Data Real-time untuk {city.title()}:")
        print(f"Suhu saat ini       : {temperature} °C")
        print(f"Kelembapan          : {humidity} %")
        print(f"Kecepatan Angin     : {wind_speed} m/s")
        print(f"Kualitas Udara (AQI): {aqi} - {category}")
        print(f"Anjuran             : {advice}")
        print(f"Polutan Utama       : {main_pollutant}")
        print(f"Waktu Pengukuran    : {pollution_data['ts']}")
        print("=" * 90)
    
    # Fungsi untuk memanggil fitur Analisis Udara
    while True:
        print("Daftar Kota Tersedia:")
        # Menampilkan daftar kota secara vertikal dengan bullet
        for kota in kota_provinsi:
            print(f" • {kota.title()}")
            
        print("=" * 90)
        city = input("Masukkan nama kota: ").upper()
        print("=" * 90)

        # Cek apakah kota ada di daftar
        if city in kota_provinsi:
            state = kota_provinsi[city]
            data_kota(city, state)
            break
        else:
            print("Maaf, data untuk kota tersebut belum tersedia.")
            print("=" * 90)
            continue

    # Fungsi untuk kembali ke menu
    kembali = input("ENTER untuk kembali ke menu!").lower
    if kembali == True:
        print()
    time.sleep(0.5)
    os.system("cls")