N = int(input('Enter N: '))
array = []*N
j = 0
for i in range(0, N):
    array.append(int(input()))
min = array[1]
for i in range(1, N, 2):
    if array[i]<min:
        min = array[i]
print('Minimum value: ',min)