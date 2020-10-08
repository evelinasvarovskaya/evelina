A = float(input("Enter the A: "))
N = int(input("Enter the N (N>0): "))
res = 0
for i in range(0,N+1):
    res += A**i
print(res)