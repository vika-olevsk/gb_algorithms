# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. 
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, 
# то используйте метод сортировки, который не рассматривался на уроках


import random
m = 10
list = random.sample(range(50), 2*m+1)

def select_nth(n, items):
    pivot = random.choice(items)

    lesser = [item for item in items if item < pivot]
    if len(lesser) > n:
        return select_nth(n, lesser)
    n -= len(lesser)

    numequal = items.count(pivot)
    if numequal > n:
        return pivot
    n -= numequal

    greater = [item for item in items if item > pivot]
    return select_nth(n, greater)

def median(items):
    if len(items) % 2:
        return select_nth(len(items)//2, items)

    else:
        left  = select_nth((len(items)-1) // 2, items)
        right = select_nth((len(items)+1) // 2, items)

        return (left + right) / 2

print(f'List {list} has median {median(list)}')