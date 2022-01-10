k = int(input())

if k < 1 or k > 99:
    print("ошибка")

elif k == 1 or k % 10 == 1 and k != 11:
    print(k, "рубль")

elif k % 10 in [2, 3, 4] and k not in [12, 13, 14]:
    print(k, "рубля")
else:
    print(k, "рублей")
