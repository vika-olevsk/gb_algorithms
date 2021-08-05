# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. 
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. 
# Объяснить полученный результат.
# Diagram: https://drive.google.com/file/d/12XNAmsinHWurG_veKcvlBzTb-_bhrOU3/view?usp=sharing

a = list(map(int, list(bin(5))[2:]))
b = list(map(int, list(bin(6))[2:]))

and_res = [0, 0, 0]
or_res = [0, 0, 0]
for i in range(3):
    if a[i] == 1 and b[i] == 1:
        and_res[i] = 1
        or_res[i] = 1
    elif a[i] == 1 or b[i] == 1:
        or_res[i] = 1

print(and_res, or_res)

shift_left = [0, 0]
shift_left.insert(0, a[-1])
# shifted by two zeros from left side
shift_right = [0, 0]
shift_right.append(a[-1])
# shifted by two zeros from right side
print(shift_left, shift_right)