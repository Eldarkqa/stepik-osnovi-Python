import math

a = float(input())  #сторона басейна в метрах
b = float(input())  #расход краски на 1 квадратный метр в милилитрах (10 ** (-6))
v = int(input())    #объем банки в литрах (10 ** (-3))

if a > 0 and b > 0 and v > 0:
    s = 5 * a ** 2  #площадь в м2
    n = b * s / (v * 10 ** 3)
    print(math.ceil(n))
else:
    print("error")
