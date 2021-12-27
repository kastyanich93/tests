import sys

#Вычисляем целевое значение
# Функция для вычисления среднего значения с округлением в меньшую сторону
def goal(data):
    m = 0
    for element in data:
        m += element
    n = len(data)
    m //= n
    return m 


if __name__ == '__main__':
    if sys.argv and len(sys.argv) > 1:
        # Если программа запускается из консоли
        file_name = sys.argv[1]  # имя файла с данными
    else:
        # Если программа запускается не из консоли
        file_name = input()  # имя файла с данными
    data = []
    with open(file_name, 'r') as file:
        for line in file:
            data.append(int(line))
    avg = goal(data)
    #print(avg)
    ans = 0
    #пробегаемся по массиву, для каждого элемента считаем разницу между
    #самим элементом и целевым значением, а потом суммируем эти разницы
    for i in range(0, len(data)):
        ans += abs(data[i]-avg)
    print(ans)
    