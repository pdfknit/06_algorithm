# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел. При этом каждое число представляется как коллекция,
# элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F.
# Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
from collections import deque

vocabulary = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')
count_base = len(vocabulary)


def hex_sum(a, b):
    digit_a_deque = deque()
    digit_b_deque = deque()

    for digit_a in a:
        for idx, base_number in enumerate(vocabulary):
            if digit_a == base_number:
                digit_a_deque.appendleft(idx)

    for digit_b in b:
        for idx, base_number in enumerate(vocabulary):
            if digit_b == base_number:
                digit_b_deque.appendleft(idx)

    result_deque = deque()
    plus = 0
    for digit_a, digit_b in zip(digit_a_deque, digit_b_deque):
        curr_sum = int(digit_a) + int(digit_b) + plus
        if curr_sum >= count_base:
            plus = 1
            curr_sum -= count_base
        else:
            plus = 0
        result_deque.appendleft(curr_sum)

    limit = len(digit_a_deque) - len(digit_b_deque)
    if limit > 0:
        tale = [digit_a_deque[idx] for idx in range(len(digit_b_deque), len(digit_a_deque))]
    else:
        tale = [digit_b_deque[idx] for idx in range(len(digit_a_deque), len(digit_b_deque))]

    for tale_digit in tale:
        result_deque.appendleft(plus + tale_digit)
        plus = 0
    if len(tale) == 0 and plus == 1:
        result_deque.appendleft(plus)

    result_list = []
    for digit in result_deque:
        result_list.append(vocabulary[digit])

    return ''.join(result_list)


a = input('Введите 16-ричное число:\n')
b = input('Введите 16-ричное число:\n')
print(hex_sum(a, b))
