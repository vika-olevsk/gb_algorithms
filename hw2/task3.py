# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. 
# Например, если введено число 3486, то надо вывести число 6843.
import numpy as np

num = input('Enter a number: ')
digs = list(num)
rev_digs = []

for i in range(len(digs)):
    rev_digs.insert(0, digs[i])

print(''.join(rev_digs))
