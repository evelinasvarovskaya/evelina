N = int(input('Enter N: '))
a = []*N
for i in range(0,N):
    a.append(int(input()))
for i in range(0,N):
    if i%2 != 0:
        print(a[i])
for i in range(N-1,-1,-1):
    if i%2 == 0:
        print(a[i])
