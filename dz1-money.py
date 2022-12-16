#1. Money
from random import randint

gerb =0 
resh = 0
list=list()
for i in range(5):
    list.append(randint(0,1))
print (list)
for i in list:
    if i == 0:
        gerb += 1
    else :
        resh +=1
print(min(gerb, resh,))