# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел 
# выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = 100

list = list(range(1,n+1))
sum = sum(list)

print(sum, n*(n+1)/2)