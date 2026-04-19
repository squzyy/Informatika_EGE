"""x = 5 ** 20 + 5 ** 10 - 5 ** 13 - 5 ** 3

sm = 0
while x > 0:
    sm += (x % 5) # сумма цифр в записи
    x = x // 5
print(sm)"""

"""x = 7 * 49**120 - 6 * 343 ** 65 - 5 * 7 ** 40

k = 0
while x > 0:
    if x % 7 == 6:
        k += 1
    x = x // 7
print(k)"""


"""x = 2 * 2401**525 + 3 * 343**524 - 4 * 49**523 + 5 * 49 ** 522 - 6 * 7**521 - 35

k = 0
while x > 0:
    if x % 49 <= 9:
        k += 1
    x //= 49
print(k)"""


"""
Определите все значения x, при которых значение данного арифметического выражения кратно 11. В ответе укажите сумму найденных чисел в десятичной системе счисления. Основание системы счисления указывать не нужно.
from string import *
k = 0
for x in printable[:15]:
    n1 = int('97968' + x + '13', 15)
    n2 = int('7' + x + '213', 15)
    s = n1 + n2
    if s % 11 == 0:
        R = int(x, 15)
        k += R
print(k)"""


"""from string import *
k = 0
for x in printable[:18]:
    n1 = int('56' + x + '3', 18)
    n2 = int('4' + x + '9', 18)
    n3 = int('57' + x + '1', 18)
    s = n1 + n2 - n3
    prostoe = True
    
    # Проверяем все числа от 2 до s-1
    for i in range(2, s):
        if s % i == 0:  # если делится без остатка
            prostoe = False  # значит, не простое
            break  # дальше можно не проверять
    
    # Если число больше 1 и простое, увеличиваем счётчик
    if s > 1 and prostoe:
        k += 1

print(k)"""


"""x = 18 * 7 ** 108 - 5 * 49 ** 76 + 343 ** 35 - 50

sm = 0
x = abs(x)
while x > 0:
    sm += x % 49
    x = x // 49
print(sm)"""


"""x = 125 ** 10
k = 0
while x > 0:
    if x % 5 == 0:
        k += 1
    x //= 5
print(k)"""

"""
Значение арифметического выражения 
9 * 11 ** 210 + 8 * 11 ** 150 - x, где x – целое положительное число, не превышающее 3000, записали в 11﻿-﻿ричной системе счисления. Определите наибольшее значение x
x, при котором в 11﻿-﻿ричной записи числа, являющегося значением данного арифметического выражения, содержится ровно 60 нулей.

В ответе запишите число в десятичной системе счисления.



d = 9 * 11 ** 210 + 8 * 11 ** 150
max_x = 0

for x in range(1, 3000 + 1):  # x от 1 до 3000
    res = d - x
    
    # Подсчет нулей в 11-ричной записи числа res
    zeros_count = 0
    temp = res
    while temp > 0:
        if temp % 11 == 0:
            zeros_count += 1
        temp //= 11
    
    if zeros_count == 60:
        max_x = x  # сохраняем x, который дал 60 нулей

print(max_x)"""

    
"""d = 5 ** 85 + 5 ** 7
mx = 0
for x in range(1, 2500 + 1):
    res = d - x
    k = 0
    while res > 0:
        if res % 5 == 0:
            k += 1
        res //= 5
    if k == 80:
        mx = x
print(mx)"""

"""d = 9 * 11 ** 210 + 8 * 11 ** 150
mx = 0
for x in range(1, 3000 + 1):
    res = d - x
    k = 0
    while res > 0:
        if res % 11 == 0:
            k += 1
        res //= 11
    if k == 60:
        mx = x
print(mx)"""
"""
from string import *

for x in printable[:19]:
    n1 = int('98897' + x + '21', 19)
    n2 = int('2' + x + '923', 19)
    s = n1 + n2
    if s % 18 == 0:
        print(s // 18)"""

"""from string import *

for x in printable[:27]:
    n1 = int('KLMN' + x + '12', 27)
    n2 = int('F' + x + 'GHI34', 27)
    s = n1 + n2
    if s % 26 == 0:
        print(s // 26)"""

"""
Определите значение x, при котором в двадцативосьмеричной записи числа, являющегося значением данного арифметического выражения, содержится наибольшее количество нулей.

Для найденного x вычислите значение арифметического выражения и укажите его в ответе в десятичной системе счисления.
d = 4 * 28 ** 10 + 3 * 28 ** 6 + 28 ** 3
max_zeros = 0
best_x = 0

for x in range(1, 28000 + 1):
    res = d - x
    k = 0
    while res > 0:
        if res % 28 == 0:
            k += 1
        res //= 28
    if k > max_zeros:  # изменили: сравниваем с максимумом
        max_zeros = k  # сохраняем новый максимум
        best_x = x     # запоминаем x
print(d - best_x)"""

"""from string import *

for x in printable[:13]:
    n1 = int('537' + x + '623', 13)
    n2 = int('6' + x + '35' + x + '2', 13)
    s = n1 - n2
    if s % 3 == 0:
        R = int(x, 13)
        print(R)"""

