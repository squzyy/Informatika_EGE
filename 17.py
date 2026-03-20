#abs - модуль, нужен например для поиска остатков от отрицательных чисел  т.к. -17 % 10 в питоне будет 3 а не 7 поэто нужно pirnt(abs(-17) % 10)

"""
В файле содержится последовательность целых чисел. Элементы
последовательности могут принимать целые значения от -10 ОО0 до 10 ООО
включительно. Определите и запишите в ответе сначала количество пар
элементов последовательности, в которых хотя бы одно число делится на 3,
затем максимальную из сумм элементов таких пар. В данной задаче под парой
подразумевается два идущих подряд элемента последовательности.
Например, для последовательности из пяти элементов: 6; 2; 9; -3; 6 - ответ: 4 11

Например, для последовательности из пяти элементов: 6; 2; 9; -3; 6 - ответ: 4 11:
a = [6, 2, 9, -3, 6] 

otv = []

for i in range(len(a) - 1):
    if ((a[i] % 3 == 0) + (a[i+1] % 3 == 0)) > 0:
        otv.append(a[i] + a[i+1])
print(len(otv), max(otv))
"""
#1
"""
a = []

for i in open('17.txt'):
    a.append(int(i))

otv = []

for i in range(len(a) - 1):
    if ((a[i] % 3 == 0) + (a[i+1] % 3 == 0)) > 0:
        otv.append(a[i] + a[i+1])
print(len(otv), max(otv))
"""
#2
"""a = []

for i in open('17.txt'):
    a.append(int(i))

mn = min(a)

otv = []

for i in range(len(a) - 1):
    if ((a[i] % 111 == mn) + (a[i+1] % 111 == mn)) > 0:
        otv.append(a[i] + a[i+1])
print(len(otv), min(otv))"""
#3
"""a = []

for i in open('17.txt'):
    a.append(int(i))


mn = min([i for i in a if i % 21 == 0]) # Определите количество пар последовательности, в которых хотя бы одно числоделится на минимальный элемент последовательности, кратный 21.

otv = []

for i in range(len(a) - 1):
    if ((a[i] % mn == 0) + (a[i+1] % mn == 0)) > 0:
        otv.append(a[i] + a[i+1])
print(len(otv), max(otv))"""
#4
"""
В файле содержится последовательность натуральных чисел. Её элементы могу
принимать целые значения от 1 до 100 ООО включительно. Определите
количество пар последовательности, в которых только один из элементов
является трёхзначным числом, а сумма элементов пары кратна минимальному
трёхзначному элементу последовательности, оканчивающемуся на 7.
В ответе запишите количество найденных пар, затем минимальную из сумм
элементов таких пар. В данной задаче под парой подразумевается два идущих
подряд элемента последовательности.
a = []

for i in open('17.txt'):
    a.append(int(i))

mn = min([i for i in a if 99 < i < 1000 and i % 10 == 7]) # трехзначные числа и оканчивается на 7

otv = []

for i in range(len(a) - 1):
    if ((99 < a[i] < 1000) + (99 < a[i+1] < 1000)) == 1: # один элемент последовательности
        if (a[i] + a[i+1]) % mn == 0:
            otv.append(a[i] + a[i+1])
print(len(otv), min(otv))
"""

