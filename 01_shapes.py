# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 1000)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# def triangle(point, length, angle=0):
#     for _ in range(3):
#         v = sd.get_vector(start_point=point, length=length, angle=angle, width=3)
#         v.draw()
#         angle += 120
#         point = v.end_point
# point_0 = sd.get_point(300, 300)
# length = 100
# triangle(point=point_0, length=length)
#
# def square(point, length, angle=0):
#     for _ in range(4):
#         v = sd.get_vector(start_point=point, length=length, angle=angle, width=3)
#         v.draw()
#         angle += 90
#         point = v.end_point
#
# point_1 = sd.get_point(100, 100)
# length_1 = 150
# square(point=point_1, length=length_1)
#
#
def polygon(point, length, n, angle=0):
    for _ in range(n):
        v = sd.get_vector(start_point=point, length=length, angle=angle, width=3)
        v.draw()
        angle = angle + (180 - (n - 2) * 180 / n)
        point = v.end_point
#
#
# point_p = sd.get_point(200, 200)
# length_p = 100
# np = 6
# polygon(point=point_p, length=length_p, n=np)
# polygon(point=sd.get_point(400, 400), length=50, n=4)
for angle in range(0, 361, 10):
    polygon(point=sd.get_point(500, 500), length=200, n=4, angle=angle)




# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
