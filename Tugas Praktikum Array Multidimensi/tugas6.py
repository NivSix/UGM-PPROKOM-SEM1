Array1 = [
    [4,6],
    [1,7]
    ]
Array2 = [
    [2,3],
    [5,6]
    ]

for x in range(0, len(Array1)):
    for y in range(0, len(Array1[0])):
        print (Array1[x][y] + Array2[x][y], end=' '),
    print()