# My example task: Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
# Например, если введено число 3486, то надо вывести число 6843.
import numpy as np

num = input('Enter a number: ')
digs = list(num)
rev_digs = []
for i in range(len(digs)):
    rev_digs.insert(0, digs[i])
print(''.join(rev_digs))

# Расчеты памяти для такого кода. Наши переменные: num (str), digs (list of size len(num)),
# rev_digs (list of size len(num))

# Для num = '1234'
# num = 37 + 4 = 41 bits
# digs = 40 + 8 * 4 + (37 + 1) * 4 = 224 bits
# rev_digs =  40 + 8 * 4 + (37 + 1) = 224 bits
# total = 41 + 224 + 224 = 489 bits = 61.125 bytes