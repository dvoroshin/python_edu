x1 = int(input('Введите координату Х первой точки: '))
y1 = int(input('Введите координату Y первой точки: '))
x2 = int(input('Введите координату Х второй точки: '))
y2 = int(input('Введите координату Y второй точки: '))

result = pow((x2-x1)**2 + (y2-y1)**2, 0.5)

print(round(result, 2))
