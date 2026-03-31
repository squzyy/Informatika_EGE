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

"""import sys
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
        print(A)"""


"""for A in range(1, 10000):
    Da = True
    for x in range(1, 10000):
        if (((x&42 != 0) or (x&13 != 0)) <= ((x&30 == 0) <= (x&A != 0))) == 0:
            Da = False
            break
    if Da == True:
        print(A)
        break
            """




"""P = [i for i in range(25, 50 + 1)]
Q = [i for i in range(32, 47 + 1)]

A = [i for i in range(1, 100 + 1)]


for x in range(1, 100 + 1):
    if (((not(x in A)) <= (x in P)) <= ((x in A) <= (x in Q))) == 0:
        A.remove(x)
print(A)"""

"""P = [i for i in range(130, 171 + 1)]
Q = [i for i in range(150, 185 + 1)]

A = []


for x in range(1, 1000):
    if ((x in P) <= (((x in Q) and (not(x in A))) <= (not(x in P)))) == 0:
        A.append(x)
print(A)
"""


"""for A in range(1, 10_00):
    for x in range(1, 10_00):
        for y in range(1, 10_00):
            if ((x +3*y > A) or (y < 30) or (x < 30)) == 0:
                break
        if ((x +3*y > A) or (y < 30) or (x < 30)) == 0:
            break
    else:
        print(A)
"""






"""
P = [i for i in range(10, 40+1)]
Q = [i for i in range(5, 15+1)]
R = [i for i in range(35, 50 + 1)]

A = []

for x in range(1, 10_000):
    if (((x in A) or (x in P)) or ((x in Q) <= (x in R))) == 0:
        A.append(x)
print(A)
"""




"""def Del(n, m):
    return n % m == 0

for A in range(1, 100000):
    Yes = True
    for x in range(1, 100000):
        if ((A < 50) and ((not(Del(x, A))) <= (Del(x, 10) <= (not(Del(x, 18)))))) == 0:
            Yes = False
            break
    if Yes == True:
        print(A)"""



"""P = (12, 14, 19, 20, 25)
Q = (13, 18, 19 ,20, 30)

A = list(range(1, 100+1))

for x in range(1, 100+1):
    if ((not((x in P) == (x in A))) <= ((x in Q) == (x in A))) == 0:
        A.remove(x)
        print(A)"""










"""for A in range(1, 10000): 
    Yes = False
    for x in range(1, 10000):  
        for y in range(1, 10000):
            if not ((x + 2*y != 58) or ((A - x > 0) == (A + y > 0))):
                Yes = True
                break
        if Yes:
            break
    if not Yes:
        print(A)
        break"""




"""for A in range(1, 1000):
    Yes = True
    for y in range(1, 100):
        for x in range(1, 100):
            if not ((x + 2*y != 58) or ((A-x >0) == (A + y > 0))):
                Yes = False
                break
    if Yes == True:
        print(A)
        break"""



"""def F(m, n):
    return m & n

for A in range(1, 10_000):
    Yes = True
    for x in range(1, 10000):
        if not ((x & A == 0) or ((x & 44 == 4) <= (x & 27 == 10))):
            Yes = False
            break
    if Yes == True:
        print(A)"""




"""for A in range(1, 10000):
    Yes = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((x >= A) or (121 >= x**2)) and ((y**2 < 49) or (A < y))):
                Yes = False
                break
    if Yes == True:
        print(A)"""


"""def Del(x, A):
    return x % A == 0

for x in range(1, 1000):
    if (Del(x, 30) or Del(15, x)):
        if x > 1:
            print(x)"""



"""def Del(n, m):
    return n % m == 0

B = [i for i in range(160, 180 + 1)]

for A in range(1, 10000):
    Yes = True
    for x in range(1, 1000):
        if not((x in B) <= (Del(x, 35) <= Del(x, A))):
            Yes = False
            break
    if Yes == True:
        print(A)"""


"""def Del(n, m):
    return n % m == 0

B = [i for i in range(50, 70 + 1)]

for A in range(1, 10_000):
    Yes = True
    for x in range(1, 1000):
        if not(Del(x , A) or ((x in B) <= (not Del(x, 21)))):
            Yes = False
            break
    if Yes == True:
        print(A)"""

"""for A in range(1, 1000):
    Yes = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((2*x + y < A) or (y > 17) or (x > y)):
                Yes = False
                break
    if Yes == True and A > 0:
        print(A)"""

"""def F(m, n):
    return m & n


for A in range(1, 10_0000):
    Yes = True
    for x in range(15, 30 + 1):
        if not((x&29 == 0) or ((x&11 == 0) <= (not(x&A == 0)))):
            Yes = False
            break
    if Yes == True:
        print(A)
        break"""


"""P = [i for i in range(23, 45 + 1)]
Q = [i for i in range(34, 56 + 1)]

A = [i for i in range(1, 100 + 1)]


for x in range(1, 10000):
    if not((x not in A) or ((x not in P) and (x in Q))):
        A.remove(x)
print(A)"""


"""P = [i for i in range(10, 21 + 1)]

A = []

for x in range(1, 10000):
    if not((not(x in P)) or (x in A)):
        A.append(x)
print(A)"""



"""for A in range(1, 10000):
    Yes = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((x * y > A) or (x > y) or (11 > x)):
                Yes = False
                break
    if Yes == True:
        print(A)"""

