# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0'
# в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), программа должна сообщать
# об ошибке и снова запрашивать знак операции. Также она должна сообщать пользователю о невозможности деления на ноль,
# если он ввел его в качестве делителя.
while True:
    a = int(input('Введите первое число'))
    b = int(input('Введите второе число'))
    op = input('Введите операцию или 0 для выхода')
    if op == '0':
        break
    elif op == '+':
        result = a + b
    elif op == '-':
        result = a + b
    elif op == '/':
        if b == 0:
            result = 'Делить на 0 нельзя'
        else:
            result = a / b
    elif op == '*':
        result = a * b

    print(result)