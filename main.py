import random


#Homework 1
a = int(input())
b = int(input())

matrix_1 = [[random.randint(1,11)
            for i in range(b)]
            for j in range(a)]
print('Matrix 1: ')

for i in range(a):
    print(matrix_1[i])

matrix_2 = [[random.randint(1,11)
            for i in range(b)]
            for j in range(a)]
print('Matrix 2: ')

for i in range(a):
    print(matrix_2[i])

res = [[matrix_1[i][j] + matrix_2[i][j] 
       for i in range(len(matrix_1))]
       for j in range(len(matrix_1))]
print('Сложения двух матриц: ')

for r in res:
    print(r)
