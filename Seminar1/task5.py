# Дано число. 
# Проверить кратно ли оно 5 и 10
# или 15, но не 30.


a = int(input('Введите число '))
if a % 30 == 0:
    print('не ok')
elif a % 5 == 0 and a % 10 == 0 or a % 15 == 0:
    print('ok')
else:
    print('не ok')


# или

# if (a % 30 !=0):
#     if ((a % 5 == 0 and a % 10 == 0) or a % 15 ==0): 
#         print('ok')
# else: print('не ok')
