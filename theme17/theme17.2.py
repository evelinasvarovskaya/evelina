N = int(input('Enter N: '))
array = []*N
sum = 0
for i in range(0,N):
    array.append(int(input()))
d = array[2]-array[1]
for i in range(0,N-1):
    if array[i+1] == array[i] + d:
        sum += 1
if N == sum+1:
    print('Разность прогрессии равна', d)
else:
    print('Элементы не образуют арифметическую прогрессию', 0)