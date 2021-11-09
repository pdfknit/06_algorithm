# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

SIZE = 10
MIN_ITEM = -10
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(f'{array = }')

max_index = None

for i in range(1, len(array)):
    if array[i] < 0:
        if not max_index:
            max_index = i
        elif array[i] > array[max_index]:
            max_index = i

print(f'max_value = {array[max_index]}, index = {max_index}')
