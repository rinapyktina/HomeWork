#!/usr/bin/env python 3
# -*- encoding:utf-8 -*-
if __name__== "__main__":
    a=float(input("a? "))
    b=float(input("b? "))
    c=float(input("c? "))
    import math
    if a==0:
        print("Ошибка")
    else:
        discr = b**2 - 4 * a * c
        if discr > 0:
            x1 = (-b + math.sqrt(discr)) / (2 * a)
            x2 = (-b - math.sqrt(discr)) / (2 * a)
            if x1 == x2 :
                print("x =", x1)
            else:
                print("x1 =", x1, ", x2 =", x2)
        elif discr == 0:
            x = -b / (2 *a)
            print("x =", x)
        elif discr < 0:
            print("Корней нет")
