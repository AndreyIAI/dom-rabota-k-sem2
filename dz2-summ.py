#2 SUMM

n=int(input())
flag = True
if n<0:
    flag = False
n = abs(n)
if flag:
    print (int(((n+1)/2)*n))
else:
    print (-int(((n+1)/2)*n)+1)