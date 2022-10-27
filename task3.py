# Задайте последовательность цифр. Напишите программу, которая выведет 
# список неповторяющихся элементов
# исходной последовательности.

# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []


n = int(input('Укажите размер списка: '))
min = int(input('Введите минимальное значение диапазона: '))
max = int(input('Введите максимальное значение диапазона: '))
my_list = []
occurrences = []
final_list = []

import random
for i in range(n):
    my_list.append(random.randint(min, max))
print(f'Исходный список: {my_list}')

for item in my_list :
    count = 0
    for x in my_list :
        if x == item :
            count += 1
    occurrences.append(count)
final_list = set()
index = 0
while index < len(my_list) :
    if occurrences[index] == 1 :
        final_list.add(my_list[index])
    index += 1
print(final_list)