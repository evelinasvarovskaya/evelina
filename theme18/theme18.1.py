N = int(input('Enter N: '))
a = []*N
b = []*N
c = [0]*N
for i in range(0,N):
    a.append(int(input()))
for i in range(0,N):
    b.append(int(input()))
for i in range(0,N):
    c[i] = a[i]
    a[i] = b[i]
    b[i] = c[i]
for i in range(0,N):
    print(a[i])
for i in range(0,N):
    print(b[i])