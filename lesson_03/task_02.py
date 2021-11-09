# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{array = }')

min_index = 0
max_index = 0

for i in range(1, len(array)):
    if array[i] < array[min_index]:
        min_index = i
    elif array[i] > array[max_index]:
        max_index = i

max_value = array[max_index]
array[max_index] = array[min_index]
array[min_index] = max_value
print(f'{array = }')
