# Подсчитать сумму цифр в вещественном числе.


# n = int(input('Введите число '))
# sum = 0
# while n != 0:
#     p = n % 10 # выявляем последнюю цифру числа делением на 10 с остатком
#     sum += p # добавляем её в сумму
#     n = n // 10 # отсекаем последнюю цифру целочисленным делением на 10

# print(sum)

    ## ИЛИ

s = input('Введите вещественное число: ')
sum = 0
for i in s:
    if i.isdigit(): # если все символы в строке являются цифрами
        sum = sum + int(i)
print(f'Сумма цифр {sum}')


