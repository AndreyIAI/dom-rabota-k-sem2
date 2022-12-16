n=int(input("Введите количество людей в строю: "))
list_rost=list()

for i in range (n):
    k=int(input("Вводите рост по очереди " ))
    list_rost.append(k)
my_rost=int(input("Введите свой рост "))
j=1
for i in list_rost:
    if my_rost<=i:
        j+=1
print(j)