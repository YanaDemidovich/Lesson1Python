# Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в списке positions - создайте этот список (например: positions = [1, 3, 6]).

n = int(input('Введите число: '))
list = []
for i in range(-n, n+1):
    list.append(i)
print(list)

def get_mult(list, positions):
    mult = 1
    for i in positions:
        mult *= list[i]
    return mult

positions = [1, 3, 6]
print(get_mult(list, positions))

# Как создавать списки в txt и обращаться к ним ни на лекциях, ни на семинарах не было.