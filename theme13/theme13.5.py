A = float(input("Enter the A: "))
N = int(input("Enter the N (N>0): "))
res = 1
x = 1
for i in range(0,N):
    x = -x*A
    res = res + x
print("Значение выражения: ", int(res) )