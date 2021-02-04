matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# matrix = matrix[::-1]
# print(matrix)
# n = len(matrix)
# for i in range(n):
#     for j in range(i + 1, n):
#         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
# print(matrix)

matrix = list(zip(*reversed(matrix)))
print(matrix)