"""from string import *

for y in printable[:15]:
    n1 = int('ABCD' + y, 15)
    n2 = int('123' + y + '4', 15)
    s = n1 + n2
    if s % 14 == 0:
        print(s // 14)"""

"""from string import *

for x in printable[:25]:
    n1 = int('b7' + x + '35F1', 25)
    n2 = int('16' + x + 'k1', 25)
    n3 = int('1' + x + 'g',25)
    s = n1+n2+n3
    if s % 24 == 0:
        print(s // 24)"""


"""def to_4(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s
a = []
for x in range(1, 200):
    r = to_4(x)
    if int(r) % 1000 == 123: #r.endswith('123')
        a.append(x)
        print(a)"""

"""x = 3 * 7 ** 82 - 4 * 49**21 + 5 * 343 ** 25
sm = 0
while x > 0:
    sm += x % 7
    x //= 7
print(sm)"""

"""from string import printable

for x in printable[:29]:
    n1 = int('42' + x + '158', 29)
    n2 = int('16' + x + '234', 29)
    s = n1 + n2
    if s % 28 == 0:
        print(s // 28)"""

"""from string import *

for x in printable[:23]:
    n1 = int('324' + x + '72', 23)
    n2 = int('45' + x + '562', 23)
    s = n1 + n2
    if s % 22 == 0:
        print(s // 22)"""

"""from string import printable

for x in printable[:29]:
    n1 = int('463' + x + '7921', 29)
    n2 = int('8241' + x + '153', 29)
    s = n1 + n2
    if s % 28 == 0:
        print(s // 28)"""

"""
Определите наименьшее значение 
x, при котором в двенадцатеричной записи значения этого арифметического выражения содержится наибольшее количество нулей.

В ответе запишите число в десятичной системе счисления.

d = 12**457 + 12**48
a = []

# Считаем количество нулей для каждого x
for x in range(1, 3500 + 1):
    res = d - x
    k = 0
    while res > 0:
        if res % 12 == 0:
            k += 1
        res //= 12
    a.append(k)

max_zeros = max(a)

for i, zeros in enumerate(a):
    if zeros == max_zeros:
        i += 1
        print(i)"""

"""d = 3 ** 100
for x in range(1, 2030 + 1):
    res = d - x
    k = 0
    while res > 0:
        if res % 3 == 0:
            k += 1
        res //= 3
    if k == 5:
        print(x)"""


"""from itertools import *
d = 5 ** 100
a = []
for x in range(1, 2030 + 1):
    res = d - x
    k = 0
    while res > 0:
        if res % 5 == 0:
            k += 1
        res //= 5
    a.append(k)
        

max_k = max(a)

for i, zeros in enumerate(a):
    if zeros == max_k:
        i += 1
        print(i)
        break
"""

"""
Определите в тридцатишестеричной записи числа количество цифр с числовым значением, не превышающим 7.
x = 5*1296**597+8*216**314-4*36**215+9*6**214-7*6**18-54
k = 0
while x > 0:
    if x % 36 <= 7:
        k += 1
    x //= 36
print(k)"""

"""k = 0
x = 7 ** 21 + 49 ** 13 - 7 ** 10
while x > 0:
    
    if x % 7 == 6:
        k += 1
    x //= 7
print(k)"""


"""from string import *
a = []
for x in printable[:16]:
    n1 = int('27A' + x + '23', 16)
    for y in printable[:16]:
        n2 = int('8' + y + 'E5D2', 16)
        res = n1 + n2
        if res % 5 == 0:
            a.append(int(x, 16) + int(y, 16))
print(max(a))"""


"""x = 2 * 729**75 + 2 * 243 ** 78 + 81 ** 81 + 2 * 27 ** 84 + 2 * 9 ** 87 + 58
a = []
while x > 0:
    if x % 27 == 0:
        a.append(x)
    x //= 27
print(len(a))"""


"""x = 2 ** 2048 + 32 ** 102 - 8 * 4 ** 128
a = []
while x > 0:
    if x % 32 and x >= 10:
        a.append(x)
    x //= 32
print(len(a))"""


"""x = 5 ** 20 + 5 ** 10 - 5 ** 13 - 5 ** 3
sm = 0
while x >0:
    sm += x % 5
    x //= 5
print(sm)"""
"""a = []
for x in range(1, 95 + 1):
    temp = x
    while temp >= 5:
        temp //= 5
    if temp == 3:
        a.append(x)
print(sum(a))"""

"""from string import *
a = []
for x in printable[:8]:
    n1 = int('36' + x + '53', 8)
    for y in printable[:8]:
        n2 = int('4' + y + '3', 8)
        s = n1 - n2
        if s > 0:
            a.append(s)
print(a)"""


"""from string import *

for x in printable[:15]:
    n1 = int('9897' + x + '21', 15)
    n2 = int('12' + x + '023', 15)
    s = n1 + n2
    if s % 14 == 0:
        print(s//14)"""

