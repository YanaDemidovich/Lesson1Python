# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в списке positions - создайте этот список (например: positions = [1, 3, 6]).

# n = int(input('Введите число: '))
# list = []
# for i in range(-n, n+1):
#     list.append(i)
# print(list)

# def get_mult(list, positions):
#     mult = 1
#     for i in positions:
#         mult *= list[i]
#     return mult

# positions = [1, 3, 6]
# print(get_mult(list, positions))

# Как создавать списки в txt и обращаться к ним ни на лекциях, ни на семинарах не было.

n = int(input('Введите число: '))
l = '' # '1, 3, 5, 7'
s = 0
c = 1
l1 = []
for i in range(-n, n+1):
    l1.append(i)
with open('./Seminar2/list.txt', 'r') as f:
    l = f.readline()
l2 = l.split(',')
print(l)
print(l1)
print(l2)
for i in l2:
    print(l1[int(i.strip())])
    c = c * l1[int(i.strip())]
print(c)

