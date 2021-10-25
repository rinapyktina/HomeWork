#!/usr/bin/env python 3
# -*- encoding:utf-8 -*-
if __name__== "__main__":
    x=int(input("Номер месяца:"))
    if 3<=x<=5:
        print("Весна")
    elif 6<=x<=8:
            print("Лето")
    elif 9<=x<=11:
                print("Осень")
    elif x==12 or x==1 or x==2:
        print("Зима")
    else:
       if x<1 or x>12:
            print("Ошибка")
