"""from itertools import permutations
a = '56 4678 4678 2357 14 1238 2348 2367'.split()
s = 'DF DE DG DA FD FE FC FH CF CB BA BC AG AB AH AD EF ED EG EH HF HE HG HA GE GH GA GD'.split()
print('1 2 3 4 5 6 7 8')
for p in permutations('ABCDEFGH'):
  if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
    print(*p)"""
"""from itertools import *

a = '57 457 46 236 12 348 128 67'.split()
s = 'FC CG GD DB BF FA AE EB GH HD'.split()
print('1 2 3 4 5 6 7 8')
for p in permutations('ABCDEFHG'):
  if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
    print(*p)"""

"""from itertools import *
a = '235 13 1245678 36 13 347 368 37'.split()
s = 'АБ БГ ГЕ ЕЗ ЗЖ ЖД ДГ ГВ ВА АГ ГА ГБ ГЕ ГЗ ГЖ ГД ЗГ ЖГ'.split()
print('1 2 3 4 5 6 7 8')
for p in permutations('АБВГДЕЗЖ'):
  if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
    print(*p)"""

"""from itertools import *
a = '236 136 1245678 35 347 123 358 37'.split()
s = 'ЖЗ ЗБ БЕ ЕД ДГ ГБ БА АВ ВЖ ЖБ БЗ БВ БГ БД ЕГ'.split()
print('1 2 3 4 5 6 7 8')
for p in permutations('ЖЗБДГАВЕ'):
  if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
    print(*p)"""

"""from itertools import *
a = '3457 456 167 128 126 2358 138 467'.split()
s = 'LK KB BP PL LR LA PQ BC KR AC AQ RC CQ'.split()
print('1 2 3 4 5 6 7 8')
for p in permutations('LKBPRCQA'):
  if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
    print(*p)"""

"""from itertools import *
a = '24 14 46 1236 6 345'.split()
s = 'AC CB CD BF BE EF'.split()
print('1 2 3 4 5 6')
for p in permutations('ACBEFD'):
  if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
    print(*p)"""

"""from itertools import *
a = '345 467 14 123567 147 24 245'.split()
s = 'AF FE ED DC CB GA GE GD GC GB'.split()
print('1 2 3 4 5 6 7')
for p in permutations('AFEDCBG'):
  if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
    print(*p)"""


"""from itertools import *
a = '346 45 16 42567 24 1347 46'.split()
s = 'АБ АВ БВ ВГ ВД ВЕ ГЕ ГК ДЕ ЕК'.split()
print('1 2 3 4 5 6 7')
for p in permutations('АБВГДЕК'):
  if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
    print(*p)"""
