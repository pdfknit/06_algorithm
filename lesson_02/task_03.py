# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, надо вывести 6843.

def mirror(digit, mirror_digit=0):
    if digit == 0:
        return mirror_digit
    else:
        cur_element = digit % 10
        mirror_digit = mirror_digit * 10 + cur_element
        return mirror(digit=digit // 10, mirror_digit=mirror_digit)


a = int(input('Введите число\n'))

print('Результат:', mirror(a))
