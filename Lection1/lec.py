# print('hello world')

# value = None
# print(type(value))

# value = 12334
# print(type(value))

# a = 123
# b = 1.23
# print(type(a))
# print(type(b))

# s = '"Привет \'мир"'
# print(s) # комментарии через решетку
# print(a,' - ', b,' - ', s)
# print('{} - {} - {}'.format(a, b, s)) # формат
# print('{2} - {0} - {1}'.format(a, b, s)) # формат через индекс
# print(f'{a} - {s} - {b}') # интерполяция

# f = False
# print(f)
# list = [1, 2, 3, 'hello']
# print(list)

# Ввод (input), вывод (print) данных

# print('Введите а')
# a = input()
# print('Введите b')
# b = input()
# print(a, b) # вывод №1
# print('{} {}'.format(a, b)) # вывод №2
# print(f'{a} {b}') # вывод №3

# Если захотим произвести какое-то вычисление, то
# необходимо определить тип принимаемого на вход данного
# print('Введите а')
# a = int(input()) # int для целых чисел
# print('Введите b')
# b = int(input())
# print(a,' + ', b, ' = ', a+b)

# print('Введите а')
# a = float(input()) # float для вещественных чисел (с плавающей запятой)
# print('Введите b')
# b = float(input())
# print(a,' + ', b, ' = ', a+b)

# Арифметические операции

# a = 1.3123255
# b = 3
# c = round(a * b, 9)
# print(c)

# a = 3
# a = a + 5
# print(a)
            # либо
# a = 3
# a += 5
# print(a)

# Логические операции

# a = 1 != 2 # != не равно
# print(a)

# f = 1 > 2 or 4 < 3
# print(f)

    ## if - else ##
# a = int(input('Введите а '))
# b = int(input('Введите b '))
# if a > b:
#     print(a)
# else:
#     print(b)

    ## if - elif ##
# username = input('Введите имя ')
# if username == 'Маша':
#     print('Привет, Маша!')
# elif username == 'Марина':
#     print('Привет, Марина!')
# elif username == 'Яна':
#     print('Привет, Яна!')
# else:
#     print('Неужели это', username)


## ЦИКЛЫ
# УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ WHILE

# original = 23
# inverted = 0
# while original !=0: # до тех пор пока
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

        # либо

# original = 23
# inverted = 0
# while original !=0: # до тех пор пока
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй хватит')
# print(inverted)

# УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ FOR

# for i in 1, 2, 3, 4:
#     print(i**2)

        # либо
# list = [1, 2, 3, 4]
# for i in list:
#     print(i**2)


# list = range(10) # range - ранжированный набор от 0 до 10
# for i in list:
#     print(i)

        # либо

# for i in range(8): # ранжированный набор от 0 до 8
#     print(i)

        # либо

# for i in range(1, 8): # ранжированный набор от 1 до 8 (указываем диапазон)
#     print(i)

        # либо

# for i in range(1, 8, 2): # ранжированный набор от 1 до 8 (указываем диапазон) с шагом в 2 единицы
#     print(i)

        # либо

# for i in 'слово': # ранжированный набор символов по порядку
#     print(i)

## СТРОКИ

# text = 'съешь ещё этих мягких французских булок'
# print(len(text))  # определяет кол-во символов в строке
# print('еще' in text)  # проверяет наличие нужных символов (подстроки) в заданной строке
# print(text.isdigit())
# print(text.islower())
# print(text.replace('еще','ЕЩЕ'))
# print(text[0:4])  # показывает первые 4 сивола


## ФУНКЦИИ
# def - определяет фукцию

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 1
    else:
        return

arg = 2.3
print(f(arg))
print(type(f(arg)))


