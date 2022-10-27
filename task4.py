# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше 
# и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем 
# данную итерацию степени
# Записываем результат в файл.

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0


from random import randint
import itertools

k = int(input('Задайте натуральную степень k: '))
koeffs_lst = []

koeffs_list = list([randint(0, 101) for i in range(k+1)])
if koeffs_list[0] == 0:
    koeffs_list[0] = randint(1, 101)
print(f' Список коэффициентов: {koeffs_list}')

def get_polynomial(k, koeffs_list): 
    str1 = ['*x**']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c  in itertools.zip_longest(koeffs_list, str1, range(k, 1, -1), fillvalue = '') if a !=0]

    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))

    polynomial[-1] = ' = 0' 
    return "".join(map(str, polynomial)).replace(' 1*x',' x')

list = get_polynomial(k, koeffs_list)
print(list)

with open('Poly.txt', 'w') as data:
    data.write(list)