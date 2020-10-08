N = int(input("Enter N: "))
A = int(input("Enter A: "))
B = int(input("Enter B: "))
a = [0]*N
a[0] = A
a[1] = B
for i in range(2,N):
    for j in range(0,i):
        a[i] += a[j]
for i in range(0,N):
    print(a[i])