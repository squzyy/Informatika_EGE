# ЕСЛИ ЧТО переменную = 0 юзаем при нахождении  количество чего та
#'01234567' - это например восьмиричная система счисления
#Важные моменты: Индексация всегда с 0, Отрицательные индексы (начинаются с -1 для последнего символа)
#permutations - когда перестановки, или что-то нужно использовать 1 раз, так же очень нужнен (не всегда) set для отделения одинаковых строк
# если мне нужно узнать не полное количество, а какое-то значение например в середине то использовать enumerate
"""
from itertools import product
k = 0
for n, s in enumerate(product(sorted('МУЖЧИНА'), repeat=5)):
    if (n + 1) % 2 == 1:
        if s[0] != 'Ж':
            if 0 < s.count('Ч') < 3:
                k += 1

print(k)
"""
"""
from itertools import product

alphabet = sorted('ТЕОРИЯ')  # ['Е', 'И', 'О', 'Р', 'Т', 'Я']

for n, s in enumerate(product(alphabet, repeat=7)):
    if (n + 1) % 2 == 0 and s[0] not in ('Е', 'И', 'О') and s.count('Я') == 1:
        print(n + 1)
        break
"""
"""
#YES, SIR
from itertools import*
numbi = 1 # можно не писать если использовать enumerate: for numbi, i in enumerate(product(sorted('АБВГДЕЖЗ'), repeat=3), 1):
for i in product(sorted('АБВГДЕЖЗ'), repeat=3):
    print(numbi, i)
    numbi += 1 

for numbi, i in enumerate(product(sorted('АБВГДЕЖЗ'), repeat=3), 1):
    if numbi == 350:
        print(i)
#Yes,Sr
"""
"""
from itertools import*
cnt = 0 # кол-во слов
numb = 1
for i in (product(sorted('ИНФОРМАТ'), repeat=5)):
    if numb % 2 != 0 and i[0] != 'О' and 1 <= i.count('Н') <= 2:
            cnt += 1
    numb += 1
print(cnt)
"""
"""
from itertools import *

cnt = 0
for i in product(sorted('12345678'), repeat = 5):
    if i.count('2') == 1:
        cnt += 1
print(cnt)
"""
"""
#Тут очень ВАЖНО запомнить что если нас просят не начинать с каких-либо цифр, то например как в данном случае если мы не допишем для i[0] not in '0(вот этот пидор)1357' то будет не 5-значное число (repeat=5)
from itertools import*
cnt = 0
for i in product('01234567', repeat = 5):
    if i[0] not in '01357' and i[-1] not in '26' and i.count('7') <= 2:
        cnt += 1
print(cnt)
"""
"""
from itertools import*
cnt = 0
for i in product(sorted('012345678'), repeat=7):
    numb = ''.join(i)
    if numb[0] != '0' and numb.count('5') == 1 and \
    all('5' + d not in numb and d + '5' not in numb for d in '02468'):
        cnt += 1
print(cnt)
"""
"""
from itertools import*
cnt = 0
for i in product(sorted('0123456789ab'), repeat = 5):
    numb = ''.join(i)
    if i[0] != '0' and numb.count('7') == 1 and \
    sum(1 for b in numb if b > '8') <= 3:
        cnt += 1
print(cnt)
"""
"""
from itertools import*
cnt = 0
for g in permutations('ВИКАГОПТЕР', r = 4):
    numb = ''.join(g)
    if numb[0] not in 'П' and 'ГО' not in numb:
        cnt += 1
print(cnt)
"""
"""
from itertools import*
cnt = 0
for i in set(permutations('КАРЕТА', r=4)):
    word = ''.join(i)
    if 'АА' not in word:
        cnt += 1
print(cnt)
"""
"""
from itertools import *
cnt = 0
for i in permutations('0123456789', r=4):
    numb = ''.join(i)
    if numb[0] != '0':
        for d in ('02468'):
            numb = numb.replace(d, '0')
        for d in ('13579'):
            numb = numb.replace(d, '1')
        if '00' not in numb and '11' not in numb:
                cnt += 1
print(cnt)
"""
"""
from itertools import *
numb = 1
for i in product(sorted('МАРИЯ'), repeat = 4):
    word = ''.join(i)
    if word == 'АРИЯ':
        print(numb)
    numb += 1
"""
"""
from itertools import *

numb = 1
for i in product(sorted('КОФЕ'), repeat=5):
    word = ''.join(i)
    
    if word.count('О') == 1:
        pos = word.index('О')
        left_ok = pos == 0 or word[pos-1] not in 'КФ'
        right_ok = pos == 4 or word[pos+1] not in 'КФ'
        
        if left_ok and right_ok:
            print(numb, word)
    
    numb += 1
"""
"""
from itertools import*
numb = 1
cht = 0
for i in product(sorted('СВОБДА'), repeat = 5):
    word = ''.join(i)
    if len(set(word)) == 5:
         if 'ОСОБА' < word < 'СДОБА':
            numb +=1
            cht += 1
            print(cht, word)
"""
"""
from itertools import*
numb = 1
ccc = 0
for i in product(sorted('ЛЕГКО'), repeat=6):
    word = ''.join(i)
    numb += 1
    if word.count('Г') >= 2 and 'ГГ' not in word:
        print(numb, word)
        
        ccc += 1
"""
"""
from itertools import*

for numb, i in enumerate(product(sorted('ЛАЙМ'), repeat = 5), 1):
    word = ''.join(i)
    if word.count('М') == 1 and'ЛЛ' not in word:
        print(numb, word)
"""
"""
from itertools import *

for dd, i in enumerate(product('0123456789ABC', repeat=6), 1):
    word = ''.join(i)
    if word[0] == '0' or word.count('5') > 1:
        continue
    nec = '13579B'
    if any(word[c] in nec and word[c+1] in nec for c in range(5)):
        continue
    print(dd, word)
    break
"""
"""
from itertools import*

for numb, i in enumerate(product(sorted('СТРОКА'), repeat = 5), 1):
    word = ''.join(i)
    if word[0] != 'А' and word[0] != 'С' and word[0] != 'Т' and word.count('О') == 2 and numb % 2 == 0:
        print(numb, word)
"""
"""
from itertools import product
bund = 0
for i in product('ВЗГЛЯД', repeat=4):
    
    word = ''.join(i)
    if 1 <= word.count('З') <= 2:
        bund += 1
        print(bund)
"""
"""
from itertools import*
cnt = 0
for i in product('012345', repeat = 6):
    word = ''.join(i)
    nochet = '135'
    if word[0] != '0' and word.count('2') == 1:
        if all('2' + g not in word and g + '2' not in word for g in nochet):
            cnt += 1
            print(cnt)
"""
    
    



    
























































































