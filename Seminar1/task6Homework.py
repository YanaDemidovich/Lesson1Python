# 6. Дано число обозначающее день недели. 
# Вывести его название и указать является ли он выходным.

def f(x):
    if x == 1:
        return 'Понедельник'
    elif x == 2:
       return 'Вторник'
    elif x == 3:
        return 'Среда'
    elif x == 4:
        return 'Четверг'
    elif x == 5:
        return 'Пятница'
    elif x == 6:
        return 'Суббота'
    elif x == 7:
        return 'Воскресенье'
    else:
        return 'Такого дня нет'

def weekend(i):
    if 5 < i < 8:
        return 'выходной день'
    elif 0 < i <= 6:
        return 'рабочий день'
    else:
        return 'введите другое число'

a = int(input('Введите день недели '))
print(f(a)," - ",weekend(a))




