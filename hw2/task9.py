# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. 
# Вывести на экран это число и сумму его цифр.

nums = input('Enter a list of numbers separated by space: ')
nums = nums.split()

biggest_sum = 0
needed_num = 0

for el in nums:
    sum = 0
    for subel in el:
        sum += int(subel)
    if biggest_sum < sum:
        biggest_sum = sum
        needed_num = int(el)

print(f'Biggest sum is {biggest_sum} for number {needed_num}')