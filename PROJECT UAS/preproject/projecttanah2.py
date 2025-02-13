# Program untuk Analisis Kesuburan Tanah dengan Rekomendasi Perbaikan

def check_soil_fertility():
    # Input dari pengguna untuk setiap karakteristik tanah
    color = input("Apakah warna tanah gelap? (ya/tidak): ").strip().lower()
    texture = input("Apakah tekstur tanah gembur? (ya/tidak): ").strip()
    moisture = input("Apakah tanah lembab? (ya/tidak): ").strip().lower()
    pH = float(input("Berapa pH tanah? (0-14): "))
   

    # Kriteria kesuburan
    fertile_criteria = [
        color == "ya",
        texture == "ya",
        moisture == "ya",
        6.0 <= pH <= 7.5,
       
    ]
    
    # Menyimpan rekomendasi jika ada kriteria yang tidak terpenuhi
    recommendations = []
    
    if color != "ya":
        recommendations.append("Tambahkan kompos atau bahan organik untuk meningkatkan kandungan humus sehingga warna tanah menjadi lebih gelap.")
        
    if texture != "ya":
        recommendations.append("Tambahkan bahan organik atau pasir kasar untuk memperbaiki tekstur tanah agar lebih gembur.")
        
    if moisture != "ya":
        recommendations.append("Perbaiki retensi air tanah dengan menambahkan bahan organik, atau lakukan penyiraman secara rutin untuk menjaga kelembaban.")
        
    if not (6.0 <= pH <= 7.5):
        if pH < 6.0:
            recommendations.append("pH tanah terlalu asam. Tambahkan kapur pertanian (dolomit) untuk menetralkan pH.")
        else:
            recommendations.append("pH tanah terlalu basa. Tambahkan sulfur atau pupuk asam untuk menurunkan pH.")


    # Menentukan hasil kesuburan tanah dan memberikan output
    if all(fertile_criteria):
        print("Tanah ini sangat subur! Cocok untuk pertumbuhan tanaman.")
    elif len(recommendations) <= 2:
        print("Tanah ini cukup subur, tetapi ada beberapa hal yang dapat ditingkatkan:")
        for recommendation in recommendations:
            print(f"- {recommendation}")
    else:
        print("Tanah ini kurang subur. Berikut adalah beberapa rekomendasi untuk memperbaiki kesuburan tanah:")
        for recommendation in recommendations:
            print(f"- {recommendation}")

# Menjalankan fungsi analisis tanah
check_soil_fertility()
