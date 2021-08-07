# 6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен 
# его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться 
# больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток 
# число не отгадано, то вывести загаданное число.

import random

num = random.randint(0,100)

i = 0
while i < 10:
    guess = int(input('Guess a number: '))
    if guess == num:
        print('Correct!')
        break
    if guess > num:
        print('Your guess is bigger than num!')
    if guess < num:
        print('Your guess is smaller than num!')
    i += 1

if guess != num:
    print(f'Num is {num}')
