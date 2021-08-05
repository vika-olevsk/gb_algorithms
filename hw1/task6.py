# 6 . Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
# Diagram: https://drive.google.com/file/d/1R558TqzzI6YRMe8pTlvlJHTUad05ZETl/view?usp=sharing

num = int(input('Enter number of the letter : '))

start = ord('a')
ascii = start + num - 1 

print(f'Letter is on the {chr(ascii)}')