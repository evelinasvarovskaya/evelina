a, b, c = map(int, input().split())
print("Первоначальные значения переменных:", a, b, c)
x = a
a = c
c = b
b = x
print("Новые зна1чения переменных:", a, b, c)