# Реализовать алгоритм перемешивания списка.

from random import randint

import random as rand

l1 = []
l2 = []
n = int(input('Укажите размер списка: '))
for i in range(n):
    l1.append(rand.randint(0, 50))
print(l1)
for i in range(n):
    e = rand.randint(0, len(l1)-1)
    # print(e)
    e2 = l1.pop(e)
    l2.append(e2)
print(l2)