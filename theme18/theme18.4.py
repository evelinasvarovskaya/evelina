N = int(input('Enter N: '))
a = []*N
for i in range(0, N):
    a.append(int(input()))
max, chmax, chmin = 0, 0, 0
min = a[0]
for i in range(0,N):
    if a[i] > max:
        max  = a[i]
        chmax = i
    if a[i] < min:
        min = a[i]
        chmin = i
if chmax > chmin:
    for i in range(chmin+1,chmax):
        a[i] = 0
if chmax < chmin:
    for i in range(chmax+1,chmin):
        a[i] = 0
for i in range(0, N):
    print(a[i])