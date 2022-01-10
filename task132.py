# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 22:08:00 2021

@author: Mr
"""
from math import sqrt


def compute_len(x_0, y_0, x_1, y_1):
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len_line


def compute_area(a_1, a_2, a_3):
    p = (a_1 + a_2 + a_3) / 2
    area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
    return area


x_a = float(input("x_a = "))
y_a = float(input("y_a = "))
x_b = float(input("x_b = "))
y_b = float(input("y_b = "))
x_c = float(input("x_c = "))
y_c = float(input("y_c = "))

c = compute_len(x_a, y_a, x_b, y_b)
a = compute_len(x_b, y_b, x_c, y_c)
b = compute_len(x_a, y_a, x_c, y_c)

if a + b <= c or b + c <= a or a + c <= b:
    print("error")

else:
    s = compute_area(a, b, c)
    p = (a + b + c) / 2
    r = sqrt((p - a) * (p - b) * (p - c) / p)
    R = a * b * c / (4 * s)
    Ma = sqrt(2 * (c ** 2 + b ** 2) - a ** 2) / 2
    Mb = sqrt(2 * (a ** 2 + c ** 2) - b ** 2) / 2
    Mc = sqrt(2 * (a ** 2 + b ** 2) - c ** 2) / 2
    M = Ma + Mb + Mc
    print(round(r, 4), round(R, 4), round(M, 4))
