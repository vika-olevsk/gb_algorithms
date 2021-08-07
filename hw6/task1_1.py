# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах 
# в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее 
# эффективным использованием памяти.

# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода 
# для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду. 
# Также укажите в комментариях версию Python и разрядность вашей ОС.

# OS: 64-bit, Python 3.8.10

# My example task: Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь

import numpy as np

num = input('Enter 3-digit number:')
num = list(map(int, list(num)))
sum_num = sum(num)
mult_num = np.prod(num)
print(sum_num, mult_num)

# Расчеты памяти для такого кода. Наши переменные: num (list с 3 элементами int), sum_num (int),
# mult_num (int)

# num = 40 + 8 * 3 = 64 bits
# sum_num = 24 bits
# mult_num = 24 bits
# total = 64 + 24 + 24 = 112 bits = 14 bytes

