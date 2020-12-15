n = int(input("enter N: "))
a = []*n
for i in range(0, n):
    a.append(int(input()))
min = min(a)
max = max(a)
j = 0
k = 0
for i in range(0, n):
    if a[i] != min:
        a[j] = a[i]
        j += 1
    else:
        a[j] = 0
        a[j+1] = a[i]
        j += 2
for i in range(0, n+1):
    if a[i] != max:
        a[k] = a[i]
        k += 1
    else:
        a[k] = a[i]
        a[k+1] = 0
        k += 2
for i in range(0, k):
    print(a[i])