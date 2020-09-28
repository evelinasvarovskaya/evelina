a1 = int(input())
b1 = int(input())
c1 = int(input())
a2 = int(input())
b2 = int(input())
c2 = int(input())
delta = a1*b2 - a2*b1
deltax = c1*b2 - c2*b1
deltay = a1*c2 - a2*c1
x = deltax/delta
y = deltay/delta
print(delta, deltax, deltay)
print(x,y)
