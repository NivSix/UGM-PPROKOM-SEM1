matriks = [[0 for k in range(3)] for b in range(2)]

for b in range(2):
    for k in range(3):
        matriks[b][k] = int(input(f"Masukkan nilai ke-[{b}][{k}] "))
        if k == 2:
            print("-" * 20)

for b in range(2):
    for k in range(3):
        print(matriks[b][k], end=" ")
    print()