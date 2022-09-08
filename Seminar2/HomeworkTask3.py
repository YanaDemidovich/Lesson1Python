# Задать список из n чисел последовательности (1 + 1/n)^n 
# и вывести на экран их сумму

n = int(input('Введите число: '))
list = []
for i in range(1, n+1):
    list.append(round((1 + 1 / i)**i, 2))
print(list)
print(sum(list))
