'''
Case - study: Fractals
Devs:
    M.Kondrashov - 40 %
    E.Bikmetov -
    K.Bychkov -
'''


from turtle import *
from math import sqrt
speed(100000000000000000000)


def koch(order, size):
    '''Рисует фрактал Коха'''
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
    '''Функция запроса глубины и длины (Кох)'''
    up()
    goto(-100, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch(n, a)


def iced(order, size):
    '''Рисует "ледяной" фрактал'''
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
    '''Функция запроса глубины и длины (Ледяной)'''
    up()
    goto(-100, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    iced(n, a)


def iced_2(order, size):
    '''Рисует "ледяной" фрактал - 2'''
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
    '''Функция запроса глубины и длины (Ледяной - 2)'''
    up()
    goto(-100, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    iced(n, a)


def koch_snowflake(order, size):
    '''Фрактал снежинка Коха'''
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
    '''Функция запроса глубины рекурсии и длины ( Снежинка Коха )'''
    up()
    goto(-100, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch_snowflake(n, a)


def minkovsky(order, size):
    if order == 0:
        forward(size)
    else:
        minkovsky(order-1, size/4)
        left(90)
        minkovsky(order-1, size/4)
        right(90)
        minkovsky(order-1, size/4)
        right(90)
        minkovsky(order-1, size/4)
        minkovsky(order - 1, size / 4)
        left(90)
        minkovsky(order - 1, size / 4)
        left(90)
        minkovsky(order - 1, size / 4)
        right(90)
        minkovsky(order - 1, size / 4)


def main_minkovsky():
    '''Функция запроса глубины рекурсии и длины ( Минковский )'''
    up()
    goto(-100, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    minkovsky(n, a)


def levi(order, size):
    if order == 0:
        forward(size)
    else:
        left(45)
        levi(order-1, sqrt(2*(size/2)**2))
        right(90)
        levi(order - 1, sqrt(2 * (size / 2) ** 2))
        left(45)


def main_levi():
    '''Функция запроса глубины рекурсии и длины ( Минковский )'''
    up()
    goto(-100, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    levi(n, a)


def fractal_asking():
    while True:
        try:
            fractal = int(input('Фракталы:\n1- Коха\n2 - Снежинка Коха\n'
                                '3 - Ледяной\n4 - Ледяной (2)\n5 - Минковского\n6 - Леви\n'
                                'Напишите номер фрактала, который хотите увидеть: '))
            return fractal
        except ValueError:
            print('Введите целое число')


def main_of_mains(fractal):
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
    else:
        print('Такого фрактала нет.')
        fractal = fractal_asking()
        main_of_mains(fractal)


num = fractal_asking()
main_of_mains(num)
#hideturtle()
done()
