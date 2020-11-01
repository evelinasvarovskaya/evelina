N = int(input('Enter N: '))
a = []*N
for i in range(0, N):
    a.append(int(input()))
value = a[0]
for i in range(1, N):
    if a[i-1] > a[i]:
        t = a[i-1]
        a[i-1] = a[i]
        a[i] = t
for i in range(0, N):
    print(a[i])