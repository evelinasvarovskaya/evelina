x1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
r1 = abs(x1-x2)
r2 = abs(y1-y2)
p = (r1+r2)*2
s = r1*r2
print(p, s)