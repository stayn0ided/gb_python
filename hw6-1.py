# Задача 1. Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 

a1, n, d = int(input()), int(input()), int(input())
list = []
for i in range(n):
    list.append(a1 + d * i)
print(*list)