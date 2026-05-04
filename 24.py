"""a = open('24.txt').readline()
k = 0
mx = []
for i in range(len(a)):
    if a[i] == 'X':
        k += 1
        mx.append(k)
    else:
        k = 0
print(max(mx))"""

"""a = open('24.txt').readline()
mx = 0
for l in range(len(a)):
    for r in range(l+1+mx, len(a)):
        s = a[l:r+1]
        if 'XX' in s or 'YY' in s or 'ZZ' in s:
            break
        else:
            mx = max(mx, len(s))
print(mx)"""

"""a = 'ACABCCC'
a = a.replace('AC', '*').replace('AB', '*')
mx = 0
k = 0
for i in range(len(a)):
    if a[i] == '*':
        k += 1
        mx = max(mx, k)
    else:
        k = 0
print(a, mx)"""
"""a = 'ABABCOCABA'
a = a.replace('O', 'A')
a = a.replace('D', 'B').replace('C', 'B')
a = a.replace('BA', '*').replace('B', ' ').replace('A', ' ').split()
print(len(max(a, key = len)))"""

"""a = 'PNONPOPPNPNNOPNONPO'
a = a.replace('PNO', '*').replace('NPO', '*')
k = 0
mx = 0
for i in range(len(a)):
    if a[i] == '*':
        k += 1
        mx = max(mx, k)
    else:
        k = 0
print(mx)"""

"""a = 'TUVWXYZZZXZUW'
mx = 0
for l in range(len(a)):
    for r in range(l+1+mx, len(a)):
        s = a[l:r+1]
        if s.count('Z') < 2:
            break
        else:
            mx = max(mx, len(s))
print(mx)"""

"""a = open('24.txt').readline()
for i in '123456789ABCDEF': a = a.replace(i, '*') # от 1 до 9
k, mx = 0, 0
for i in range(len(a)):
    if a[i] == '*':
        k += 1
        mx = max(mx, k)
    else:
        k = 0
print(mx)"""

"""a = open('24.txt').readline()
for i in '2468': a = a.replace(i, '0')
mx = 0
for l in range(len(a)):
    if a[l] == '0': # начинается с четной цифры 
        for r in range(l+1+mx, len(a)):
            s = a[l:r+1]
            if s.count('S') > 35 or s.count('0') > 1: 
                break
            if s.count('S') == 35 and s.count('0') == 1: # s.count('0') > 1 не содержащую др четную цифру, # s.count('S') > 35 ровно 35 S
                mx = max(mx, len(s))
print(mx)"""

a = open('24.txt').readline()
mx = 0
for l in range(len(a)):
    for r in range(l+1+mx, len(a)):
        s = a[l:r+1]
        if s.count('Y') > 80: # в условии не прописываем что нам не подходит s.count('2025') < 90 так как она накапливается
            break
        if s.count('2025') >= 90 and s.count('Y') == 80:
            mx = max(mx, len(s))
print(mx)