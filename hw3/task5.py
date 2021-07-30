# 5. В массиве найти максимальный отрицательный элемент. 
# Вывести на экран его значение и позицию в массиве.

list = [-300, 2, -50, 12, 345, 9, -34, 1111, -5000]

ref_num = -10000
ind = 0
# find max negative element
for i, el in enumerate(list):
    if el < 0 and el > ref_num:
        ref_num = el
        ind = i

print (f'max negative number is {ref_num} on {ind} position')