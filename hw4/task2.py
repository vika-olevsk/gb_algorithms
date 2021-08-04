# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# - Без использования «Решета Эратосфена»;
# - Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. 
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile
n = 100


def non_resheto():
    needed_nums = [2]
    i = 3
    while len(needed_nums) < n:
        check = 0
        for el in needed_nums:
            if i % el == 0:
                check = 1
        if check == 0:
            needed_nums.append(i)
        i += 1
    #print(needed_nums)



def resheto():
    black_list = []
    white_list = []
    x = 2
    while len(white_list) < n:
        if x not in black_list:
            white_list.append(x)
            for j in range(2,n*n):
                black_list.append(x*j)
        x += 1
    #print(white_list)






cProfile.run('non_resheto()')
# 643 function calls in 0.002 seconds
# difficulty is o(n)
cProfile.run('resheto()')
# 1000445 function calls in 1.197 seconds
# difficulty is o(n**2)


