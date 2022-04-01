'''Viết chương trình tính tích của
    2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).
'''

matrix_A = [[-2, 3, 1],
            [-4, 0, 3],
            [2, -3, 4]]
matrix_B = [[1, 2, -3],
            [2, 3, 1],
            [3, 2, -2]]
matrix_C = []
m = len(matrix_A)
n = len(matrix_A[0])
p = len(matrix_B[0])

for i in range(m):
    temp = []
    for j in range(p):
        c_ij = 0
        for k in range(n):
            c_ij += matrix_A[i][k] * matrix_B[k][j]
        temp.append(c_ij)
    matrix_C.append(temp)

print(f"Kết quả: {matrix_C}")