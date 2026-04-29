"""import sys
sys.setrecursionlimit(3000000)
n = 1
max_value = 2
def F(n):
    if n == 1:
        return 2
    prev = F(n - 1)
    if prev < 7555444:
        return prev + 6
    return prev - 7555444
while n < 1000_000:
    n += 1
    print(F(n))"""

"""import sys
sys.setrecursionlimit(300000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n * F(n - 1)
res = (F(2024) // 4 + F(2023)) // F(2022)
print(res)"""

"""def F(n):
    if n > 10000:
        return 42
    if n <= 10000 and n % 2 == 0:
        return 2 * n + F(n + 3) + F(n + 4) + F(n + 6)
    if n <= 10000 and n % 2 != 0:
        return -(n + F(n + 1) + F(n + 3))
res = F(9996) - F(9994)
print(res)"""
"""
yes = 0

def f(n):
    global yes
    
    print('*')
    yes += 1
    
    if n >= 1:
        print('*')
        f(n - 1)
        f(n // 2)
        yes += 1
f(40)
print(yes)
"""
"""
import sys
sys.setrecursionlimit(10000000)
def F(n):
    if n < 4:
        return 3
    if n > 3:
        return 3 * F(n - 3)
res = F(3333) // F(3300)
print(res)
"""
"""
def F(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + F(n - 1)
    if n > 1 and n % 2 != 0:
        return 2 * F(n - 2)
print(F(24))
"""
"""
import sys 
sys.setrecursionlimit(1000000)
def F(n):
    if n == 41:
        return 41
    if n > 41 and n % 2 == 0:
        return F(n - 1) - n
    if n > 41 and n % 2 != 0:
        return n * F(n - 2)
res = F(9094) // F(9089)
print(res)
"""
"""
def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n / 2)
    if n % 2 != 0:
        return 1 + F(n - 1)
    
k = 0
for i in range(1, 501):
    if F(i) == 3:
        k += 1
print(k)
"""






"""size = 3000

F = [0] * (size + 1)


for n in range(size, 19, -1):
    if n >= 2025:
        F[n] = 1
    else:
        F[n] = (n - F[n+2]) - F[n+4]

res = F[20] + F[25]
print(res)"""

"""
если inf то:
from sys import *
from decimal import *
setrecursionlimit(1000000)

# Устанавливаем высокую точность
getcontext().prec = 10000

def F(n):
    if n <= 1:
        return Decimal(1)
    if n > 1 and n % 2 == 0:
        return F(n-1) / Decimal(3)
    if n > 1 and n % 2 != 0:
        return Decimal(6) * F(n-1)

yes = F(2049)
no = F(2046)
print(float(yes / no))"""

"""from sys import *
from decimal import *

getcontext().prec = 10000


def F(n):
    if n >= 2025:
        return Decimal(n)
    if n < 2025:
        return Decimal(n) + Decimal(3) + F(n+3)

da = F(23)
net = F(21)
print(float(da - net))"""

"""from sys import *
from decimal import *
setrecursionlimit(1000000)
getcontext().prec = 10000


def F(n):
    if n < 4:
        return Decimal(3)
    if n > 3:
        return Decimal(3) * F(n - 3)

da = F(3333)
net = F(3300)
print(float(da/net))"""


"""from sys import *
from decimal import *

setrecursionlimit(100000)
getcontext().prec = 10000

def F(n):
    if n > 10000:
        return Decimal(42)
    if n <= 10_000 and n % 2 == 0:
        return Decimal(2) * Decimal(n) + F(n + 3) + F(n + 4) + F(n + 6)
    if n <= 10_000 and n % 2 != 0:
        return -(Decimal(n) + F(n + 1) + F(n+3))
    
da = F(9996) - F(9994)
print(float(da))"""




"""from sys import *
from decimal import *

setrecursionlimit(100000)
getcontext().prec = 10000

def F(n):
    if n <= 100:
        return Decimal(3.14**n)
    if n > 100 and n % 2 == 0:
        return F(n - 1) + Decimal(n**2)
    if n > 100 and n % 2 != 0:
        return Decimal(2) * F(n - 2)
da = F(298) - Decimal(2) * F(295)
print(float(da))
    """

