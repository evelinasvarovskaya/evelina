N = int(input('Enter N: '))
a = []*N
for i in range(0, N):
    a.append(int(input()))
for i in range(0,N-1):
    for j in range(i+1,N):
        if a[i] == a[j]:
            print('numbers of identical elements: ',i,j)