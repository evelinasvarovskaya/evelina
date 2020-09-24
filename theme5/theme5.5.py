import math

x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
r1 = math.sqrt((x2-x1)**2+(y2-y1)**2)
r2 = math.sqrt((x2-x3)**2+(y2-y3)**2)
r3 = math.sqrt((x3-x1)**2+(y3-y1)**2)
p = r1+r2+r3
s = math.sqrt(p*(p-r1)*(p-r2)*(p-r3))
print(p, s)