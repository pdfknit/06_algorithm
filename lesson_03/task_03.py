# Определить, какое число в массиве встречается чаще всего

import random

SIZE = 1000
MIN_ITEM = 0
MAX_ITEM = 500
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# print(f'{array = }')

result = {}
for i in range(len(array)):
    if array[i] in result.keys():
        result[array[i]] = result[array[i]] + 1
    else:
        result[array[i]] = 1

# print(f'{result = }')
max_count = 0
max_values = []
for val, cnt in result.items():
    if cnt > max_count:
        max_values = [val]
        max_count = cnt
    elif cnt == max_count:
        max_values.append(val)
print(f'{max_count = }, {max_values = }')
