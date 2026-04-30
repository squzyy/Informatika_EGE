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
'''
k = 0
for i in open('da.txt'):
    a = [int(x) for x in i.split()]
    maxc = max(a)
    minc = min(a)
    summ = (maxc + minc) % 3 == 0
    b = sorted(a)
    comd = (b[0] - b[1] == b[2] - b[3] or \
            b[0] - b[2] == b[1] - b[3] or \
            b[0] - b[3] == b[2] - b[1])
    if summ and comd:
        k += 1
print(k)
 '''
'''
k = 0
for i in open('da.txt'):
    a = ([int(x) for x in i.split()])
    povt = [x for x in a if a.count(x) == 2]
    nechet = any(c % 2 != 0 for c in a)
    if (povt and not nechet) or (not povt and nechet):
        k += 1
print(k, a)

 '''
'''
k = 0
for i in open('da.txt'):
    a = sorted([int(x) for x in i.split()])
    if a[3] < (a[0] + a[1] + a[2]) and \
    (a[0] + a[1] == a[2] + a[3] or \
     a[0] + a[2] == a[1] + a[3] or \
     a[0] + a[3] == a[1] + a[2]):
        k += 1
        print(k)
'''
'''
Я РЕШИЛ ЭТО сососососо
Определите, сколько среди заданных троек чисел таких, которые могут быть сторонами прямоугольного треугольника.
n = 0
for i in open('da.txt'):
    a = ([int(x) for x in i.split()])
    da = (a[2]**2 == (a[0]**2 + a[1]**2) or\
          a[1]**2 == (a[2]**2 + a[0]**2) or\
          a[0]**2 == (a[1]**2 + a[2]**2))
    if da:
        n += 1
        print(n, a)
'''
'''
—  в строке есть ровно одно число, которое повторяется трижды, и остальные числа без повторений;

—  квадрат суммы всех повторяющихся чисел строки больше квадрата суммы всех неповторяющихся чисел строки.

В ответе запишите только число.
k = 0
for i in open('da.txt'):
    a = sorted(([int(x) for x in i.split()]))
    da = 1
    dva = [x for x in a if a.count(x) == 3]
    nep = [x for x in a if a.count(x) == 1]
    sum1 = sum(dva)
    sum2 = sum(nep)
    if dva and nep and sum1**2 > sum2**2:
        k += 1
        print(k, a)

'''
'''
k = 0
for i in open('da.txt'):
    a = ([int(x) for x in i.split()])
    da = len([x for x in a if a.count(x) == 2]) == 2 #в строке есть ровно одно число, которое повторяется дважды, а остальные числа различны;
    net = len([x for x in a if a.count(x) == 1]) == 5 # в строке есть ровно одно число, которое повторяется дважды, а остальные числа различны;
    if da and net and a.count(min(a)) == a.count(max(a)):
        k += 1
        print(k)
'''

"""k = 0
for i in open('da.txt'):
    a = ([int(x) for x in i.split()])
    povt3 = [x for x in a if a.count(x) == 3]
    povt1 = [x for x in a if a.count(x) == 1]
    if len(povt3) == 3 and len(povt1) == 3 and len(set(a)) == 4:
        if sum(povt1) / 3 < povt3[0]:
            k += 1
            print(k, a)
        """

'''k = 0
for i in open('da.txt'):
    a = sorted(([int(x) for x in i.split()]))
    summa = (a[1] + a[2] + a[3])
    if summa // a[0] >= 6 and a[3] * a[0] > (a[1] * a[2]):
        k += 1
        print(k, summa, a)'''

"""k = 0
for i in open('da.txt'):
    a = sorted(([int(x) for x in i.split()]))
    if a[0] < (a[1] + a[2]) and a[1] < (a[0] + a[2]) and a[2] < (a[0] + a[1]) or \
    a[0] < (a[2] + a[1]) and a[1] < (a[2] + a[0]) and a[2] < (a[1] + a[0]):
        k += 1
        print(k, a)"""



"""k = 0
for i in open('da.txt'):
    a = ([int(x) for x in i.split()])
    min_val = min(a)
    if a.count(min_val) == 1 and min(a) in a[:4] and \
        (a[0] + a[1] + a[2] + a[3]) / 4 > (a[4] + a[5] + a[6] + a[7]) / 4:
        k += 1
        print(k, a)"""


