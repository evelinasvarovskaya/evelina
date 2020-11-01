N = int(input('Enter N: '))
a = []*N
nechet = 0
for i in range(0, N):
    a.append(int(input()))
for i in range(N-1, 0, -1):
    if a[i] % 2 != 0:
        nechet = a[i]
        break
for i in range(0,N):
    if a[i] % 2 != 0:
        a[i] += nechet
    print(a[i])