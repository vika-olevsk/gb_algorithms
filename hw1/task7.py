# 7. По длинам трех отрезков, введенных пользователем, определить возможность 
# существования треугольника, составленного из этих отрезков. Если такой треугольник 
# существует, то определить, является ли он разносторонним, равнобедренным или равносторонним.
# Diagram: https://drive.google.com/file/d/1GYku3UUqnH8or-yGQXZoQTMXu8MaywFv/view?usp=sharing

data = input('Enter three numbers in format a b c: ')
a, b, c = list(map(int, data.split()))

if a + b > c:
    if a == b == c:
        print('равносторонний')
    elif a==b or b==c or a==c:
        print('равнобедренный')
    else:
        print('разносторонний')
else:
    print('no')