"""ss = []
for i in open('9.txt'):
    a = [int(x) for x in i.split()]
    to_3 = [x for x in a if a.count(x) == 3]
    to_1 = [x for x in a if a.count(x) == 1]
    if len(to_3) == 3 and len(to_1) == 4:
        if ((sum(to_1)) / 4) <= to_3[0]:
            ss.append(a)
print(sum(ss[-1]))"""


'''k = 0
for i in open('9.txt'):
    a = [int(x) for x in i.split()]
    if (a[0] == 90 and a[1] + a[-1] == 90) or \
    (a[1] == 90 and a[0] + a[-1] == 90) or \
    (a[-1] == 90 and a[0] + a[1] == 90):
        k += 1
print(k)'''

'''k = 0  
for i in open('9.txt'):
    a = sorted([int(x) for x in i.split()])
    if abs(((a[-1]) - (a[0])) ** 3) <= ((a[1] + a[2]) ** 2):
        k += 1
        print(k, a)
print(k)'''
        
"""k = 0
for i in open('9.txt'):
    a = [int(x) for x in i.split()]
    to_3 = [x for x in a if a.count(x) == 3]
    to_1 = [x for x in a if a.count(x) == 1]
    if len(to_3) == 3 and len(to_1) == 3:
        if sum(to_1) * 3 <= sum(to_3) * 10:
            k += 1
            print(k, a)
print(k)
"""
"""k = 0
for i in open('9.txt'):
    a = [int(x) for x in i.split()]
    to_3 = [x for x in a if a.count(x) == 3]
    to_1 = [x for x in a if a.count(x) == 1]
    if len(to_3) == 3 and len(to_1) == 3:
        if sum(to_3) ** 2 > sum(to_1) ** 2:
            k += 1
            print(k, a)
print(k)
 """

"""k = 0
for i in open('9.txt'):
    a = sorted([int(x) for x in i.split()])
    if a[-1] < (a[0] + a[1] + a[2]):
        if (a[0] + a[1] == a[2] + a[-1]) or \
        (a[0] + a[2] == a[1] + a[-1]) or \
        (a[0] + a[-1] == a[1] + a[2]):
            k += 1
            print(k, a)
print(k)
"""


"""k = 0
for i in open('9.txt'):
    a = [int(x) for x in i.split()]
    to_2 = [x for x in a if a.count(x) == 2]
    to_1 = [x for x in a if a.count(x) == 1]
    if len(to_2) == 4 and len(to_1) == 3:
        if (sum(to_2) / 4) < (sum(a) / 7):
            k += 1
            print(a)
print(k)"""

"""k = 0
for i in open('9.txt'):
    a = ([int(x) for x in i.split()])
    to_2 = [x for x in a if a.count(x) == 2]
    to_1 = sorted([x for x in a if a.count(x) == 1])
    if len(to_2) == 2 and len(to_1) == 5:
        if (to_1[0] * to_1[1] * to_1[2]) > to_2[0] ** 2:
            k += 1
            print(k, a)
print(k)
"""
"""k = 0
for i in open('9.txt'):
    a = [int(x) for x in i.split()]
    to_2 = sorted([x for x in a if a.count(x) == 2])
    to_1 = sorted([x for x in a if a.count(x) == 1])
    if len(to_2) == 2 and len(to_1) == 2:
        if (((to_1[0] % 2 != 0) and (to_1[-1] % 2 != 0))) and ((to_2[0] % 2) == 0):
            k += 1
            print(to_1)
print(k)"""

"""k = 0
for i in open('9.txt'):
    a = [int(x) for x in i.split()]
    to_2 = [x for x in a if a.count(x) == 2]
    to_1 = [x for x in a if a.count(x) == 1]
    if len(to_2) == 2 and len(to_1) == 5:
        if sum(1 for d in a if d == max(a)) == sum(1 for d in a if d == min(a)):
            k += 1
            print(a)
print(k)"""

