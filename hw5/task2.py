# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
# При этом каждое число представляется как массив, элементы которого это цифры числа. 
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import OrderedDict
d = OrderedDict({'A': 10, 'B': 11, 'C': 12, 'D':13, 'E':14, 'F': 15})

def hex2dec(hex_num):
    dec_num = 0
    for i, el in enumerate(list(reversed(hex_num))):
        if el.isdigit():
            dec_num += int(el) * 16**i
        else:
            dec_num += d[el] * 16**i
    return dec_num


def dec2hex(num):
    hex_num = []
    check = True
    while check:
        if num < 10:
            check = False
            hex_num.append(str(num))
        elif 10 <= num < 16 :
            check = False
            for char, val in d.items():  
                if val == num:
                    print(char)
                    hex_num.append(char)
        elif num > 16:
            res = num % 16
            if res < 10:
                hex_num.append(str(res))
            elif 10 <= res < 16 :
                for char, val in d.items():  
                    if val == res:
                        hex_num.append(char)
            num = num // 16
    return list(reversed(hex_num))



num1 = list(input('Enter first Hexadecimal number:'))
num2 = list(input('Enter second Hexadecimal number:'))

def sum(x, y):
    x_dec = hex2dec(x)
    y_dec = hex2dec(y)
    sum_dec = x_dec + y_dec
    sum_hex = dec2hex(sum_dec)
    return sum_hex

def mult(x, y):
    x_dec = hex2dec(x)
    y_dec = hex2dec(y)
    mult_dec = x_dec * y_dec
    mult_hex = dec2hex(mult_dec)
    return mult_hex

res_sum = sum(num1, num2)
res_mult = mult(num1, num2)
print(f'Sum of {num1} and {num2} is {res_sum}')
print(f'Mult of {num1} and {num2} is {res_mult}')

