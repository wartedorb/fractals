from turtle import *


def koch(order, size):
    '''Рисует фрактал Коха'''
    if order == 0:
        forward(size)
    else:
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)
        right(120)
        koch(order-1, size/3)
        left(60)
        koch(order-1, size/3)


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
        iced(order-1, size / 2)
        left(90)
        iced(order-1, size / 4)
        right(180)
        iced(order-1, size / 4)
        left(90)
        iced(order-1, size / 2)

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
        iced_2(order-1, size / 2)
        left(120)
        iced_2(order-1, size / 4)
        right(180)
        iced_2(order-1, size / 4)
        left(120)
        iced_2(order-1, size / 4)
        right(180)
        iced_2(order-1, size / 4)
        left(120)
        iced_2(order-1, size / 2)


def main_iced_2():
    '''Функция запроса глубины и длины (Ледяной - 2)'''
    up()
    goto(-100, 0)
    down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    iced(n, a)





done()