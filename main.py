"""
Case - study: Fractals
Devs:
    M.Kondrashov - 50 %
    E.Bikmetov - 30%
    K.Bychkov - 30%
"""

from turtle import *
from math import sqrt

speed(100000000000000000000)


def koch(order, size):
    """Рисует фрактал Коха"""
    if order == 0:
        forward(size)
    else:
        koch(order - 1, size / 3)
        left(60)
        koch(order - 1, size / 3)
        right(120)
        koch(order - 1, size / 3)
        left(60)
        koch(order - 1, size / 3)


def main_koch():
    """Функция запроса глубины и длины (Кох)"""
    try:
        up()
        goto(-100, 0)
        down()
        n = int(input('Глубина рекурсии:'))
        a = int(input('Длина стороны:'))
        koch(n, a)
    except ValueError:
        print('Введите целое число')
        main_koch()


def iced(order, size):
    """Рисует "ледяной" фрактал"""
    if order == 0:
        forward(size)
    else:
        iced(order - 1, size / 2)
        left(90)
        iced(order - 1, size / 4)
        right(180)
        iced(order - 1, size / 4)
        left(90)
        iced(order - 1, size / 2)


def main_iced():
    """Функция запроса глубины и длины (Ледяной)"""
    try:
        up()
        goto(-100, 0)
        down()
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        iced(n, a)
    except ValueError:
        print('Введите целое число')
        main_iced()


def iced_2(order, size):
    """Рисует "ледяной" фрактал - 2"""
    if order == 0:
        forward(size)
    else:
        iced_2(order - 1, size / 2)
        left(120)
        iced_2(order - 1, size / 4)
        right(180)
        iced_2(order - 1, size / 4)
        left(120)
        iced_2(order - 1, size / 4)
        right(180)
        iced_2(order - 1, size / 4)
        left(120)
        iced_2(order - 1, size / 2)


def main_iced_2():
    """Функция запроса глубины и длины (Ледяной - 2)"""
    try:
        up()
        goto(-100, 0)
        down()
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        iced_2(n, a)
    except ValueError:
        print('Введите целое число')
        main_iced_2()


def koch_snowflake(order, size):
    """Фрактал снежинка Коха"""
    if order == 0:
        koch(order, size)
        right(120)
        koch(order, size)
        right(120)
        koch(order, size)
        right(120)
    else:
        for i in range(6):
            koch(order - 1, size / 3)
            left(60)
            koch(order - 1, size / 3)
            right(120)


def main_koch_snowflake():
    """Функция запроса глубины рекурсии и длины ( Снежинка Коха )"""
    try:
        up()
        goto(-100, 0)
        down()
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        koch_snowflake(n, a)
    except ValueError:
        print('Введите целое число')
        main_koch_snowflake()


def minkovsky(order, size):
    if order == 0:
        forward(size)
    else:
        minkovsky(order - 1, size / 4)
        left(90)
        minkovsky(order - 1, size / 4)
        right(90)
        minkovsky(order - 1, size / 4)
        right(90)
        minkovsky(order - 1, size / 4)
        minkovsky(order - 1, size / 4)
        left(90)
        minkovsky(order - 1, size / 4)
        left(90)
        minkovsky(order - 1, size / 4)
        right(90)
        minkovsky(order - 1, size / 4)


def main_minkovsky():
    """Функция запроса глубины рекурсии и длины ( Минковский )"""
    try:
        up()
        goto(-100, 0)
        down()
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        minkovsky(n, a)
    except ValueError:
        print('Введите целое число')
        main_minkovsky()


def levi(order, size):
    if order == 0:
        forward(size)
    else:
        left(45)
        levi(order - 1, sqrt(2 * (size / 2) ** 2))
        right(90)
        levi(order - 1, sqrt(2 * (size / 2) ** 2))
        left(45)


def main_levi():
    """Функция запроса глубины рекурсии и длины ( Минковский )"""
    try:
        up()
        goto(-100, 0)
        down()
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        levi(n, a)
    except ValueError:
        print('Введите целое число')
        main_levi()


def s(size):
    """Расчет стороны для дракона"""
    return sqrt((size ** 2 / 2))


def dragon(order, size, a='l'):
    """Фрактал дракон"""
    if order == 0:
        forward(size)
    else:
        if a == 'l':
            left(45)
        else:
            right(45)
        dragon(order - 1, s(size), a='l')
        if a == 'l':
            right(90)
        else:
            left(90)
        dragon(order - 1, s(size), a='r')
        if a == 'l':
            left(45)
        else:
            right(45)


def main_dragon():
    """Фрактал - дракон запрос глубины и стороны"""
    try:
        up()
        goto(-100, 0)
        down()
        n = int(input('Глубина рекурсии: '))
        a = int(input('Длина стороны: '))
        dragon(n, a)
    except ValueError:
        print('Введите целое число')
        main_dragon()


def binar_tree(angl, h, size=100):
    """Фрактал бинарное дерево"""
    if h == 0:
        return

    fd(size)
    left(angl)
    binar_tree(angl, h - 1, int(size / 1.5))
    left(-2 * angl)
    binar_tree(angl, h - 1, int(size / 1.5))
    left(angl)
    fd(-size)


def main_binar_tree():
    """Запрос переменных для бинарного дерева"""
    try:
        up()
        goto(-100, 0)
        left(90)
        down()
        angl = int(input('Введите угол наклона: '))
        h = int(input('Введите высоту дерева (в изломах): '))
        binar_tree(angl, h)
    except ValueError:
        print('Введите целое число')
        main_binar_tree()

def branch(n, size):
    """Фрактал Ветка"""
    if n == 0:
        left(180)
        return

    x = size/(n+1)
    for i in range(n):
        forward(x)
        left(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        left(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        right(135)

    forward(x)
    left(180)
    forward(size)

def main_brach():
    """Запрос параметров для фрактала ветка"""
    try:
        n = int(input('Введите глубину рекурсии: '))
        size = int(input("Введите размер: "))
        left(90)
        branch(n, size)
    except ValueError:
        print('Введите целое число')
        main_brach()

def fractal_asking():
    """Запрос фрактала"""
    while True:
        try:
            fractal = int(input('Фракталы:\n1 - Коха\n2 - Снежинка Коха\n'
                                '3 - Ледяной\n4 - Ледяной (2)\n5 - Минковского\n6 - Леви\n7 - Дракон Хартера-Хейтуэя\n'
                                '8 - Бинарное дерево\n9 - Ветка\n'
                                'Напишите номер фрактала, который хотите увидеть: '))
            return fractal
        except ValueError:
            print('Введите целое число')


def main_of_mains(fractal):
    """Запуск фрактала"""
    if fractal == 1:
        main_koch()
    elif fractal == 2:
        main_koch_snowflake()
    elif fractal == 3:
        main_iced()
    elif fractal == 4:
        main_iced_2()
    elif fractal == 5:
        main_minkovsky()
    elif fractal == 6:
        main_levi()
    elif fractal == 7:
        main_dragon()
    elif fractal == 8:
        main_binar_tree()
    elif fractal == 9:
        main_brach()
    else:
        print('Такого фрактала нет.')
        fractal = fractal_asking()
        main_of_mains(fractal)


num = fractal_asking()
main_of_mains(num)
hideturtle()
done()
