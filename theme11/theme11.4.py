x,y = map(int,input('Enter X,Y: ').split())
if x>0 and y>0:
    print('first quarter')
elif x<0 and y>0:
    print('Second quarter')
elif x<0 and y<0:
    print('third quarter')
else:
    print('fourth quarter')