"""from sys import *
from decimal import *

setrecursionlimit(10020)
getcontext().prec = 10000

def F(n):
    if n >= 10_000:
        return Decimal(1)
    if n < 10_000 and n % 2 == 0:
        return F(n + 3) + Decimal(7)
    if n < 10_000 and n % 2 != 0:
        return F(n + 1) - Decimal(3)
da = F(50) - F(57)
print(float(da))"""

"""from sys import *
from decimal import *

setrecursionlimit(100000)
getcontext().prec = 10000
def F(n):
    if n  == 1:
        return Decimal(1)
    if n == 2:
        return Decimal(1)
    if n > 2:
        return F(n - 2) * (n + 1)
da = F(8)
print(float(da))"""



"""from sys import *
from decimal import *

setrecursionlimit(100000)
getcontext().prec = 10000

def F(n):
    if n == 1:
        return Decimal(1)
    if n > 1 and n % 2 != 0:
        return Decimal(n) + F(n - 2)
    if n % 2 == 0:
        return Decimal(n) * F(n - 1)
da = F(40)
print(float(da))"""



"""from sys import *

setrecursionlimit(100_000)

def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2 and n % 2 == 0:
        return (4 * n - F(n-3))//8
    if n > 2 and n % 2 != 0:
        return (4 * n - F(n-1) + F(n-2))//8
da = F(52)-F(38)
print(da)"""


"""from sys import *
from decimal import *
getcontext().prec = 10000
setrecursionlimit(10_0000)

def F(n):
    if n == 1:
        return Decimal(n)
    if n > 1:
        return Decimal(n) - 1 + F(n - 1)
da = F(2024) - F(2022)
print(float(da))"""


"""from sys import *

setrecursionlimit(100000)

def Yes(a, b):
    return a % b and a // b

def F(n):
    if n == 0:
        return 0
    if n > 0 and n % 2 == 0:
        return F(n//10) + n % 10
    if n % 2 != 0:
        return F(n//10)

s = 0

for k in range(10**9, 2 * 10**9):
    if F(k) == 2:
        s += 1
        print(s)"""
        
     

"""from sys import *
setrecursionlimit(100000)

def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return F(n - 2) * n
da = F(7)
print(da)"""




    
"""def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return F(n-2) * (n + 1)
da = F(8)
print(da)"""
"""from functools import lru_cache

@lru_cache(None)
def F(n):
    if n <= 1:
        return 1
    if n % 2 == 0 and n > 1:          # чётное
        return (n // 2) * F(n - 1)
    if n % 2 != 0 and n > 1:                   # нечётное
        return ((n - 1) // 2) * F(n - 1)

# Прогрев кеша не обязателен, но можно для скорости
for n in range(1, 10000):
    F(n)

result = (F(2024) - F(2022)) / F(2021)
print(result)"""
"""def F(n):
    result = 1
    for i in range(n, 3001):   # от n до 3000 включительно
        result = result * i
    return result

# Вычисляем нужные значения
f52 = F(52)
f53 = F(53)
f54 = F(54)

# Считаем результат
answer = (f52 - 2 * f53) // f54
print(answer)
"""
"""from functools import lru_cache
@lru_cache(None)
def F(n):
  if n <= 12:
    return 1
  if n > 12:
    return F(n - 1) + n - 2
for n in range(1, 3000):
  F(n)
print(F(2024) - F(2020))"""
"""from functools import lru_cache

@lru_cache(None)
def F(n):
    if n <= 1000:
        return 0  # базовое значение не влияет на ответ
    return n + 2 * F(n - 2) + 6 * F(n - 6)
for n in range(30000, 0, -1):
  F(n)
result = F(20024) - 2 * F(20022) - 3 * F(20020) + 18 * F(20014)
print(result)"""
# Массив для хранения значений F(n)
F = [0] * 20025  # индексы от 0 до 20024

# Базовые значения для n <= 1000 (можно любые)
for n in range(1001):
    F[n] = 0  # всё равно сократится

# Вычисляем для n от 1001 до 20024
for n in range(0, 20025):
    F[n] = n + 2 * F[n-2] + 6 * F[n-6]

# Считаем результат
result = F[20024] - 2*F[20022] - 3*F[20020] + 18*F[20014]
print(result)