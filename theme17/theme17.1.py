N = int(input('Enter N: '))
K = int(input('Enter K: '))
L = int(input('Enter L: '))
sum, k = 0, 0
array = []*N
for i in range(0,N):
    array.append(int(input()))
for i in range(K-1,L):
    sum += array[i]
    k += 1
res = sum/k
print('arithmetic mean is', res)