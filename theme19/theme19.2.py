##переделать

n = int(input("enter N:" ))
a = []*n
for i in range(0, n):
    a.append(int(input()))
i = 1
sum = 0
while i <= n:
    k = 0
    for j in range(1, n-1):
        if a[i] == a[j]:
            k += 1
        if k != 2:
            i += 1
        else:
            for m in range(i, n):
                if a[m] == a[i]:
                    sum += 1
                for l in range(m, sum):
                    a[l] = a[l+1]
print(sum)
for i in range(0, sum):
    print(a[i])