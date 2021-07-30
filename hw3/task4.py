# 4. Определить, какое число в массиве встречается чаще всего.

list = [1, 4, 7, 3, 1, 5, 2, 6, 8, 4, 3, 9, 0, 5, 7, 9, 2, 1]

most_freq_num = 0

ref_count = 0
for num in list:
    count = 0
    for el in list:
        if el == num:
            count +=1
    if count > ref_count:
        ref_count = count
        most_freq_num = num

print(f'{most_freq_num} is in the list {ref_count} times')