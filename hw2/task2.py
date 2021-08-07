# 2. Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


num = input('Enter a number: ')
digits = list(map(int, list(num)))

count_even = 0
count_odd = 0
for el in digits:
    if el % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print(f'Number {num} has {count_odd} odd digits and {count_even} even digits')