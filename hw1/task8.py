# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
# Diagram: https://drive.google.com/file/d/1IU0LwDK4ngWFitCeybxhPh53RXCoV_LT/view?usp=sharing

year = int(input('Enter a year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('високосный')
        else: 
            print('не високосный')
    else:
        print('високосный')
else:
    print('не високосный')