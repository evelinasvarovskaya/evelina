n = int(input("Enter N (N>0): "))
res = 1
x = 1.1
for i in range(0,n):
    res = res*x
    x = x+0.1
print(res)