# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (800, 800)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,
# def draw_branches(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length)
#     v1.draw()
#     v2 = sd.get_vector(start_point=point, angle=(180 - angle), length=length)
#     v2.draw()
#     return v1.end_point, v2.end_point
#
#
# point = sd.get_point(400, 0)
#
# draw_branches(point=point, angle=60, length=150)


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# def draw_branches(point, angle, length, width=3, delta=30):
#     if length < 10:
#         return
#     vector = sd.Vector(point, angle, length, width)
#     vector.draw()
#     draw_branches(vector.end_point, angle - delta, length * 0.75, width)
#     draw_branches(vector.end_point, angle + delta, length * 0.75, width)
#
#
#
#
# start_point = sd.get_point(400, 0)
# draw_branches(point=start_point, angle=90, length=150)

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def draw_branches(point, angle, length, width=3, delta=30):
    if length < 10:
        return
    vector = sd.Vector(point, angle, length, width)
    vector.draw()

    draw_branches(vector.end_point, angle - delta, length * 0.75, width)
    draw_branches(vector.end_point, angle + delta, length * 0.75, width)


start_point = sd.get_point(400, 0)
# draw_branches(point=start_point, angle=30, length=50)
# draw_branches(point=start_point, angle=45, length=100)
draw_branches(point=start_point, angle=90, length=150)

sd.pause()
