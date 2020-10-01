a = int(input('Enter A: '))
b = int(input('Enter B: '))
if a==b:
    a=b=0
elif a>b:
    b = a
elif a<b:
    a = b
print('new variable values a, b: ', a, b)