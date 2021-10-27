#!/usr/bin/env python 3
# -*- encoding:utf-8 -*-
if __name__== "__main__":
    a = float(input("a? "))
    if a == 0:
        print("Ошибка")
    else:
        b = float(input("b? "))
        c = float(input("c? "))
        import math
        discr = b ** 2 - 4 * a * c
    if discr > 0:
            t1 = (-b + math.sqrt(discr)) / (2 * a)
            t2 = (-b - math.sqrt(discr)) / (2 * a)
            x1 = math.sqrt(t1)
            x2 = - (math.sqrt(t1))
            x3 = math.sqrt(t2)
            x4 = - (math.sqrt(t2))
            if t1 == t2:
                t1 = t2
                x = math.sqrt(t1)
                x_ = - (math.sqrt(t1))
                print("x1 = %.2f \nx2 = %.2f" % (x, x_))
            else:
                print("x1 = %.2f \nx2 = %.2f \nx3 = %.2f \nx4 = %.2f" % (x1, x2, x3, x4))
    elif discr == 0:
            t = -b / (2 *a)
            if t >= 0:
                x_0 = math.sqrt(t)
                x_1 = - (math.sqrt(t))
                print("x1 = %.2f \nx2 = %.2f" % (x_0, x_1))
            else:
                 print("Корней нет")
    elif discr < 0:
            print("Корней нет")

