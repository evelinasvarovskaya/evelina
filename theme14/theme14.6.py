N = int(input('Enter N: '))
c = 0
i = 2
a = 0
b = 1
while N!=c:
    c = a + b
    a = b
    b = c
    i+=1
print('Порядковый номер числа Фибоначчи N: ', i)