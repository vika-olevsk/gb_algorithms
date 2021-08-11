# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
from collections import Counter

s = 'vika loves kiwi'

counter = Counter(s)
print(counter)

# Counter({'i': 3, 'v': 2, 'k': 2, ' ': 2, 'a': 1, 'l': 1, 'o': 1, 'e': 1, 's': 1, 'w': 1})
# Diagram: https://drive.google.com/file/d/14zGL0cPBvvnNrl7S5x2ehVenGSclMbd4/view?usp=sharing
simb = {'i': '00', 'v': '010', 'k': '011', ' ': '100', 'a': '1010', 'l': '1011', 'o':'1100', 
        'e':'1101', 's': '1110', 'w': '1111'}

code = ''
for letter in s:
    code += simb[letter] + ' '
print(code)