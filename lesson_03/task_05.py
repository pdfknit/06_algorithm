# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{array = }')

min_index = 0
max_index = 0

for i in range(1, len(array)):
    if array[i] < array[min_index]:
        min_index = i
    elif array[i] > array[max_index]:
        max_index = i

result = 0
if max_index > min_index:
    start = min_index + 1
    last_el = max_index
else:
    start = max_index + 1
    last_el = min_index

for i in range(start, last_el):
    result += array[i]

print('Сумма элементов между максимальным и минимальным =', result)
