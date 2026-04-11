# ЕСЛИ ЧТО переменную = 0 юзаем при нахождении  количество чего та
#'01234567' - это например восьмиричная система счисления
#Важные моменты: Индексация всегда с 0, Отрицательные индексы (начинаются с -1 для последнего символа)
#permutations - когда перестановки, или что-то нужно использовать 1 раз, так же очень нужнен (не всегда) set для отделения одинаковых строк
# если мне нужно узнать не полное количество, а какое-то значение например в середине то использовать enumerate
# all() — все элементы удовлетворяют условию, Возвращает True, если каждый элемент в последовательности истинный (или условие выполняется для всех).
# any() — хотя бы один элемент удовлетворяет условию, Возвращает True, если хотя бы один элемент в последовательности истинный.
#int(x, base) — заходим в любую систему, выходим с числом
#bin() — покажи число в двоичной
#oct() — покажи число в восьмеричной
#hex() — покажи число в шестнадцатеричной
#print() — покажи число в десятичной

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
"""
from itertools import *

for ss, i in enumerate(product(sorted('БАТЫР'), repeat = 5), 1):
    word = ''.join(i)
    if ('Ы' not in word) and ('АА' not in word):
        print(ss)
"""
"""
# НЕВЕРНО all(chet + d not in word and nechet + chet not in word for d in nechet) где chet = 'abcd', nechet = '13579'. При выполнении for d in nechet происходит следующее: nechet + chet '13579abcd'
from itertools import*
k = 0
for i in product('0123456789abcd', repeat = 5):
    word = ''.join(i)
    chet = 'abcd'
    nechet = '13579'
    if word[0] != '0' and \
    all((lett + dig not in word) and (dig + lett not in word) #Здесь двойной цикл: сначала lett перебирает 'a','b','c','d', а для каждого lett перебираются все dig
    for lett in 'abcd' for dig in '13579'): #Здесь двойной цикл: сначала lett перебирает 'a','b','c','d', а для каждого lett перебираются все dig
        k += 1
        print(k)
"""
"""
from itertools import*
k = 0
for i in product('012345', repeat=6):
    word = ''.join(i)
    if word[0] != '0' and word.count('2') == 1 and \
    all('1' + d not in word and d + '1' not in word and '3' + d not in word and d + '3' not in word and '5' + d not in word and d + '5' not in word for d in '2'):
        k += 1
print(k)     
"""
"""
from itertools import *
n = 0
for i in product(sorted('МАРИЯ'), repeat = 4):
    word = ''.join(i)
    n += 1
    print(n, word)
"""
"""
from itertools import *

for num, i in enumerate(product(sorted("АЛГОРИТМ"), repeat=5), 1):
    word = ''.join(i)
    if word[0] not in 'АГ' and word.count('Р') >= 2:
        if num % 2 == 0:
            print(num)
            break 
"""
'''
from itertools import *
ss = 0
for k, i in enumerate(product(sorted('ФАВОРИТ'), repeat=7), 1):
    word = ''.join(i)
    if word.count('ТРИО') == 1 and word[:4] != 'ТРИО' and word[-4:] != 'ТРИО': #[:4] первые 4 буквы, [-4:] последние 4
        if k % 2 != 0:
            ss += 1

            print(ss, k)

'''
'''
from itertools import *
n = 1
for k, i in enumerate(product(sorted('ЯНДЕКС'), repeat = 6), 1):
    word = ''.join(i)
    if word == 'ЯНДЕКС':
        print(k)
'''
'''
from itertools import *

for i in product('0123456789ab', repeat = 6):
    word = ''.join(i)
    da = '13579b'
    no = '02468a'
    if word[0] != '0' and word.count('5') == 1 and \
    da + no not in word:
        print(word)
'''
'''
from itertools import*
k = 0
for ss, i in enumerate(product('0123456789abcde', repeat=8), 0):
    word = ''.join(i)
    if word[0] != '0' and word.count('0') == 2:
        if sum(word.count(letter) for letter in 'abcde') <= 4:
            k += 1
            print(k)
'''
'''
from itertools import *
k = 0
for i in product('0123456', repeat=6):
    word = ''.join(i)
    da = sum(1 for d in word if d in '246') % 2 == 0 # а количество остальных чётных цифр чётно.
    if word[0] != '0' and word.count('0') == 1 and da:
        k += 1
        print(k)
'''
"""from itertools import *
k = 0
for i in product('АНДРЕЙ', repeat = 6):
    word = ''.join(i)
    if word.count('Й') <= 1 and word[0] not in 'Й' and word[5] not in 'Й' and \
    all(d + 'Й' not in word and 'Й' + d not in word for d in 'Е'):
        k += 1
    print(k, word)"""

"""from itertools import *
k = 0
for i in product(sorted('СЛОН'), repeat = 5):
    word = ''.join(i)
    k += 1
    if k == 1020:
        print(k, word)
"""

