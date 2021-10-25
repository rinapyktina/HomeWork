#!/usr/bin/env python 3
# -*- encoding:utf-8 -*-
if __name__== "__main__":
    x=float(input("x?"))
    if x<= 3.5:
        y=2 * x**2 + math.cos(x)
    elif 3.5<x<=5:
        y=x + 1
    else:
        y=2 * x -x**2
print("y =", y)
