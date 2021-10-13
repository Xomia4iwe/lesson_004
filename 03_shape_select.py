import simple_draw as sd

sd.resolution = (800, 800)


# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

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

figure = {'1': {'Название фигуры': 'Треугольник', 'Количество граней': 3},
          '2': {'Название фигуры': 'Квадрат', 'Количество граней': 4},
          '3': {'Название фигуры': 'Пентагон', 'Количество граней': 5},
          '4': {'Название фигуры': 'Хексагон', 'Количество граней': 6}}

for number, n in figure.items():
    print(number, ' - ', n['Название фигуры'])
y = input("Введите свой номер: ")

if x in colors:
    if y in figure:
        polygon(point=sd.get_point(350, 350), length=100, n=figure[y]['Количество граней'], color=colors[x]['Цвет'])
        sd.pause()
else:
    print('Вы ввели неправильное значение. Повторите попытку!')

sd.pause()
