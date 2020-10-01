a = int(input('Enter A: '))
b = int(input('Enter B: '))
c = int(input('Enter C: '))
sum = 0
if a<b and a<c:
    sum = b+c
elif b<a and b<c:
    sum = a+c
elif c<a and c<b:
    sum = a+b
print('The sum of the 2 largest value is', sum)