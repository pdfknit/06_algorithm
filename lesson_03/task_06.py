# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
from pprint import pprint

MATRIX_SIZE = 4

result_matrix = []
for column in range(MATRIX_SIZE):
    curr_line = []
    line_sum = 0
    for row in range(MATRIX_SIZE):
        element = int(input('Введите значение'))
        curr_line.append(int(element))
        line_sum += element

    curr_line.append(line_sum)
    result_matrix.append((curr_line))

for i in range(len(result_matrix)):
    print(result_matrix[i])
