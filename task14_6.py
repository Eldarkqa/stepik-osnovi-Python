h = int(input())
m = int(input())
s = int(input())

if 0 <= h <= 11 and 0 <= m <= 59 and 0 <= s <= 59:
    a = h * 30 + m * 0.5 + s * 0.5 / 60
    print(round(a, 2))
else:
    print("error")
