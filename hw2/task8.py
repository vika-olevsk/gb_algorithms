# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. 
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

nums = input('Enter a list of numbers separated by space: ')
nums = nums.split()
dig = input('Enter a digit to check: ')

count = 0
for el in nums:
    dgs = list(el)
    for subel in dgs:
        if subel == dig:
            count += 1

print(count)
