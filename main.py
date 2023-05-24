# Урок № 13. Двумерные списки

# Задание № 1

import random

def prm(x):
    for i in x:
        print(*i)

a = int(input("высота: "))
b = int(input("ширина: "))
print("=========================")
print("matrix1")
matrix1 = [[random.randint(-999, 999) for i in range(b)] for i in range(a)]
prm(matrix1)
print("=========================")
print("matrix2")
matrix2 = [[random.randint(-999, 999) for i in range(b)] for i in range(a)]
prm(matrix2)
print("=========================")
matrix3 = [[0 for i in range(b)] for i in range(a)]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrix3[i][j] = matrix1[i][j] + matrix2[i][j]

print("matrix3")
prm(matrix3)
print("=========================")