# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import numpy as np

matrix = np.array([[1, 12, 4, 7], 
                    [23, 56, 2, 1], 
                    [11, 56, 87, 32], 
                    [12, 3, 8, 9]])

# find min elements in each column:
m_t = matrix.T
mins = [] 
for el in m_t:
    min = 10000
    for subel in el:
        if subel < min:
            min = subel
    mins.append(min)


max = 0
# find max amoung min elements
for el in mins:
    if el > max:
        max = el
print(max)