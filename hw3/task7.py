# 7. В одномерном массиве целых чисел определить два наименьших элемента. 
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

list = [300, 5, 50, 12, 345, 9, 34, 1111, 2]

first_num = 10000
ind_fn = 0
second_num = 10000

# find first_num
for i, el in enumerate(list):
    if el < first_num:
        first_num = el
        ind_fn = i

# find second num
for i, el in enumerate(list):
    if el < second_num and second_num >= first_num and i != ind_fn: 
        second_num = el


print(first_num, second_num)