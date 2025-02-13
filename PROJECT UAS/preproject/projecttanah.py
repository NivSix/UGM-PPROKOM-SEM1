# Program untuk Analisis Kesuburan Tanah

def check_soil_fertility():
    # Input dari pengguna untuk setiap karakteristik tanah
    color = input("Apakah warna tanah gelap (ya/tidak)? ").strip().lower()
    texture = input("Apakah tekstur tanah gembur atau lempung (ya/tidak)? ").strip().lower()
    moisture = input("Apakah kelembaban tanah stabil (ya/tidak)? ").strip().lower()
    pH = float(input("Berapa pH tanah (0-14)? "))
    nutrients = input("Apakah tanah mengandung unsur hara yang cukup (ya/tidak)? ").strip().lower()
    organisms = input("Apakah ada banyak mikroorganisme dalam tanah (ya/tidak)? ").strip().lower()
    structure = input("Apakah struktur tanah stabil dan tidak mudah padat (ya/tidak)? ").strip().lower()

    # Kriteria kesuburan
    fertile_criteria = [
        color == "ya",
        texture == "ya",
        moisture == "ya",
        6.0 <= pH <= 7.5,
        nutrients == "ya",
        organisms == "ya",
        structure == "ya"
    ]
    
    # Menentukan apakah tanah subur
    if all(fertile_criteria):
        print("Tanah ini subur.")
    else:
        print("Tanah ini kurang subur.")
        
# Menjalankan fungsi analisis tanah
check_soil_fertility()
