# Найти максимальное из пяти чисел.

list = [5, 6, 10, 8, 9]
max = list[0]
for i in list:
    if i >= max:
        max = i
else:
    print(max)


