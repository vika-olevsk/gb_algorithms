# 1. Определение количества различных подстрок с использованием хэш-функции. 
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. 
# Требуется найти количество различных подстрок в этой строке.

import hashlib

s = 'dsdsasdhjksdfhjksdfhjk'

hashs = set()
for i in range(len(s)+1):
    for j in range(len(s)+1):
        if j > i:
            hashs.add(hashlib.sha1(s[i:j].encode('utf-8')).hexdigest())

print(len(hashs))
