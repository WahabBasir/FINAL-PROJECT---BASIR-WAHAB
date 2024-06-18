print('BASIR P. WAHAB')
print('1BSCE-B')
print()
print('ICT 09 Programming 1')
print('FINAL PROJECT')
print()
print('MATRIX 2')
print()
print()

import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

row_sums = np.sum(arr, axis=1)

col_sums = np.sum(arr, axis=0)

print("Input Array:")
print(arr)

print("\nSum of rows:")
print(row_sums)

print("\nSum of columns:")
print(col_sums)
