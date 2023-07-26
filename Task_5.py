# Напиши функцию которая принимает строку и умеет решать уравнения типов
#
# Nx + y = 0
# x^N + y = 0
# Ax^2 + Bx + c = 0

def solve_eq(equation):
    equation = equation.split()
    print(equation)
    if len(equation) == 7:
       a = int(equation[0][:1])
       b = int(equation[1] + equation[2][:1])
       c = int(equation[3] + equation[4][:1])
       D = b ** 2 - 4 * a * c
       x1 = ((-b + D ** 0.5) / (2 * a))
       x2 = ((-b - D ** 0.5) / (2 * a))
       print(x1, x2)
    if (len(equation) == 5 and equation[0][1:2] == '^'):
        a1 = int(equation[0][2:3])
        b1 = int(equation[2])
        if equation[1] == '-':
            x3 = b1**(1/a1)
            print(x3)
        else:
            x3 = -b1**(1/a1)
            print(x3)
    if (len(equation) == 5 and equation[0][1:2] != '^'):
        a2 = int(equation[0][:1])
        b2 = int(equation[2])
        if equation[1] == '-':
            x4 = b2/a2
            print(x4)
        else:
            x4 = -b2/a2
            print(x4)


print(solve_eq('3x^2 - 18x + 27 = 0'))
print(solve_eq('x^3 + 9 = 0'))
print(solve_eq('4x + 8 = 0'))