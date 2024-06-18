print('BASIR P. WAHAB')
print('1BSCE-B')
print()
print('ICT 09 Programming 1')
print('FINAL PROJECT')
print()
print('MATRIX 1')
print()
print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpose = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(3):
    for j in range(3):
        transpose[j][i] = matrix[i][j]

for row in transpose:
    print("\t".join(map(str, row)))
