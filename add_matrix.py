import numpy as np
 
# ---------- Using Python Lists ----------
print("----- Matrix Addition using Lists -----")
A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
 
B = [[9, 8, 7],
     [6, 5, 4],
     [3, 2, 1]]
 
rows = len(A)
cols = len(A[0])
result = [[0 for _ in range(cols)] for _ in range(rows)]
 
for i in range(rows):
    for j in range(cols):
        result[i][j] = A[i][j] + B[i][j]
 
print("Matrix A:", A)
print("Matrix B:", B)
print("Sum (using lists):")
for row in result:
    print(row)
 
# ---------- Using NumPy ----------
print("\n----- Matrix Addition using NumPy -----")
np_A = np.array(A)
np_B = np.array(B)
np_result = np_A + np_B
 
print("Matrix A:\n", np_A)
print("Matrix B:\n", np_B)
print("Sum (using NumPy):\n", np_result)
