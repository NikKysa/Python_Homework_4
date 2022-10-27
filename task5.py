# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0


import random

def createDict():
    equation = {}
    degree = int(input('Введите максимальную степень многочлена: '))
    for i in range(degree, -1, -1):
        equation[i] = random.randint(-10,10)
    return equation


def createEquation(equation: dict):
    strEquation = ''
    first = True

    for k,v in equation.items():
        if first:
            first = False
            if v > 0:
                strEquation += f'{v}*x^{k}'
            elif v < 0:
                strEquation += f'-{abs(v)}*x^{k}'    # v взять по модулю abs
        else:
            if v > 0:
                strEquation += f' + {v}*x^{k}'
            elif v < 0:
                strEquation += f' - {abs(v)}*x^{k}'

    return strEquation

def printEquation(equation: str):
    print(equation.replace('*x^1', 'x').replace('*x^0', '') + ' = 0')


def parseEquation(equation: str):
    eqDict = {}
    equation = equation.replace(' + ', ' ').replace(' - ', ' -')
    equation = equation.split()


    for i in equation:
        element = i.split('*x^')
        eqDict[int(element[1])] = int(element[0])
    
    return eqDict


def summEquation(equation1: dict, equation2: dict):
    finalEquation = {}

    for i in range(max(len(equation1), len(equation2)), -1, -1):
        if equation1.get(i) or equation2.get(i):
            finalEquation[i] = (equation1.get(i) if equation1.get(i) else 0) + (equation2.get(i) if equation2.get(i) else 0)
    return finalEquation

equation1 = createDict()
equation2 = createDict()

finalEquation = summEquation(equation1, equation2)

printEquation(createEquation(equation1))
printEquation(createEquation(equation2))
printEquation(createEquation(finalEquation))