N = int(input('Enter N: '))
a = []*N
sum = 0
for i in range(0,N):
    a.append(int(input()))
for i in range(1, N-1):
    if i == 1:
        if a[1]<a[2]:
            sum = 1
    if i == N:
        if a[N+1]>a[N]:
             sum = N
    else:
        if a[i-1] < a[i] and a[i] > a[i+1]:
            sum = i
print('Local maximum: ',sum)