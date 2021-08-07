# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 
# и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар 
# "код-символ" в каждой строке.

counts = list(range(32, 128))

i = 0
while i < len(counts):
    if i == 90:
        lim = len(counts)
    else:
        lim = i+10
    line = [(counts[j], chr(counts[j])) for j in range(i, lim)]
    print(line)
    i += 10