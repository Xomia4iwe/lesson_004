# -*- coding: utf-8 -*-

import simple_draw as sd

import random as r

sd.resolution = (1200, 600)


def snowfall(n):
    snowflakes = []

    for _ in range(n):
        snowflakes.append([r.randint(100, 1000), r.randint(550, 1600), r.randint(20, 40), r.random(), r.random(),
                           r.randint(1, 179)])

    while True:
        sd.clear_screen()
        for s in snowflakes:
            x, y, length, factor_a, factor_b, factor_c = s
            point = sd.get_point(x, y)
            sd.start_drawing()
            sd.snowflake(center=point, length=length, color=sd.background_color, factor_a=factor_a,
                         factor_b=factor_b, factor_c=factor_c)
            if y > 50:
                s[1] -= 10
                x -= sd.random_number(-25, 25)
                point_fall = sd.get_point(x, y)
                sd.snowflake(point_fall, length=length, color=sd.COLOR_WHITE, factor_a=factor_a,
                             factor_b=factor_b, factor_c=factor_c)
            else:
                last_point = sd.get_point(x, y - 1)
                sd.snowflake(last_point, length, color=sd.COLOR_WHITE, factor_a=factor_a,
                             factor_b=factor_b, factor_c=factor_c)
                y += sd.random_number(600, 800)

        sd.finish_drawing()
        sd.sleep(0.175)
        if sd.user_want_exit():
            break


snowfall(20)
