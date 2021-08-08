# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, 
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и 
# отсортированный массивы. Сортировка должна быть реализована в виде функции. 
# По возможности доработайте алгоритм (сделайте его умнее).

import random
list = random.sample(range(-100, 100), 10)

def bubble_sort(input_list):
    n = 1
    while n < len(input_list):
        for i in range(len(input_list)-n):
            if input_list[i] > input_list[i+1]:
                input_list[i],input_list[i+1] = input_list[i+1],input_list[i]
        n += 1
    return input_list


print(list)
print(bubble_sort(list))