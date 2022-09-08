# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

n = int(input('Введите число '))
list = []
current = 1
for i in range(1, n+1):
    current *= i
    list.append(current)
print(list)