#5
"""
В файле содержится последовательность целых чисел. Её элементы могут
принимать целые значения от-100 ООО до 100 ООО включительно. Определите
количество троек элементов последовательности, в которых не более двух
из трёх элементов являются четырёхзначными числами, а сумма элементов
тройки не больше максимального элемента последовательности,
оканчивающегося на 25.
В ответе запишите количество найденных троек чисел, затем максимальную
из сумм элементов таких троек.
В данной задаче под тройкой подразумевается три идущих подряд элемента
последовательности.
a = []

for i in open('17.txt'):
    a.append(int(i))

mx = max([i for i in a if abs(i) % 100 == 25])

otv = []

for i in range(len(a) - 2): # т.к. мы будем использовать в условиии не 2 элемента, а 3 (999 < a[i] < 10_000) + (999 < a[i+1] < 10_000) + (999 < a[i+2] < 10_000)
    if (999 < abs(a[i]) < 10_000) + (999 < abs(a[i+1]) < 10_000) + (999 < abs(a[i+2]) < 10_000) <= 2:
        if (a[i] + a[i+1] + a[i+2]) <= mx:
            otv.append(a[i] + a[i+1] + a[i+2])
print(len(otv), max(otv))
"""
#6
"""
В файле содержится последовательность целых чисел. Её элементы могут
принимать целые значения от-100 ООО до 100 ООО включительно. Определите
количество пар последовательности, в которых только один из элементов
является пятизначным числом, а квадрат суммы элементов пары превышает
квадрат максимального пятизначного элемента последовательности,
оканчивающегося на 37.
В ответе запишите количество найденных пар, затем максимальную из сумм
элементов таких пар.
В данной задаче под парой подразумевается два идущих подряд элемента
последовательности.

a = []

for i in open('17.txt'):
    a.append(int(i))

mx = max([i for i in a if 9999 < abs(i) < 100_000 and abs(i) % 100 == 37])

otv = []

for i in range(len(a) - 1):
    if ((9999 < abs(a[i]) < 100_000) + (9999 < abs(a[i+1]) < 100_000)) == 1:
        if (a[i] + a[i+1])**2 > mx**2:
            otv.append(a[i] + a[i+1])
print(len(a), max(otv))"""
#7
"""
В файле содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно.

Найдите модуль разности между количеством положительных и отрицательных чисел в файле.
a = []

for i in open('17.txt'):
    a.append(int(i))

positive = 0
negative = 0

for i in range(len(a)):
    if a[i] > 0:
        positive += 1
    elif a[i] < 0:
        negative += 1

otv = abs(positive - negative)
print(otv)"""
#8
"""a = []

for i in open('17.txt'):
    a.append(int(i))

mx = max([i for i in a if i % 100 == 10])
otv = []
for i in range(len(a) - 1):
    da = a[i] % 2023
    net = a[i+1] % 2023
    if da * net >= mx:
        otv.append(a[i] + a[i+1])
print(len(otv), min(otv))
print(da)"""
#9
'''
В файле содержится последовательность из 10 000 целых положительных чисел. Каждое число не превышает 10 000.
Определите и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 120, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.

a = []

for i in open('17.txt'):
    a.append(int(i))

otv = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):  # i+1 чтобы не повторяться и не брать один элемент
        if (a[i] + a[j]) % 120 == 0:
            otv.append(a[i] + a[j])

print(len(otv), max(otv))

#НЕВЕРНО
for i in range(len(a) - 1):
    if ((a[i] + a[i+1]) % 120) == 0:
Вы проверяете только соседние элементы (i и i+1). Например:
Проверяются пары: (0 и 1), (1 и 2), (2 и 3), ... (9998 и 9999)
Но не проверяются пары: (0 и 2), (0 и 3), (1 и 3), (1 и 4) и т.д.
По условию задачи нужно найти все возможные пары различных элементов, а не только стоящие рядом.
'''


"""a = [int(x) for x in open('17.txt')]

# количество чисел, кратных 5
count5 = sum(1 for x in a if x % 5 == 0)

sums = []
for i in range(len(a) - 1):
    if (a[i] < 0) != (a[i+1] < 0):          # ровно одно отрицательное
        s = a[i] + a[i+1]
        if s < count5:
            sums.append(s)

print(len(sums), max(sums))
        """

"""a = []
for i in open('17.txt'):
    a.append(int(i))

mx = max([i for i in a if i % 100 == 42])
otv = []
for i in range(len(a) - 2):
    k = 0
    for j in range(3):
        if 99 < a[i+j] < 1000:
            k += 1
            da = a[i + j]
    if k == 1 and da % 10 == 9:
        if (a[i] + a[i+1] + a[i+2]) > mx:
            otv.append(a[i] + a[i+1] + a[i+2])
print(len(otv), max(otv))
"""
        
    
"""a = []

for i in open('17.txt'):
    a.append(int(i))

mn = min([i for i in a if 99 < i < 1000 and i % 10 == 7])

otv = []
for i in range(len(a) - 1):
    if ((99 < a[i] < 1000) + (99 < a[i+1] < 1000)) == 1:
        if (a[i] + a[i+1]) % mn == 0:
            otv.append(a[i] + a[i+1])
print(len(otv), min(otv))"""

"""
a = []
for i in open('17.txt'):
    a.append(int(i))

mx = max([i for i in a if 999 < abs(i) < 10_000])
otv = []
for i in range(len(a) - 1):
    if abs(a[i] - a[i+1]) >= mx:
        otv.append(a[i] + a[i+1])
print(len(otv), max(otv))"""



"""a = []
for i in open('17.txt'):
    a.append(int(i))
otv = []

for i in range(len(a) - 1):
    da = sum([x for x in a if (a[i] % 3 == 0) or (a[i+1] % 3 == 0)])
    if da:
        otv.append(a[i] + a[i+1])
print(len(otv), max(otv))"""



"""a = []
for i in open('17.txt'):
    a.append(int(i))
res = []
for i in range(len(a) - 1):
    if (a[i] + a[i+1]) % 2 == 0: # количество пар чисел с одинаковой чётностью
        res.append(a[i] + a[i+1])
print(len(res))"""


