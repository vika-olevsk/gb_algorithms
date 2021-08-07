# 4. Написать программу, которая генерирует в указанных пользователем границах:
# - случайное целое число;
# - случайное вещественное число;
# - случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. 
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
# Diagram: https://drive.google.com/file/d/1qOPEt4jV1AqkA-EGN9u03Cbv5Bg8D7mr/view?usp=sharing

import random 

format = input('Enter format (int / float / char): ')
data = input('Enter two limits in format a b: ')

if format == 'int':
    a, b = list(map(int, data.split()))
    res = random.randint(a, b)

if format == 'float':
    a, b = list(map(int, data.split()))
    res = random.uniform(a, b)

if format == 'char':
    a, b = list(map(ord, data.split()))
    res = chr(random.randint(a, b))

print(res)
