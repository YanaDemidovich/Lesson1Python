# Задать список из n чисел последовательности (1 + 1/n)^n 
# и вывести на экран их сумму

# n = int(input('Введите число: '))
# list = []
# for i in range(1, n+1):
#     list.append(round((1 + 1 / i)**i, 2))
# print(list)
# print(sum(list))

# или

n = int(input('Введите число: '))
s = 0
d = {}
summ = 0
for i in range(1, n+1):
    s = (1+1/i)**i
    d[i] = s
    summ +=s
    print(s)
print(d)
print(summ)