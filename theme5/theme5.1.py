import math

x1,y1,x2,y2 = map(int, input().split())
r = (x2-x1)**2+(y2-y1)**2
r = math.sqrt(r)
print(r)