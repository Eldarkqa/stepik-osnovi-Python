from math import sqrt

a = float(input())
h = float(input())

if a <= 0 or h <= 0:
    print("error")

else:
    v = h * a ** 2 / (4 * sqrt(3))
    eq1 = sqrt(3) * a ** 2 / 4
    eq2 = 3 * a * sqrt(h ** 2 + a ** 2 / 12) / 2
    s = eq1 + eq2
    print(round(v, 3), round(s, 3))