"""a = []
for i in open('17.txt'):
    a.append(int(i))
# Находим два наибольших элемента
sorted_a = sorted(a, reverse=True)
max_product = sorted_a[0] * sorted_a[1]

otv = []

for i in range(len(a) - 2):
    # Проверяем, что ровно одно положительное
    positive_count = (a[i] > 0) + (a[i+1] > 0) + (a[i+2] > 0)
    if positive_count == 1:
        product = a[i] * a[i+1] * a[i+2]
        if product <= max_product:
            otv.append(a[i] + a[i+1] + a[i+2])

print(len(otv), max(otv))"""

"""a = []
for i in open('17.txt'):
    a.append(int(i))

da = [i for i in a if i % 11 == 0]
da_1 = sum(da) / len(da)
otv = []

for i in range(len(a) - 2):
    triplet = [a[i], a[i+1], a[i+2]]
    triplet_sum = sum(triplet)
    
    if any(abs(x) % 100 == 11 for x in triplet) and (triplet_sum / 3) > da_1:
        otv.append(triplet_sum)

print(len(otv), max(otv))"""



"""a = []
for i in open('17.txt'):
    a.append(int(i))

mn = [i for i in a if 9 < abs(i) < 100 and abs(i) % 10 == 1]
mn_da = min(mn)
mn_de = mn_da ** 2
otv = []
for i in range(len(a) - 1):
    x, y = a[i], a[i+1]
    if (x*x < mn_de) ^ (y*y < mn_de):
        if x + y >= 0:
            otv.append(x + y)
print(len(otv), min(otv))"""


"""a = [int(i) for i in open('17.txt')]

mn = min([i for i in a if i >= 0 and i % 35 == 0])
otv = []
for i in range(len(a) - 1):
    x, y = a[i], a[i+1]
    if x != y and (x - y) % mn == 0:
        otv.append(x + y)
print(len(otv), max(otv))"""
        
"""a = [int(i) for i in open('17.txt')]

da = sum(1 for i in a if abs(i) < 100)
otv = []
for i in range(len(a) - 1):
    x, y = a[i], a[i+1]
    das = x + y
    if das / 2 > da:
        otv.append(x + y)
print(len(otv), max(otv))"""


"""a = [int(i) for i in open('17.txt')]

mx = max([i for i in a if i % 17 == 0])
otv = []
for i in range(len(a) - 1):
    x, y = a[i], a[i+1]
    if (x + y) > mx:
        otv.append(x+y)
print(len(otv), max(otv))"""


"""a = [int(i) for i in open('17.txt')]

mx = max([i for i in a if 999 < abs(i) < 10000])

otv = []
for i in range(len(a)- 1):
    x, y = a[i], a[i+1]
    if abs(x - y) >= mx:
        otv.append(x + y)
print(len(otv), max(otv))"""


"""a = [int(i) for i in open('17.txt')]


mx = max([abs(i) for i in a if i % 1001 == 0])

otv = []
for i in range(len(a) - 1):
    x, y = a[i], a[i+1]
    pos = (99 < abs(x) < 1000) or (99 < abs(y) < 1000)
    if pos:
        if (x + y) > mx:
            otv.append(x + y)
print(len(otv), min(otv))"""

"""a = [int(i) for i in open('17.txt')]

mn = min([i for i in a if 99 < i < 1000 and i % 10 == 5])

otv = []
for i in range(len(a) - 1):
    x, y = a[i], a[i+1]
    pos = (99 < x < 1000) or (99 < y < 1000)
    if pos:
        if (x + y) % mn == 0:
            otv.append(x + y)
print(len(otv), max(otv))"""


"""a = [int(i) for i in open('17.txt')]

mn = min([i for i in a if i % 21 == 0])
otv = []
for i in range(len(a) - 1):
    x, y = a[i], a[i+1]
    if x % mn == 0 or y % mn == 0:
        otv.append(x + y)
print(len(otv), max(otv))"""


"""a = [int(i) for i in open('17.txt')]

mn = min([i for i in a if (99 < i < 1000) and i % 45 == 0])
otv = []
for i in range(len(a) - 1):
    x, y = a[i], a[i+1]
    if (999 < x < 10000) or (999 < y < 10000):
        if (x + y) % mn == 0:
            otv.append(x + y)
print(len(otv), min(otv))"""

a = [int(i) for i in open('17.txt')]

mn = min([i for i in a if i % 25 == 0])
otv = []
for i in range(len(a) - 1):
    x, y = a[i], a[i+1]
    if x % 2 == 0 or y % 2 == 0:
        if (x + y) % mn == 0:
            otv.append(x + y)
        
print(len(otv), max(otv))