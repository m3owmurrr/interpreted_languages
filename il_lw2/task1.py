# Для снеговика нужно три снежных кома разного размера. Есть n комов с радиусами r1, r2, .., rn.
# Снеговика можно слепить из любых трех комов, радиусы которых попарно различны.
# 1, 2, 3 подходят для снеговика; 2, 2, 3 или 2, 2, 2 - не подходят.
# Определите наибольшее кол-во, которых можно слепить из данных комов.
#
# В первой строке вводится кол-во шаров (от 1 до 105)
# В следующей вводятся радиусы комов (от 1 до 109)(могут повторятся)
#
# В первой строке вывести наибольшее кол-во снеговиков, в следующих - тройки радиусов комов для этих снеговиков
#
# ex
# 7
# 1 2 3 4 5 6 7
#
# 2
# 3 2 1
# 6 5 4


cFS = 3 #clodsForSnowman
def DifferentInPairs(arr):
    for i in range(cFS-1):
        for j in range(i+1, cFS):
            if(arr[i] == arr[j]):
                return False
    return True
def InRange(n, arr):
    if (len(arr) != n):
        print("The number of coms is more or less than specified")
        return False
    if (n < 1 or  n > 105):
        print("The number of clods is greater or less than possible")
        return False
    for elem in arr:
        if (elem < 1 or elem > 109):
            print("The radius of the clod is more or less than expected")
            return False
    return True

numOfСlods = int(input())
clods = list(map(int, input().split()))
if (InRange(numOfСlods, clods)):
    clodsCounter = {}
    for elem in clods:
        clodsCounter.setdefault(elem, 0)
        clodsCounter[elem] += 1
    answ = []
    answCounter = 0
    keysArr = list(clodsCounter.keys())
    while (numOfСlods >= cFS and len(clodsCounter) >= cFS):
        triad = []

        for i in range(cFS):
            triad.append(keysArr[i])
        if(DifferentInPairs(triad)):
            answ.append(triad[::-1])
            numOfСlods -= 3
            for elem in triad:
                clodsCounter[elem] -= 1
            answCounter += 1

        for elem in keysArr:
            if(clodsCounter[elem] == 0):
                clodsCounter.pop(elem)
        keysArr = list(clodsCounter.keys())

    print(answCounter)
    print(answ)