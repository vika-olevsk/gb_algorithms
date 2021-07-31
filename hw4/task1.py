# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# My algo: В диапазоне натуральных чисел от 2 до 9999 определить, 
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9999.

import cProfile
import random

def main():
    nums = list(range(2,1000))
    res = []
    for num in nums:
        count = 0
        for el in nums:
            if el % num == 0:
                count += 1
        res.append([num, count])
    #print(res)

def main2():
    nums = list(range(2,1000))
    res = {}
    for num in nums:
        count = 0
        for el in nums:
            if el % num == 0:
                count += 1
        res[num] = count
    #print(res)

cProfile.run('main()')
# 1002 function calls in 0.062 seconds
cProfile.run('main2()')
# 4 function calls in 0.082 seconds