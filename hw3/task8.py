# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. 
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее 
# в последнюю ячейку строки. В конце следует вывести полученную матрицу.

matrix = []
for i in range(5):
    data = input('Enter 3 numbers: ')
    data = list(map(int, data.split()))
    data.append(sum(data))
    matrix.append(data)

for i in range(5):
    for j in range(4):
        print(matrix[i][j],' ', end='')
    print()
