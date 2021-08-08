# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, 
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и 
# отсортированный массивы.


import random
list = random.sample(range(50), 10)

def merge(left_list, right_list):  
    sorted_list = []
    left_list_index = right_list_index = 0
    left_list_len, right_list_len = len(left_list), len(right_list)

    for _ in range(left_list_len + right_list_len):
        if left_list_index < left_list_len and right_list_index < right_list_len:
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        elif left_list_index == left_list_len:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_len:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):  
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)

print(list)
print(merge_sort(list))