"""s = []
k = 1
for i in open('9.txt'):
    a = sorted([int(x) for x in i.split()])
    chet = sum(1 for d in a if d % 2 == 0)
    nchet = sum(1 for d in a if d % 2 != 0)
    if chet == nchet:
        if a[0] + a[5] == a[1] + a[4] == a[2] + a[3]:
            s.append(k)
    k += 1
print(max(s))
"""
"""count = 0
for s in open('9.txt'):
    m = [int(x) for x in s.split()]
    m.sort()
    pov = [int(x) for x in m if m.count(x) > 1]
    nepov = [int(x) for x in m if m.count(x) == 1]
    if len(pov) > 0 and m[0] != m[1] and (m[-1])/((sum(m)-m[-1])/5) > 3:
        count += 1
print(count)"""



"""k = 0
for i in open('9.txt'):
    a = [int(x) for x in i.split()]
    to_2 = [x for x in a if a.count(x) == 2]
    to_1 = [x for x in a if a.count(x) == 1]
    if len(to_2) == 2 and len(to_1) == 4:
        if (sum(to_1) / len(to_1)) <= sum(to_2):
            k += 1
print(k)"""


"""for k, i in enumerate(open('9.txt'), 1):
  a = [int(x) for x in i.split()]
  to_2 = [x for x in a if a.count(x) == 2]
  to_3 = [x for x in a if a.count(x) == 3]
  to_1 = [x for x in a if a.count(x) == 1]
  if len(to_2) == 2 and len(to_3) == 3 and len(to_1) == 3:
      if to_3[0] > to_2[0]:
          print(k)"""
"""k = 0
for i in open('9.txt'):
    a = [int(x) for x in i.split()]
    to_2 = [x for x in a if a.count(x) == 2]
    chet = [x for x in to_2 if x % 2 == 0]
    nchet = [x for x in to_2 if x % 2 == 1]
    od = [x for x in a if a.count(x) == 1]
    if len(chet) == 2 and len(nchet) == 2 and len(od) == 3:
        if (sum(nchet)*3) > (chet[0]*chet[1]):
            k += 1
print(k)"""
"""for k, i in enumerate(open('9.txt'), 1):
    a = sorted([int(x) for x in i.split()])
    to_2 = [int(x) for x in a if a.count(x) == 2]
    to_1 = [int(x) for x in a if a.count(x) == 1]
    if len(to_2) == 2 and a.count(a[-1]) == 1:
        print(k)
        break"""

"""for k, i in enumerate(open('9.txt'), 1):
    a = sorted([int(x) for x in i.split()])
    to_2 = [int(x) for x in a if a.count(x) == 2]
    to_1 = [int(x) for x in a if a.count(x) == 1]
    if len(to_2) == 2 and a.count(a[-1]) == 1:
        print(k)
        break"""
"""k = 0
for i in open('9.txt'):
    a = sorted([int(x) for x in i.split()])
    to_1 = [x for x in a if a.count(x) == 1]
    if len(to_1) == 3 and a[-1] ** 2 < (a[0] ** 2 + a[1] ** 2):
        k += 1
print(k)"""

"""a = sorted([100, 100, 200, 200, 2, 3])
to_1 = [x for x in set(a) if a.count(x) == 1]
to_2 = [x for x in set(a) if a.count(x) == 2]
da = to_2[-1] ** 2 > (to_1[0] * to_1[1])
if len(to_2) == 2 and len(to_1) == 2 and da:
    print(a)"""
"""k = 0
for i in open('9.txt'):
    a = ([int(x) for x in i.split()])
    to_1 = [x for x in a if a.count(x) == 1]
    to_2 = [x for x in a if a.count(x) > 1]
    if to_1 and to_2:
        if (sum(to_1) / len(to_1)) < (sum(to_2) / len(to_2)):
            k += 1
            print(k)"""

"""for k, i in enumerate(open('9.txt'), 1):
    a = ([int(x) for x in i.split()])
    to_1 = [x for x in a if a.count(x) == 1]
    to_3 = [x for x in a if a.count(x) == 3]
    if len(to_3) == 2 and len(to_1) == 4:
        if to_3[0] > (sum(to_1) / len(to_1)):
            print(k)"""
k = 0
for i in open('9.txt'):
    a = ([int(x) for x in i.split()])
    to_1 = [x for x in a if a.count(x) == 1]
    to_3 = [x for x in a if a.count(x) == 2]
    if len(to_3) == 4 and len(to_1) == 3:
        if (sum(to_1) / len(to_1)) <= (sum(a) / len(a)):
            k += 1
            print(k)