"""from itertools import *
k = 0
for i in product('ПЯТНИЦА', repeat = 5):
    word = ''.join(i)
    if word[0] not in 'Н' and word.count('Я') == 1:
        k += 1
        print(k, word)"""



"""from itertools import *
k = 0
for i in product('012345678', repeat = 5):
    word = ''.join(i)
    nechet = '1357'
    sigma = '0'
    if word[0] != '0' and word.count('0') == 1 and \
    all(sigma + d not in word and d + sigma not in word for d in nechet):
        k += 1
        print(k, i)
"""

"""from itertools import *
k = 0
for i in product('ДЕМЬЯН', repeat=6):
    s = ''.join(i)
    if (s.count('Д') and s.count('Е') and s.count('М') and s.count('Ь') and s.count('Я') and s.count('Н')) == 1 and \
    s[0] != 'Ь' and ('ЕЬ' not in s and 'ЯЬ' not in s):
        k += 1
        print(k, s)
"""
"""from itertools import *
k = 0
for i in product('ABCDXY', repeat=4):
    s = ''.join(i)
    if s[0] == 'X' or s[0] == 'Y':
        if all(d not in 'XY' for d in s[1:]):
            k += 1        
            print(k, s)"""


"""from itertools import *

for k, i in enumerate(product(sorted('ЛЕМУР'), repeat = 4), 0):
    s = ''.join(i)
    if s[0] == 'Л':
        k += 1
        print(k, s)"""

"""from itertools import *
k = 0
for i in product('0123456789ab', repeat = 5):
    s = ''.join(i)
    pizda = [d for d in s if d in '02468a']
    nepizda = [g for g in s if g in '13579b']
    if s[0] != '0' and  len(pizda) == 3 and len(set(pizda)) == 1:
        da = pizda[0]
        if da * 3 in s:
            k += 1
print(k)"""

"""from itertools import *
k = 0
for i in product('РОСОМАХА', repeat=8):
    s = ''.join(i)
    if sand(s.count('Р') == 1 and s.count('О') == 2 and s.count('С') == 1 and s.count('М') == 1 and s.count('А') == 2 and s.count('Х') == 1) and \
    ('О' + 'О') not in s and ('О' + 'А') not in s and ('А' + 'А') not in s and ('А' + 'О') not in s and \
    ('Р' + 'Р') not in s and ('Р' + 'С') not in s and ('С' + 'Р') not in s and \
    ('Р' + 'М') not in s and ('М' + 'Р') not in s and \
    ('Р' + 'Х') not in s and ('Х' + 'Р') not in s and \
    ('С' + 'С') not in s and ('С' + 'М') not in s and ('М' + 'С') not in s and \
    ('С' + 'Х') not in s and ('Х' + 'С') not in s and \
    ('М' + 'М') not in s and ('М' + 'Х') not in s and ('Х' + 'М') not in s and \
    ('Х' + 'Х') not in s:
        k += 1
print(k)"""
    
"""from itertools import *
k = 0
for i in product('АНЮШК', repeat=5):
    s = ''.join(i)
    if s.count('А') >= 3:
        k += 1
        print(k, s)"""

"""from itertools import *
k = 0
for i in product('ДАНИЛ', repeat = 6):
    s = ''.join(i)
    if s.count('Д') == 1 and s.count('А') == 1 and s[-1] not in 'А':
        k += 1
        print(k, s)"""

"""from itertools import *

k = 0
for i in permutations('0123456', 6):
    s = ''.join(i)
    chet = '0246'
    nechet = '135'
    for j in range(len(s) - 1):
        da = True
        if not((s[j] in chet) != (s[j+1] in chet)):
            da = False
            break
    for h in range(len(s) - 1):
        ga = True
        if not((s[h] in nechet) != (s[h+1] in nechet)):
            ga = False
            break
    if s[0] != '0' and da == True and ga == True:
        k += 1
print(k)"""


"""k = set()
from itertools import *
for i in permutations('ДАНИССИМО', 9):
    s = ''
print(len(k))"""



"""from itertools import *
k = 0
for i in product('АЛЕКСЙ', repeat = 6):
    s = ''.join(i)
    if s.count('Й') <= 1 and ('Й' + 'А') not in s and ('А' + 'Й') not in s and \
    s[0] != 'Й' and s[-1] != 'Й':
        k += 1
        print(k, s)
"""


"""from itertools import *
k = set()
for i in permutations('ДЫНЬКА'):
    s = ''.join(i)
    if s[0] != 'Ь' and ('Ы' + 'Ь') not in s and \
    ('А' + 'Ь') not in s:
        k.add(''.join(i))
print(len(k))"""





        
    














from itertools import *

k = 0
for i in product('КАТЕР', repeat = 6):
    s = ''.join(i)
    if s[0] == 'Р' and s[-1] == 'К':
        k += 1
        print(k, s)





































        

    
























































































