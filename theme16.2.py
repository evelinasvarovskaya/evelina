N = int(input("Enter N: "))
A = int(input("Enter A: "))
D = int(input("Enter D: "))
a = [0]*N
x = 0
for i in range(0,N):
    a[i] = A*(D**x)
    x+=1
    print(a[i])