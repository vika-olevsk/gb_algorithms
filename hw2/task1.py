# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа 
# не должна завершаться, а должна запрашивать новые данные для вычислений. 
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна 
# сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о 
# невозможности деления на ноль, если он ввел 0 в качестве делителя.

oprs = ['0', '+', '-', '*', '/']

while True:
    opr = input('Choose operation (+, -, *, /): ')
    if opr == '0':
        break
    if opr not in oprs:
        print('Wrong input, enter again!')
    else:
        data = input('Enter two numbers: ')
        a, b = list(map(int, data.split()))
        if opr == '+':
            print(f'Sum is {a + b}')
        if opr == '-':
            print(f'Diff is {a - b}')
        if opr == '*':
            print(f'Product is {a * b}')
        if opr == '/':
                if b == 0:
                    print('Can not devide by 0!')
                else:
                    print(f'Quotient is {a / b}')