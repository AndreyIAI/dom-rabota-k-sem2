#3 Minimal "/"
n=int(input("Введите число: "))
flag = True
i=2
while flag:
    if n%i==0:
        print(i)
        flag=False
    i+=1