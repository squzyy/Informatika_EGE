"""
from math import dist
# Решение для файла A
# Кластеризация
cl1 = []
cl2 = []
for i in open('27.txt'):
    x, y = [float(j) for j in i.split()]
    # сам должен в файле, по диаграмме определить
    if y < 3: cl1.append([x, y])
    if y > 3: cl2.append([x, y])


# поиск центральной точки
def center(cl):
    mn = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        mn.append(s)
    return min(mn)[-1]

x1, y1 = center(cl1)
x2, y2 = center(cl2)
# средне арифметическое:
Px = (x1 + x2) / 2
Py = (y1 + y2) / 2
print(int(Px * 10_000), int(Py * 10_000))
# Решение для файла B
# Кластеризация
cl1 = []
cl2 = []
cl3 = []
for i in open('27.txt'):
    x, y = [float(j) for j in i.split()]
    # сам должен в файле, по диаграмме определить
    if y < 3: cl1.append([x, y])
    if 3 < y < 7: cl2.append([x, y])
    if y > 7: cl3.append([x, y])


# поиск центральной точки
def center(cl):
    mn = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        mn.append(s)
    return min(mn)[-1] # Центер это минимум суммы до всех точек

x1, y1 = center(cl1)
x2, y2 = center(cl2)
x3, y3 = center(cl3)
# средне арифметическое:
Px = (x1 + x2 + x3) / 3
Py = (y1 + y2 + y3) / 3
print(int(Px * 10_000), int(Py * 10_000))
"""
"""from math import dist
# Автоматическая кластеризация
# Часть A:
data = []
for i in open('27.txt'):
    x, y = [float(j) for j in i.replace(',', '.').split()]
    data.append([x, y])

clasters = []
while len(data) != 0:
    clasters.append([data.pop(0)]) #удаляет первую координату и записывает ее
    for p in clasters[-1]:
        sosedi = [p1 for p1 in data if dist(p, p1) < 1] # <1 можно играться с числом
        clasters[-1] += sosedi # списки можно соединять
        for p1 in sosedi: data.remove(p1) # остальные точки будут удалятся чтобы не проходиться по ним опять


def center(cl):
    mn = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        mn.append([s, p1])
    return min(mn)[-1]

cl1 = clasters[0]
cl2 = clasters[1]
x1, y1 = center(cl1)
x2, y2 = center(cl2)
Px = max(x1, x2)
Py = max(y1, y2)
print(int(Px * 10_000), int(Py * 10_000))

# Часть B c аномалиями, для них нужна автоматическая кластеризация:
from math import dist
# Автоматическая кластеризация
data = []
for i in open('27.txt'):
    x, y = [float(j) for j in i.replace(',', '.').split()]
    data.append([x, y])

clasters = []
while len(data) != 0:
    clasters.append([data.pop(0)]) #удаляет первую координату и записывает ее
    for p in clasters[-1]:
        sosedi = [p1 for p1 in data if dist(p, p1) < 1] # <1 можно играться с числом
        clasters[-1] += sosedi # списки можно соединять
        for p1 in sosedi: data.remove(p1) # остальные точки будут удалятся чтобы не проходиться по ним опять
    if len(clasters[-1]) == 1: # если длина аномалия кластера = 1
        clasters.remove(clasters[-1])


def center(cl):
    mn = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        mn.append([s, p1])
    return min(mn)[-1]

cl1 = clasters[0]
cl2 = clasters[1]
cl3 = clasters[2]
# Второй лишний т.к. наименьший и наиб. нужен
x1, y1 = center(cl1)
x3, y3 = center(cl3)
Qx = (x1 - x3)
Qy = (y1 - y3)
print(int(Qx * 10_000), int(Qy * 10_000))"""

"""from math import dist
data = []
for i in open('27_А.txt'):
    x, y = [float(j) for j in i.split()]
    data.append([x, y])

clasters = []
while len(data) != 0:
    clasters.append([data.pop(0)])
    for p in clasters[-1]:
        sosed = [p1 for p1 in data if dist(p, p1) < 1]
        clasters[-1] += sosed
        for p1 in sosed: data.remove(p1)

def center(cl):
    mn = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        mn.append([s, p1])
    return min(mn)[-1]

cl1 = clasters[0]
cl2 = clasters[1]
a1 = min(len(cl1), len(cl2))
center1 = center(cl1)
center2 = center(cl2)
point = (8.0, 4.5)
a2 = dist(center1, point) + dist(center2, point)
print(a1, int(a2 * 10_000))"""


from math import dist
data = []
for i in open('27_А.txt'):
    x, y = [float(j) for j in i.replace(',', '.').split()]
    data.append([x, y])
cl = []
while len(data) != 0:
    cl.append([data.pop(0)])
    for p in cl[-1]:
        sos = [p1 for p1 in data if dist(p, p1) < 1]
        cl[-1] += sos
        for p1 in sos:
            data.remove(p1)

def center(cl):
    mn = []
    for p1 in cl:
        s = sum(dist(p1, p2) for p2 in cl)
        mn.append([s, p1])
    return max(mn)[-1]

clas1 = cl[0]
clas2 = cl[1]
x1, y1 = center(clas1)
x2, y2 = center(clas2)
p1 = (x1 + x2)


