# Поезд в пути следования останавливается на N станциях (станция 1 - начальная, N - конечная).
# Дан список пассажиров, для каждого известна первая и конечная станция.
# Определить между какими станциями(перегонами) в поезде было наибольшее кол-во людей.
#
# Первая строка файла содержит кол-во станций N, следующие - информацию о пассажирах в формате:
#   Фамилия Имя станция_посадки станция_выхода
#   (ФИ - строки до 20 символов, станции - числа от 1 до N)
#   При этом номер станции посадки меньше, чем номер станции выхода
#
# Ответ - список перегонов, с максимальным числом людей. Ответ в формате станция-станция
#
# ex
# 5
# Иванов Сергей 1 5
# Сергеев Петр 3 5
# Петров Кирилл 1 2
#
# 1-2
# 3-4
# 4-5

def CheckingConditions(beg, end):
    if (end > N):
        print("Station number is greater than possible")
        return False
    if (beg >= end):
        print("The number of the final station is greater than the starting station")
        return False
    return True


f = open('text.txt', 'r')
N = int(f.read(2))
counterPass = [0 for i in range(N - 1)]
for line in f:
    beg, end = map(int, list(line.split())[2:4])
    if (CheckingConditions(beg, end)):
        for i in range(beg - 1, end - 1):
            counterPass[i] += 1

maxCount = max(counterPass)
for i in range(N - 1):
    if (counterPass[i] == maxCount):
        print(f"{i + 1}-{i + 2}")