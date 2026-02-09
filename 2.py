'''
from itertools import *
def f(x, y, w, z):
    return ((not x) and (not y)) or (y == z) or w

for a, b, c, d, e in product([0, 1], repeat=5):
    table = ((a, b, 1, c, 0),
             (1, 0, d, 1, 0),  # таблица из задачи
             (0, 0, 1, 1, 0))


# отстается всегда не изменным, может иногда изменяться xywz если другие буквы или букв больше
    if len(table) == len(set(table)):
        for p in permutations('xywz', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)
'''
'''
from itertools import *
def f(x, y, w, z):
    return ((not x) or (not y)) and (not(x == z)) and w

for a, b, c in product([0, 1], repeat=3):
    table = ((1, a, 0, 0, 1),
             (1, 0, 0, 1, 1),
             (1, 0, b, c, 1))

if len(table) == len(set(table)):
    for p in permutations('xywz', r=4):
        if all(f(**dict(zip(p, line))) == line[-1] for line in table):
            print(*p)
'''

'''
from itertools import *
def f(x, w, z, y):
    return (x == (y <= z)) and (y == (not z <= w))

for a, b, c, d in product ([0, 1], repeat=4):
    table = ((0, 0, a, 0, 1),
             (b, 0, c, 0, 1),
             (1, 0, 1, d, 0))

if len(table) == len(set(table)):
    for p in permutations('xwzy', r=4):
        if all(f(**dict(zip(p, line))) == line[-1] for line in table):
            print(*p)
'''

'''
from itertools import *
def f(x, y, w, z):
    return (not(x <= z)) or (y == w) or y

for a, b, c, d, e, l, s in product([0, 1], repeat=7):
    table = ((1, 0, a, b, 0),
             (c, 1, 0, d, 0),
             (0, e, l, s, 0))
    
    if len(table) == len(set(table)):
        for p in permutations('xywz', r=4):
            if all(f(**dict(zip(p, line[:4]))) == line[-1] for line in table):
                print(*p)
'''
'''
from itertools import *
def f(x, y, z, w):
    return (not ((not y or not x) == (y or z))) or (not w) #F  =  ((y → ¬x) ≡ (y ∨ z)) → ¬w,

for a, b, c, d, e, l, n, s in product ([0, 1], repeat=8):
    table = ((0, a, b, 0, 0),
             (1, c, 0, 0, 0),
             (d, e, 1, 0, 0),
             (l, n, 1, s, 0))
    
    if len(table) == len(set(table)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)
'''
'''
from itertools import *
def f(x, y, z, w):
    return (x and (not y)) or (x == z) or (not w)

for a, b, c, d in product ([0, 1], repeat=4):
    table = ((a, b, 0, 0, 0),
             (1, 1, 1, 0, 0),
             (1, 0, c, d, 0))
    
    if len(table) == len(set(table)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)
'''
'''
from itertools import *
def f(x, y, z, w):
    return (z and y) or ((x <= z) == (y <= w))

for a, b, c, d, e, l in product ([0, 1], repeat=6):
    table = (
        (a, b, c, 1, 0),
        (1, d, e, 1, 0),
        (1, l, 1, 1, 0)
    )

    if len(table) == len(set(table)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)
'''
'''
print('x w z ')
for x in range(2):
    for w in range(2):
        for z in range(2):
            for y in range(2):
                if ((x == y) or ((y or z) <= x)) == 0:
                    print(x, w, z, y)
'''
'''
from itertools import *

def f(x, y, z):
    return (x == y) or ((y or z) <= x)

for a, b, c in product ([0,1], repeat = 3):
    table = (
        (a, 1, 1, 0),
        (b, c, 1, 0)
    )
    if len(table) == len(set(table)):
        for p in permutations('xyz', r=3):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                 print(*p)
'''
'''
from itertools import *
def f(x, y, z, w):
    return ((x and (not y)) == (z or (not w))) <= (x and z)

for a, b, c, d, e, l in product ([0, 1], repeat=6):
    table = (
        (1, a, 1, 1, 0),
        (1, b, 1, c, 0),
        (d, e, 1, l, 0)
    )

    if len(table) == len(set(table)):
        for p in permutations('xyzw', r = 4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)
'''
'''
from itertools import *
def f(x, y, z, w):
    return (x or y) and (not(y == z)) and (not w)

for a, b, c, d in product([0, 1], repeat=4):
    table = ((1, a, 1, b, 1),
             (0, 1, c, 0, 1),
             (d, 1, 1, 0, 1))
    
    if len(table) == len(set(table)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)
'''
'''     
from itertools import*
def f(x, y, z, w):
    return ((w <= y) <= x) or (not z)

for a, b, c, d, e, l, g in product([0, 1], repeat = 7):
    table = (
        (a, b, 1, c, 0),
        (d, 0, e, l, 0),
        (g, 1, 0, 0, 0)
    )

    if len(table) == len(set(table)):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)
'''
'''
from itertools import*

def f(x, y, z, w):
    return ( x and (not y)) or (y == z) or (not w)

for a, b, c, d in product ([0, 1], repeat = 4):
    table = (
        (a, b, 0, 0, 0),
        (1, 0, c, 0, 0),
        (1, 0, 1, d, 0)
    )

    if len(set(table)) == len(table):
        for p in permutations('xyzw', r=4):
            if all(f(**dict(zip(p, line))) == line[-1] for line in table):
                print(*p)
'''
'''
from itertools import *

def f1(w, x, y, z):
    return (w <= y) == (x and z)

def f2(w, x, y, z):
    return (not x) or (not y) or (not z) or w

def f3(w, x, y, z):
    return (z or w) and y and x

table = (
    (1, 0, 1, 0, 1),  
    (0, 1, 1, 1, 0),  
    (1, 1, 1, 0, 1)   
)
for p in permutations('wxyz', r=4):
        if (f1(**dict(zip(p, table[0]))) == table[0][-1]and
        f2(**dict(zip(p, table[1]))) == table[1][-1]and
        f3(**dict(zip(p, table[2]))) == table[2][-1]):
            print(*p)
'''

    

                
            
        