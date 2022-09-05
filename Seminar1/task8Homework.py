# Сообщить в какой четверти координатной плоскости 
# или на какой оси находится точка с координатами Х и У.

def f(x, y):
    if x > 0 and y > 0:
        return 'I'
    elif x < 0 and y > 0:
        return 'II'
    elif x < 0 and y < 0:
        return 'III'
    elif x > 0 and y < 0:
        return 'IV'

x = int(input('х = '))
y = int(input('y = '))
print(f(x, y), 'четверть')



