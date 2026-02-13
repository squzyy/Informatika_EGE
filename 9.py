''' sorted (a = sorted([int(x) for x in i.split()]))), set - это когда все числа разные (if len(a) == len(set(a)))
# all() — все элементы удовлетворяют условию, Возвращает True, если каждый элемент в последовательности истинный (или условие выполняется для всех).
# any() — хотя бы один элемент удовлетворяет условию, Возвращает True, если хотя бы один элемент в последовательности истинный.
# если мне нужен номер строки а не количество то с 1
# '''
'''
cnt = 0
for i in open('da.txt'):
    a = sorted([int(x) for x in i.split()])
    if (a[0] + a[2])**2 > a[1]**2 :
        cnt += 1
print(cnt)
'''
'''
a = [12, 102, 26, 102, 21, 12, 73]
da = [x for x in a if a.count(x) == 2] # только те эелементы которые повторяются 2 раза
da_1 = [x for x in a if a.count(x) == 1] # уникальные
if len(da) == 4 and len(da_1) == 3: # тут крч 4 и 3 это общее количество наших числе в скобках (сделано чтоб среднее арефметичское посчитать)
    if sum(da) / len(da): # среднее арефметическое
        print(da) 
'''   
'''
cnt = 0
for i in open('da.txt'):
    a = ([int(x) for x in i.split()])
    if len(a) == len(set(a)):
        if sum(a) % 3 == 0:
            cnt += 1
print(cnt)
'''
'''
k = 0
for i in open('da.txt'):
    a = sorted([int(x) for x in i.split()])
    if sum(a) > a[2]*2:
        k +=1
print(k)
'''
'''
k = 0
for i in open('da.txt'):
    a = ([int(x) for x in i.split()])
    da_b = sum(x for x in a if x > 0)
    da_m = sum(x for x in a if x < 0)
    count3 = sum(1 for x in a if abs(x) % 10 == 3) # квадрат суммы положительных чисел меньше квадрата суммы отрицательных чисел. (abs() - это модуль)
    if count3 == 3 and da_b**2 < da_m**2:
        k += 1
print(k)
'''
'''
cnt = 0
for i in open('da.txt'):
    a = sorted([int(x) for x in i.split()])
    max_cube = a[3] ** 3
    product_of_others = 2 * a[0] * a[1] * a[2]
    
    if max_cube > product_of_others:
        if min(a) > 10:
            cnt += 1  
print(cnt)
'''
'''
k = 0
for i in open('da.txt'):
    a = sorted([int(x) for x in i.split()])
    if a[3] < (a[0] + a[1] + a[2]) and (a[0] + a[1]) == (a[2] + a[3]) or \
        (a[0] + a[2]) == (a[1] + a[3]) or \
            (a[0] + a[3]) == (a[1] + a[2]):
        k += 1
print(k)
'''
'''
numb = 0
for i in open('da.txt'):
    numb += 1
    a = sorted([int(x) for x in i.split()])
    doubles = set([x for x in a if a.count(x) == 2])
    if len(doubles) == 1:   # ровно одно число повторяется дважды (проверяется длина)
        povtor = list(doubles)[0]
        if a[0] != povtor:  # минимальное не повторяется
            print(numb)
'''
'''
k = 0
for i in open('da.txt'):
    a = sorted([int(x) for x in i.split()])
    krat = any(num % 3 == 0 for num in a)
    if krat and a[0] + a[1] > a[2]:
        k += 1
        print(a)
print(k)
'''
'''
for yes, i in enumerate(open('da.txt'), 1):
    a = ([int(x) for x in i.split()])
    povt2 = set([x for x in a if a.count(x) == 2])
    povt3 = set([x for x in a if a.count(x) == 3])
    if len(povt2) == 1 and len(povt3) == 1:
        if max(povt3) > max(povt2):
            print(yes)
'''
'''
da = 0
for i in (open('da.txt')):
    a = sorted([int(x) for x in i.split()])
    if a[3] < (a[0] + a[1] + a[2]) and \
       (a[0] + a[1] == a[2] + a[3] or \
        a[0] + a[2] == a[1] + a[3] or \
        a[0] + a[3] == a[1] + a[2]):
        da += 1
        print(da)
'''
'''
k = 0
for i in open('da.txt'):
    a = sorted([int(x) for x in i.split()])
    krat = any(s % 3 == 0 for s in a)
    if krat and (a[0] + a[1]) > a[2]:
        k += 1
print(k)
'''
'''
k = 0
for i in open('da.txt'):
    a = sorted([int(x) for x in i.split()])
    if a[3] < (a[0] + a[1] + a[2]) and \
    (a[0] + a[1] == a[2] + a[3] or
     a[0] + a[2] == a[1] + a[3] or
     a[0] + a[3] == a[2] + a[1]):
        k += 1
print(k)
'''
'''
k = 0
for i in open('da.txt'):
    a = ([int(x) for x in i.split()])
    razn = [x for x in a if a.count(x) == 1]
    if a[0] < a[1] < a[2]  and razn:
        k += 1
print(k)
'''
'''
k = 0
for i in open('da.txt'):
    a = ([int(x) for x in i.split()])
    povt = [x for x in a if a.count(x) == 2]
    nepovt = [x for x in a if a.count(x) == 1]
    if len(povt) > 0:  # есть хотя бы одно число, повторяющееся 2 раза
        if not nepovt:  # нет неповторяющихся чисел
            k += 1
        elif all(p > max(nepovt) for p in povt):  # все повторяющиеся больше всех неповторяющихся
            k += 1
print(k)
'''

























