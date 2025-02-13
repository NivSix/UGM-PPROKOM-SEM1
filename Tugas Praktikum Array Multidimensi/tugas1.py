grid = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 50

found = False
for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] == target:
            print (f"Element {target} found at ({row}, {col})")
            found = True
            break
        if found:
            break

if not found:
    print(f"Element {target} not found")