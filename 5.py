# [::-1] обратном навправлении
# print(n2[:len(n2) // 2]) - до середины, print(n2[len(n2) // 2:]) - после середины
# bin() преобразует целое число в его двоичное представление в виде строки
'''
r5 = n5[-1] + n5[:-1]
Разбор по частям:
Пусть n5 = "23" (как в примере с N=13)

n5[-1] - берёт последний символ строки

Индекс -1 означает последний элемент

"23"[-1] = "3"

n5[:-1] - берёт все символы кроме последнего

"23"[:-1] = "2" (от начала до предпоследнего)

n5[-1] + n5[:-1] - конкатенация (склеивание)

"3" + "2" = "32"
'''
'''
for n in range(1 ,1000):
    n2 = bin(n)[2:] # первые 2 числа 0 и b поэтому начинаем с третьего
    if n % 2 == 0:
        n2 = n2.replace('1', '11')
    else:
        n2 = n2.replace('0', '00')
    r = int(n2, 2)
    if r > 70:
        print(n)
        break
'''
'''
a = [] # создаем список если нужно узнать макс
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n % 3 == 0:
        n2 += n2[-3:] # дописываются три последние двоичные цифры
    else:
        n2 += bin((n % 3 + 1) * 3)[2:]
        r = int(n2, 2) # перевод числа в двоич.сист.счисл
        if r <= 416:
            a.append(r) # добавляем в список
print(max(a))
'''
'''
for n in range(1 ,1000):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 += '0'
    else:
        n2 += '1'
    if n2.count('1') % 3 == 0: # если просят если на втором шаге алгоритма
        n2 = '11' + n2[2:] # два левый разряда заменяются на 11
    else:
        n2 = '10' + n2[2:]
    r = int(n2, 2)
    if r >= 26:
        print(n)
        break
'''
'''
# приер в 4 тверичную
def to_4(n):
    n4 = ''
    while n > 0:
        n4 += str(n % 4)
        n //= 4
    return n4[::-1] # переворачивем

for n in range(1, 1000):
    n4 = to_4(n)
'''
'''
n = 116  # исходное число
n2 = bin(n)[2:]  # 1110100

if len(n2) % 2 == 1:
    d = len(n2) // 2
    new_n2 = n2[:d] + n2[d+1:]  # удаляем одну центральную
else:
    d = len(n2) // 2
    new_n2 = n2[:d-1] + n2[d+1:]  # удаляем две центральные

r = int(new_n2, 2)
print(r)
'''   
'''
for n in range(1, 1000):
    n2 = bin(n)[2:]
    if n % 3 == 0:
        n2 += n2[-3:]
    else:
        n2 += bin((n % 3)*3)[2:]
    r = int(n2, 2)
    if r >= 200:
        print(n)
        break
'''
'''

def to_5(n):
    n5 = ''
    while n > 0:
        n5 += str(n % 5)
        n //= 5
        return n5[::-1]

for n in range(1, 1000):
    n5 = to_5(n)
    summa = sum(int(d) for d in 5)
    if summa % 2 != 0:
        posl = n5[-1] + n5[:-1]
    else:
        n5 += bin((n[-1])*3)[2:]
        r = int(n5, 2)
        zero = n5.count('0')
        if r > zero == 2
'''

"""def to_base7(n):
    if n == 0:
        return '0'
    
    digits = ''
    while n > 0:
        remainder = n % 7
        digits += str(remainder)
        n //= 7
    
    return digits[::-1]"""

"""n = [x for x in range(100, 1000)]

for i in n:
    onetwo = [x for x in n if n[] * n[1:]]
    twothree = [x for x in n if n[2:] * n[1:]]
    if onetwo > twothree:
        list(onetwo) + list(twothree)
    else:
        list(twothree) + list(onetwo)
        print(onetwo)   """

"""def to_4(n):
    n4 = ''
    while n > 0:
        n4 += str(n % 3)
        n //= 3
    return n4[::-1] 

for n in range(1, 1000):
    n4 = to_4(n)
    r = n4
    if n % 3 == 0:
        r = r + r[-3:]
    else:
        d = n % 3
        d * 3
        d = to_4
    j = int(n, 3)
    print(j)
"""

"""a = []
for n in range(1, 1000):
    r = bin(n)[2:]
    summa = r.count('1')
    if summa % 2 == 0:
        r2 = r + '0'
        r3 = '10' + r2[2:]
    else:
        r2 = r + '1'
        r3 = '11' + r2[2:]
    R = int(r3, 2)
    if R > 30:
        a.append(n)
print(min(a))"""
    
    

"""res = []
for n in range(1, 1000):
    r = oct(n)[2:]
    nechet = 0
    for d in r:
        if int(d) % 2 == 0:
            nechet += 1
    if nechet % 2 == 1:
            da = r[-3:] + '46'
    else:
        ost = n % 8
        proizv = ost * 5
        proizv_vs = oct(proizv)[2:]
        da = proizv_vs + r
    R = int(da, 8)
    res.append(R)
minim = min(res)
print(minim)"""
"""a = []
for n in range(1, 1000):
    r = bin(n)[2:]
    summa = r.count('1')
    sisi = summa % 2
    r = r + str(sisi)
    summa2 = r.count('1')
    sisi2 = summa % 2
    r = r + str(sisi2)
    if int(r, 2) <= 120:
        a.append(n)
print(max(a))"""

"""a = []
for n in range(1, 1000):
    r = bin(n)[2:]
    nol = r.count('0')
    nenol = r.count('1')
    if nol > nenol:
        r = '10' + r[2:] + '0'
    else:
        r = '1' + r[:-2] + '10'
    if int(r, 2) >= 98:
        a.append(n)
print(min(a))"""

"""def to_3(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s
a = []
for n in range(1, 1000):
    r = to_3(n)
    if n % 3 == 0:
        r = r + r[-2:]
    else:
        r = r + to_3((n % 3) * 5)
    R = int(r, 3)
    if R >= 213:
        a.append(R)
print(min(a))"""

"""a = []
for n in range(1, 1000):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = r + '10'
    else:
        r = '1' + r and r + '1'
    R = int(r, 2)
    if 9 < R < 100:
        a.append(n)
print(min(a))"""

# print(n2[:len(n2) // 2]) - до середины, print(n2[len(n2) // 2:]) - после середины
'''a = []
for n in range(1, 1000):
    r = bin(n)[2:]
    if len(r) % 2 == 0:
        r = r[len(r) // 2:] + r[:len(r) // 2]
    R = int(r, 2)
    if R <= 26:
        a.append(n)
print(max(a))'''
"""a = []
for n in range(1, 1000):
    r = bin(n)[2:]
    if r.count('1') % 2 == 0:
        r = r + '1' and r + '10'
    else:
        r = '01' + r + '0' and r + '01'
    R = int(r, 2)
    if R < 1000 and n % 7 == 0:
        a.append(R)
print(max(a))"""


a = []
for n in range(100 + 1, 1000):
    r = hex(n)[2:]
    r.replace('b', '2')
    d = "123456789ABCDEF"
    if len([x for x in r if x in '13579bdf']) > 2:
        r = r + 'e'
    else:
        r = 'f' + r
    if int(r, 16) > 4001:
        a.append([int(r, 16), n])
print(sorted(max(a)))