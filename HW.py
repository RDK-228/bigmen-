import math
 
print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a==0 and a==0 and c ==0:
    print("Решение любое число(0=0)")
elif a==0 and b!=0:
    print(c/b)
elif a==0 and b==0 and c!=0:
    print("Нет решений")
else:
    discr = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % discr)
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif discr == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("Нет решений")