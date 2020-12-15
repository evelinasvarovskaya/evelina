n = int(input("enter N: "))
a = []*n
for i in range(0, n):
    a.append(int(input()))
j = n
for i in a:
    if a[i] > 0:
        j += 1
for i in range(n-1, 0):
    if a[i] < 0:
        a[j] = a[i]
        j -= 1
    else:
        a[j] = a[i]
        a[j-1] = 0
        j -= 2
for i in range(0, j):
    print(a[i])