# 1. В диапазоне натуральных чисел от 2 до 99 определить, 
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

nums = list(range(2,100))

res = []
for num in nums:
    count = 0
    for el in nums:
        if el % num == 0:
            count += 1
    res.append([num, count])
print(res)