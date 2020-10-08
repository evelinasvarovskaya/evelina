N = int(input("Enter N: "))
res, i = 0, 0
while res<N:
    res += i
    i+=1
res += i
print("Value: ",i)
print("Sum:", res)