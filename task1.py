#!/usr/bin/env python 3
# -*- encoding:utf-8 -*-
if __name__== "__main__":
    x=float(input("x?"))
    y=float(input("y?"))
    R=float(input("R?"))
    r=(x**2 + y**2)**0.5
    if r>R :
        print("Не принадлежит")
    else:
        print("Принадлежит")
