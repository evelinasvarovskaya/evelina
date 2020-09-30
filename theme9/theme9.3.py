k = int(input("value К in range 1-365:"))
n = int(input("value N in range 1-7:"))
value = (n+K-2)%7+1
print("Номер дня недели для K-го дня года:", value)