"""x = 7 ** 21 + 49 ** 13 - 7 ** 10
k = 0
while x > 0:
    if x % 7 == 6:
        k += 1
    x //= 7
print(k)"""

"""x = 5 ** 20 + 5 ** 10 - 5 ** 13 - 5 ** 3
sm = 0
while x > 0:
    sm += x % 5
    x //= 5
print(sm)"""

"""from string import printable
k = 0
for x in printable[:18]:
    n1 = int('56' + x + '3', 18)
    n2 = int('4' + x + '9', 18)
    n3 = int('57' + x + '1', 18)
    s = n1 + n2 - n3
    pr = True
    for i in range(2, s):
        if s % i == 0:
            pr = False
            break
    if s > 0 and pr:
        k += 1
        print(k)"""

"""x = 5 * 1296**597 + 8 * 216**314 - 4 * 36**215 + 9 * 6 ** 214 - 7 * 6 ** 18 - 54
k = 0
while x > 0:
    if x % 36 <= 7:
        k += 1
    x //= 36
print(k)"""

"""d = 5**85 + 5**7
for x in range(2501):
    s = d - x
    k = 0
    while s > 0:
        if s % 5 == 0:
            k += 1
        s //= 5
    if k == 80:
        print(x)"""

"""x = 15 * 2401 ** 1500 - 10 * 343 ** 1200 + 40 * 49 ** 1000 - 35 * 7 ** 850 - 4805
k = 0
while x > 0:
    if x % 49 > 9:
        k += 1
    x //= 49
    print(k)"""

"""from string import printable

for x in printable[:17]:
    n1 = int('5432' + x + '67', 17)
    n2 = int('302' + x, 17)
    s = n1 + n2
    if s % 19 == 0:
        print(s)"""



"""from string import printable

a = []
for x in printable[:39]:
    for y in printable[:39]:
        n1 = int('58' + x + '723' + y + '49', 39)
        if n1 % 38 == 0:
            yx = int(y + x, 39)
            for k in range(yx + 1):
                if k * k == yx:
                    a.append(yx)

print(a[0])"""

"""from string import *

for x in printable[:36]:
    n1 = int('NEW', 36)
    n2 = int('YE' + x + 'R', 36)
    s = n1 + n2
    if s % 35 == 0:
        print(s // 35)"""

"""printbl = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
k = 0
for x in printbl[:18]:
    n1 = int('56' + x + '3', 18)
    n2 = int('4' + x + '9', 18)
    n3 = int('57' + x + '1', 18)
    s = n1 + n2 - n3
    da = True
    for i in range(2, s):

        if s % i == 0:
            da = False
    if s > 1 and da == True:
        k += 1
        print(k)"""


"""from string import *
for x in printable[:29]:
    n1 = int('463' + x + '7921', 29)
    n2 = int('8241' + x + '153', 29)
    s = n1 + n2
    if s % 28 == 0:
        print(s // 28)"""

"""from string import *
for x in printable[:18]:
    n1 = int('77968' + x + '11', 18)
    n2 = int('4' + x + '213', 18)
    s = n1 + n2
    if s % 7 == 0:
        print(s // 7)"""

"""from string import printable

for x in printable[:17]:
    n1 = int('149' + x + '3', 17)
    n2 = int(x + '612', 17)
    n3 = int(x + '54' + x, 17)
    s = n1 + n2 - n3
    a = []
    if s % 7 == 0:
        R = int(x, 17)
        print(R)"""


"""def to_4(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s
a = []
for x in range(1, 200):
    r = to_4(x)
    if int(r) % 1000 == 123: #r.endswith('123')
        a.append(x)
print(a)"""


"""def to_17(n):
    s = ''
    while n > 0:
        digit = n % 17
        if digit < 10:
            s = str(digit) + s
        else:
            s = chr(ord('A') + digit - 10) + s
        n //= 17
    return s


k = 0
for x in range(1, 1000):
    r = to_17(x)
    if r[0] == '3' and r[-1] == 'D':
        k += 1
print(k)"""

"""from string import *
a = []
for x in printable[:15]:
    n1 = int('99658' + x + '29', 15)
    n2 = int('102' + x + '023', 15)
    s = n1 + n2
    if s % 14 == 0:
        print(s // 14)"""

"""
записали в некой системе счисления. Определите наибольшее основание этой системы счисления, при котором запись числа будет оканчиваться на 001.
x = 7 * 512**120 - 6 * 64**100 + 8**210 - 255

for p in range(1000, 1, -1):  # перебираем от 1000 вниз до 2
    if x % (p**3) == 1:
        print(p)
        break"""

"""x = 7 ** 21 + 49 **13 - 7**10
k = 0
while x > 0:
    if x % 7 == 6:
        k += 1
    x //= 7
print(k)"""

def to_18(n):
    s = ''
    while n > 0:
        digit = n % 18
        if digit < 10:
            s = str(digit) + s
        else:
            s = chr(ord('A')+ digit - 10) + s
        n //= 18
    return s

def to_4(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n //= 4
    return s