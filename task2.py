# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума). 
# Список можно задавать рандомно

# На входе : [ 1, 5, 88, 100, 2, -4]
# 33
# 200
# Ответ: [2, 3]

import random

n = int(input("Введите размер массива: "))
min = int(input("Введите нижний диапазон: "))
max = int(input("Введите верхний диапазон: "))
array1 = [random.randint(0,15) for _ in range(n)]
array2 = []

def find_index(array1):
    for i in range(n):
        if min <= array1[i] <= max:
            array2.append(i)
    return array2

print(array1)
print(find_index(array1))