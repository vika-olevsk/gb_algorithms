# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.


num = int(input('Enter a number: '))
num_set = []

i = 0
while i < num:
    if i % 2 == 0:
        num_set.append(1 / 2**i)
    else:
        num_set.append(-1 / 2**i)
    i += 1

print(sum(num_set))