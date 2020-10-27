def Fact2(N):
    if N%2 != 0:
        factorial = 1
        while N > 1:
            factorial *= N
            N -= 2
    if N%2 == 0:
        factorial = 1
        while N > 1:
            factorial *= N
            N -= 2
    return factorial
a = float(int(input('Enter N: ')))
print(Fact2(a))