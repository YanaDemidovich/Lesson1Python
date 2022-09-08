# Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.

string_1 = input('Введите строку №1 ')
string_2 = input('Введите строку №2 ')
count = 0
for i in range(len(string_1)):
    # print(string_1[i:i + len(string_2)])
    if string_1[i:i + len(string_2)] == string_2:
        count += 1
print(count)

