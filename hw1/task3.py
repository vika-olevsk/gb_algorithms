# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, 
# проходящей через эти точки.
# Diagram: https://drive.google.com/file/d/1jd8STBuA-vtLn-bVP2RGy0lDGBZygtVi/view?usp=sharing

data = input('Enter two coordinates in format x1 y1 x2 y2: ')
x1, y1, x2, y2 = list(map(int, data.split()))

k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1

print(f'y = {k} * x + {b}')


