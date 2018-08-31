import random as r
c1=eval(input('Please input an integer: '))
c2=0
for i in range(c1):
    x=r.random()
    y=r.random()
    if x**2+y**2<=1:
        c2+=1
print(c2/c1*4)        
