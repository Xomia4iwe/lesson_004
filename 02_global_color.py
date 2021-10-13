import simple_draw as sd

sd.resolution = (800, 800)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

def polygon(point, length, n, color=sd.COLOR_YELLOW, angle=0):
    for _ in range(n):
        v = sd.get_vector(start_point=point, length=length, angle=angle, width=3)
        v.draw(color=color)
        angle = angle + (180 - (n - 2) * 180 / n)
        point = v.end_point


colors = {'1': {'Название цвета': 'Красный', 'Цвет': sd.COLOR_RED},
          '2': {'Название цвета': 'Оранжевый', 'Цвет': sd.COLOR_ORANGE},
          '3': {'Название цвета': 'Жёлтый', 'Цвет': sd.COLOR_YELLOW},
          '4': {'Название цвета': 'Зелёный', 'Цвет': sd.COLOR_GREEN},
          '5': {'Название цвета': 'Циан', 'Цвет': sd.COLOR_CYAN},
          '6': {'Название цвета': 'Синий', 'Цвет': sd.COLOR_BLUE},
          '7': {'Название цвета': 'Фиолетовый', 'Цвет': sd.COLOR_PURPLE}}

for number, color in colors.items():
    print(number, ' - ', color['Название цвета'])

x = input("Введите свой номер: ")

if x in colors:
    polygon(point=sd.get_point(100, 150), length=200, n=3, color=colors[x]['Цвет'])
    polygon(point=sd.get_point(500, 150), length=150, n=4, color=colors[x]['Цвет'])
    polygon(point=sd.get_point(100, 400), length=100, n=5, color=colors[x]['Цвет'])
    polygon(point=sd.get_point(500, 400), length=100, n=6, color=colors[x]['Цвет'])

    sd.pause()
else:
    print('Вы ввели неправильное значение. Повторите попытку!')

sd.pause()
