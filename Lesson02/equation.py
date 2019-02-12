# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

#equation = 'y = -12x + 11111140.2121'
#x = 2.5
# вычислите и выведите y


equation = 'y = -12x + 11111140.2121'

part1 = equation.partition('x')
print(part1)

if '+' in part1[-1]:
    part2 = part1[-1].partition('+')
else:
    part2 = part1[-1].partition('-')


B = float(part2[-2] + part2[-1].lstrip(' '))
print('B =', B)

part3 = part1[0].partition('=')
K = float(part3[-1])
print('K =', K)

x = float(input('x = '))
y = K * x + B
print('y =', y)
