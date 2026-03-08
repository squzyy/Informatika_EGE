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





















