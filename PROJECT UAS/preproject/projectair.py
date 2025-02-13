def fungsi_utama(x):
    def fungsi_bersarang(y):
        return y ** 2
    
    hasil = fungsi_bersarang(x) + x
    return hasil

print(fungsi_utama(5))  # Output: 30 (5^2 + 5)
