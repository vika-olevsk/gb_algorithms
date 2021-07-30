# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и 
# максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

list = [300, 2, 50, 12, 345, 9, 34, 1111, 5]

min = 10000
max = 0
max_ind = 0
min_ind = 0

# find max and min elements
for i, el in enumerate(list):
    if el > max:
        max = el
        max_ind = i
    elif el < min:
        min = el
        min_ind = i

print(sum(list[min_ind+1:max_ind]))