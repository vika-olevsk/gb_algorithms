# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят 
# и сколько между ними находится букв.
# Diagram: https://drive.google.com/file/d/1RZ8Jmxw_KtooJkXNvJWvj163gmI_L3ps/view?usp=sharing

data = input('Enter two letters in format a b: ')
a, b = data.split()

start = ord('a')

print(f'First letter is on the {ord(a) - start + 1} place, second letter is on the ' +
        f'{ord(b) - start + 1}, distance between them is {abs(ord(b) - ord(a))} letters')