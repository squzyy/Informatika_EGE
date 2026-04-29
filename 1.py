from itertools import permutations
a = '56 4678 4678 2357 14 1238 2348 2367'.split()
s = 'DF DE DG DA FD FE FC FH CF CB BA BC AG AB AH AD EF ED EG EH HF HE HG HA GE GH GA GD'.split()
print('1 2 3 4 5 6 7 8')
for p in permutations('ABCDEFGH'):
  if all(str(p.index(x) + 1) in a[p.index(y)] for x, y in s):
    print(*p)