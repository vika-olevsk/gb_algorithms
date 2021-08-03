# 1. Пользователь вводит данные о количестве предприятий, их наименования 
# и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. 
# Программа должна определить среднюю прибыль (за год для всех предприятий) 
# и вывести наименования предприятий, чья прибыль выше среднего 
# и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

comp_data = {}
num_of_comp = int(input('Enter number of companies: '))
sum_rev = 0

for i in range(num_of_comp):
    name = input(f'Enter name of company {i+1}: ')
    qoq = input(f'Enter QoQ revenue of {name}, four numbers: ')
    qoq = list(map(int, qoq.split()))
    y_rev = sum(qoq)
    comp_data[name] = y_rev
    sum_rev += y_rev

avg_rev = sum_rev / num_of_comp
lower_rev = []
higher_rev = []

for i in comp_data:
    print()
    if comp_data[i] < avg_rev:
        lower_rev.append(i)
    else:
        higher_rev.append(i)
        
print(avg_rev, comp_data)
print('Companies with revenue lower than averageare: ', lower_rev)
print('Companies with revenue higher than averageare: ', higher_rev)