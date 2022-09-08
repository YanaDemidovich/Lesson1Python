# 7. Проверить истинность утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# где ¬ означает not (отрицание "не")
# ⋁ означает or - "или"
# ⋀ означает and - "и"
# для всех значений предикат.

# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# варианты для перебора 0 и 1


for x in range(2): # range(2) - это ранжированные по порядку цифры от 0 до 2
    for y in range(2):
        for z in range(2):
            print(f'x = {x}', f'y = {y}', f'z = {z}')
            print(not (x or y or y or z) == (not x and not y and not z))


