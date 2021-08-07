# 9. Вводятся три разных числа. Найти, какое из них является средним 
# (больше одного, но меньше другого).
# https://drive.google.com/file/d/1kMGQ5ctAShBXpZavMDMQQLSbQLjggmC7/view?usp=sharing

data = input('Enter three numbers in format a b c: ')
a, b, c = sorted(list(map(int, data.split())))

if a<b<c:
    print(b)
elif c<a<b:
    print(a)
else:
    print(c)

