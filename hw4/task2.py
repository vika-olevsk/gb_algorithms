# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# - Без использования «Решета Эратосфена»;
# - Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. 
# Результаты анализа сохранить в виде комментариев в файле с кодом.

import cProfile
n = 1000

all_nums = list(range(2,n+1))

def non_resheto():
    needed_nums = []
    i = 2
    while i < n:
        for el in all_nums:
            if i % el != 0:
                needed_nums.append(i)
        i += 1


def resheto():
    # Используя алгоритм «Решето Эратосфена»
    a = [0] * n  
    for i in range(n):  
        a[i] = i  
    a[1] = 0

    m = 2  
    while m < n:
        if a[m] != 0: 
            j = m * 2  
            while j < n:
                a[j] = 0  
                j = j + m 
        m += 1

    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])
    del a
    #print(b)



cProfile.run('non_resheto()')
# 990952 function calls in 0.338 seconds
# difficulty is o(n)
cProfile.run('resheto()')
# 172 function calls in 0.001 seconds
# difficulty is o(n**2)


