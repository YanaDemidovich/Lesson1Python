# Напишите программу, 
# которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y)

def f(x):
    if x == 1:
        return 'х > 0, y > 0'
    elif x == 2:
        return 'х < 0, y > 0'
    elif x == 3:
        return 'х < 0, y < 0'
    elif x == 4:
        return 'х > 0, y < 0'
    else:
        return 'не существует'

a = int(input('Введите номер четверти '))
print('в четверти', a, 'диапазон возможных координат', f(a))