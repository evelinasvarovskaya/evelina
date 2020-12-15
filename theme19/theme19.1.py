n = int(input("enter N: "))
a = []*n
for i in range(0, n):
    a.append(int(input()))
j = 0
for i in range(1, n):
     if a[j] != a[i]:
         j += 1
         a[j] = a[i]
for i in range(0, j+1):
    print(a[i])