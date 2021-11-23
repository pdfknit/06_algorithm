# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
# [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def rand_array(size, min_v, max_v):
    array = [random.uniform(min_v, max_v) for _ in range(size)]
    return array


def merge_sort(array):
    if len(array) == 1:
        return array

    result_array = []
    left_array = merge_sort(array[:len(array) // 2])
    right_array = merge_sort(array[len(array) // 2:])

    while len(left_array) and len(right_array):
        if left_array[0] > right_array[0]:
            result_array.append(right_array.pop(0))
        else:
            result_array.append(left_array.pop(0))

    if len(left_array) > len(right_array):
        result_array.extend(left_array)
    else:
        result_array.extend(right_array)
    return result_array


cur_array = rand_array(10, 0, 49)
print(f'Исходный массив: {cur_array}')
print(f'Результат сортировки слиянием: {merge_sort(cur_array)}')
