A = int(input('Enter A: '))
B = int(input('Enter B: '))
while A!=B:
    if A>B:
        A = A-B
    if A<B:
        B = B-A
print("НОД :", A)