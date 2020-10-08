N = int(input("Enter N: "))
a = []*N
for i in range(0,N):
    a.append(int(input()))
j = 0
k = N-1
for i in range(0,N):
    if i%2 == 0:
        print(a[j])
        j+=1
    else:
        print(a[k])
        k-=1