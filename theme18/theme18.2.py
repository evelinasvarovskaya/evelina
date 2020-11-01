N = int(input('Enter N: '))
a = []*N
b =[0]*N
s = 0
sum = 0
for i in range(0,N):
    a.append(int(input()))
for i in range(1,N+1):
    for j in range(0,i):
        b[i-1] += a[j]
    b[i-1] = b[i-1]/i
for i in range(0,N):
    print(b[i])