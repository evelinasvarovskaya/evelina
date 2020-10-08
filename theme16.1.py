N = int(input("Enter N: "))
a = [0]*N
x = 1
for i in range(0,N):
    a[i] = x
    x+=2
    print(a[i])