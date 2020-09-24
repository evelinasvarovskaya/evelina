a, b, c = map(int, input().split())
print("Первоначальные значения переменных:", a, b, c)
x = a
a = b
b = c
c = x
print("Новые значения переменных:", a, b, c)