"""P = [i for i in range(19, 142 + 1)]
Q = [i for i in range(75, 182 + 1)]

A = []

for x in range(1, 1000):
    if (not((x in Q) <= ((not(x in A)) and (x in P) <= (not(x in Q))))):
        A.append(x)
print(A)"""







"""P = (2, 4, 6, 8, 10, 12, 14, 16, 18, 20)
Q = (5, 10, 15, 20, 25, 30, 35, 40, 45, 50)

A = [i for i in range(1, 100+1)]

for x in range(1, 100+1):
    if not(((x in A) <= (x in P)) and ((x in Q) <= (not(x in A)))):
        A.remove(x)
print(A)
"""


"""P = (12, 14, 19, 20, 25)
Q = (13, 18, 19, 20 , 30)

A = [i for i in range(1, 100+1)]

for x in range(1, 100+1):
    if not((not((x in P) == (x in A))) <= ((x in Q) ==(x in A))):
        A.remove(x)
print(A)

print(12*13*14*18*19*20*25*30)"""

"""def Del(n, m):
    return n % m == 0

for A in range(1, 10000):
    Yes = True
    for x in range(1, 1000):
        if not((not(Del(x, 3) and Del(x, 5))) or (A >= 42 - x)):
            Yes = False
            break
    if Yes == True:
        print(A)
        break"""

"""def F(M, K):
    return M&K

for A in range(1, 10000):
    Yes = True
    for x in range(1, 1000):
        if (((x&17 != 0) <= ((x&A != 0) <= (x&58 != 0))) <= ((x&8 == 0) and (x&A != 0) and (x&58 == 0))) == 1:
            Yes = False 
    if Yes == True:
        print(A)
        break"""




"""def Del(n, m):
    return n % m == 0

for A in range(1, 10_000):
    da = True
    for x in range(1, 1000):
        if not((not(Del(x, 3) and Del(x, 5))) or (A >= 42 - x)):
            da = False
            break
    if da == True:
        print(A)
        break"""

"""for A in range(1, 1000):
    da = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((2*x + y < A) or (y > 17) or (x > y)):
                da = False
                break
    if da == True:
        print(A)
        break"""

"""
P = (-42, -10, -8, 2, 16)
Q = (-10, -4, 2, 15, 23)

A = [i for i in range(1, 100 + 1)]

for x in range(1, 100 + 1):
    if not(((x in A) <= (x in P)) or (x in Q)):
        A.remove(x)
print(sum(A))
"""

"""
P = [i for i in range(23, 58 + 1)]
Q = [i for i in range(1, 39 + 1)]

A = []

for x in range(1, 100 + 1):
    if not(((x in P) or (x in A)) <= ((x in Q) or (x in A))):
        A.append(x)
print(A)"""


"""for A in range(1, 1000):
    da = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((x * y < A) or (x < y) or (x >= 12)):
                da = False
                break
    if da == True:
        print(A)
        break"""


"""def Del(n, m):
    return n % m == 0

for A in range(1, 10_000):
    da = True
    for x in range(1, 10_000):
        if not((Del(72, x) <= (not Del(120, x))) or (A - x > 100)):
            da = False
            break
    if da == True:
        print(A)
        break"""


"""for A in range(1, 1000):
    da = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not((2*x + 3*y < A) or (x > y) or (y > 24)):
                da = False
                break
    if da == True:
        print(A)
        break"""


"""def F(m, n):
    return m & n

for A in range(1, 10_0000):
    da = True
    for x in range(1, 10_0000):
        if not ((x&25 != 0) <= ((x&19 == 0) <= (x&A != 0))):
            da = False
            break
    if da == True:
        print(A)
        break"""

"""P = [i for i in range(22, 72 + 1)]
Q = [i for i in range(42, 102 + 1)]

A = []

for x in range(1, 100+1):
    if not ((not((not(x in A)) and (x in P))) or (x in Q)):
        A.append(x)
print(len(A))"""

"""def Del(n, m):
    return n % m == 0

for A in range(1, 10_000):
    da = True
    for x in range(1, 10_000):
        if not((not Del(x,A)) <= (not(Del(x, 21)) and (not Del(x, 35)))):
            da = False
            break
    if da == True:
        print(A)"""
        


"""P = [i for i in range(7, 63 + 1)]
Q = [i for i in range(28, 99 + 1)]
R = [i for i in range(85, 119 + 1)]

A = []

for x in range(1, 200 + 1):
    if not((x in Q) <= ((not(x in P)) <= (((not(x in R)) and (not(x in A))) <= (not(x in Q))))):
        A.append(x)
print(len(A))"""

"""for A in range(1, 1000):
    yes = True
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(((y +3*x )> A) or (x < 20) or (y < 50)):
                yes = False
    if yes:
        print(A)"""


"""def F(n, m):
    return n & m

for A in range(1, 10000):
    yes = True
    for x in range(1, 10000):
        if not(((x&116 != 0) or (x&92 != 0)) <= ((x&69==0) <= (x&A != 0))):
            yes = False
            break
    if yes == True:
        print(A)
        break"""
        
"""P = [i for i in range(30, 45 + 1)]
Q = [i for i in range(40, 55 + 1)]

A = []

for x in range(1, 100):
    if not(((not(x in A))<=(not(x in P))) and ((x in Q)<=(x in A))):
        A.append(x)
print(len(A))"""