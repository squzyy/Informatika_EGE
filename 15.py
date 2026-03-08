'''
Побитовая конъюкция n & m (5 = 101, 6 = 110 и каждая цифра 101 умножается на каждую цифру 110, в данном случае: 1*1, 0*1, 0*1 = 100 в итоге print(int('100', 2)) или print(5 & 6))
Длина это большее - меньшее но если например: [6, 7, 8, 9, 10, 11] то мы будем из 12 вычитать 6, зависит от условия задачи в задаче не было 11
'''


"""for a in range (2000):
    if all( (x*y < a) or (y > x) or (x >= 8)
           for x in range (1, 2001)
           for y in range (1, 2001) ):
        print(a)
        break"""

"""
def Del(n, m):
    return n % m == 0

for A in range(1, 10_000):
    Yes = True
    for x in range(1, 10_000):
        if ((not(Del(x, A))) <= (not(Del(x, 18))) or (not(Del(x, 42)))) == 0:
            Yes = False
            break
    if Yes == True:
        print(A)
"""
"""for A in range(1, 10_00):
    for x in range(1, 10_00):
        if ((x & 34 != 0) <= ((x & 41 == 0) <= (x & A != 0))) == 0:
            break
    else:
        print(A)"""

"""for A in range(1, 1000):
    Yes = True
    for x in range(1 ,1000):
        for y in range(1 ,1000):
            if (((y + 5*x != 31) or (A > x-2)) and (A < y+37)) == 0:
                Yes = False
                break
    if Yes == True:
        print(A)

или

for A in range(1, 1000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if (((y + 5*x != 31) or (A > x-2)) and (A < y+37)) == 0:
                break
        if (((y + 5*x != 31) or (A > x-2)) and (A < y+37)) == 0: -- Еще раз из-за того что мы в цикле и в x и в y
            break
    else:
        print(A)"""

"""
R = list(range(12, 31 + 1))
Q = list(range(6, 15 +1))
P = list(range(17, 23 + 1))

A = [] #Для наименьшей длины

for x in range(1 , 100):
    if (((x in A) or (x in P)) or ((x in Q)<= (x in R))) == 0:
        #print((((x in A) or (x in P)) or ((x in Q)<= (x in R))), A, x)
        A.append(x)
        #print((((x in A) or (x in P)) or ((x in Q)<= (x in R))), A, x)
print(A)


Q = list(range(8, 17 + 1))
P = list(range(3, 11 + 1))
A = list(range(1, 100 + 1)) #Для наибольшей длины

for x in range(1, 100 + 1):
    if (((x in A) <= (x in P)) or (x in Q)) == 0:
        print(((x in A) <= (x in P)) or (x in Q), A, x)
        A.remove(x)
        print(((x in A) <= (x in P)) or (x in Q), A, x)
        """
"""
P = (1, 2, 4, 12, 13)
Q = (1, 4, 9, 13, 35, 81)
R = (2, 10, 13, 15, 35)

a = []

for x in range(1, 130):
    if (((x not in P) and (x not in Q)) or (x in R)) == 0:
        a.append(x)
        print(a)

"""
"""
P = list(range(74, 194 + 1))
Q = list(range(152, 223 + 1))

A = []

for x in range(1, 300):
    if (((not(x in A)) and (x in P)) <= ((x in P) <= (not(x in Q)))) == 0:
        A.append(x)
print(A)
print(194-152)
"""

"""
P = (14, 16, 18, 20, 22, 24)
Q = (16, 19, 22, 25, 28)

A = []

for x in range(1, 100):
    if ((x not in P) or ((x not in Q) <= (x in A))) == 0:
        A.append(x)
print(A)
print(14*18*20*24)
"""

"""def Del(n, m):
    return n % m == 0

for A in range(1, 10000):
    Yes = True
    for x in range(1, 10000):
        if (Del(x, 128) <= ((not(Del(x, A))) <= (not Del(x, 80)))) == 0:
            Yes = False
            break
    if Yes == True:
        print(A)
"""
"""
def Del(n, m):
    return n % m == 0

for A in range(1, 10_0000):
    Yes = True
    for x in range(1, 10_0000):
        if (((Del(x, A) and Del(x, 45)) <= Del(x, 162)) and (A > 200)) == 0:
            Yes = False
            break
    if Yes == True:
        print(A)
        break
"""

import sys
sys.setrecursionlimit(2000000)

def Del(n, m):
    return n % m == 0

for A in range(1, 10_000):
    Da = True
    for x in range(1, 10_000):
        if (Del(A, 45) and (Del(750, x) <= ((not Del(A, x)) <= (not Del(120, x))))) == 0:
            Da = False
            break
    if Da == True:
        print(A)


















































