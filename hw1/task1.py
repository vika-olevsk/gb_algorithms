# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь
# Diagram here: https://drive.google.com/file/d/19gotd8rQdNPXUBpWJumfWbBqJl5idoZT/view?usp=sharing

import numpy as np

num = input('Enter 3-digit number:')
num = list(map(int, list(num)))

sum_num = sum(num)
mult_num = np.prod(num)

print(sum_num, mult_num)