from itertools import product
k = 0
for n, s in enumerate(product(sorted('МУЖЧИНА'), repeat=5)):
    if (n + 1) % 2 == 1:
        if s[0] != 'Ж':
            if 0 < s.count('Ч') < 3:
                k += 1

print(k)

"""
from itertools import product

alphabet = sorted('ТЕОРИЯ')  # ['Е', 'И', 'О', 'Р', 'Т', 'Я']

for n, s in enumerate(product(alphabet, repeat=7)):
    if (n + 1) % 2 == 0 and s[0] not in ('Е', 'И', 'О') and s.count('Я') == 1:
        print(n + 1)
        break
"""