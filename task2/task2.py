import sys, math
#функция вычисления расстояния между точками
def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if __name__ == '__main__':
    #ввод аргументов командной строки (программа запускается через консоль)
    if sys.argv and len(sys.argv)>2:
        filename1 = sys.argv[1]
        filename2 = sys.argv[2]
    else:
    #если не ввели аргументы командной строки сразу (программа запускается не из консоли)
        names = input()
        filename1, filename2 = names.split(' ')

#считываем координаты центра окружности и её радиус
    with open(filename1, 'r') as file:
        Xc, Yc = map(float, file.readline().split(' '))
        R = float(file.readline())

#смотрим точки окружности    
    with open(filename2, 'r') as file:
        for line in file:
            x0, y0 = map(float, line.split(' '))
            if dist(x0, y0, Xc, Yc) > R:
                print("2") #точка снаружи
            elif dist(x0, y0, Xc, Yc) < R:
                print("1") #точка внутри
            else: #точка лежит на окружности
                print("0")


