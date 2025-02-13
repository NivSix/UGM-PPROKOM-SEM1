import random
komputer = random.randint(1,10)
while True:
    tebakan = int(input('Coba tebak angka dari 1 hingga 10: '))
    if tebakan < komputer:
        print('Angkanyaa kekecilann!')
    elif tebakan > komputer:
        print('Angkanyaa kebesarann!')
    else:
        print('Selamat Tebakan Kamu Benar!')
        break