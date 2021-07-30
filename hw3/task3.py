# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import sample

list = sample(range(100), 5)

min = 100
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

# replace them
print(list)
list[max_ind] = min
list[min_ind] = max
print(list)

