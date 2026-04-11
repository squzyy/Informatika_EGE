"""# 19
def F(kamni, xod):
    if xod == 3 and kamni >= 29:
        return True
    if xod == 3 and kamni <= 29:
        return False
    if kamni >= 29:
        return False
    
    if xod % 2 == 0:
        return F(kamni + 1, xod + 1) or F(kamni * 2, xod + 1)
    else:
        return F(kamni + 1, xod + 1) and F(kamni * 2, xod + 1)

for kamni in range(1, 29):
    if F(kamni, 1):
        print(f'№_19: {kamni}')
# 20
def F(kamni, xod):
    if xod == 4 and kamni >= 29:
        return True
    if xod == 4 and kamni <= 29:
        return False
    if kamni >= 29:
        return False
    
    if xod % 2 == 1:
        return F(kamni + 1, xod + 1) or F(kamni * 2, xod + 1)
    else:
        return F(kamni + 1, xod + 1) and F(kamni * 2, xod + 1)

for kamni in range(1, 29):
    if F(kamni, 1):
        print(f'№_20: {kamni}')
#21
def F(kamni, xod):
    if (xod == 3 or xod == 5) and kamni >= 29:
        return True
    if xod == 5 and kamni <= 29:
        return False
    if kamni >= 29:
        return False
    
    if xod % 2 == 0:
        return F(kamni + 1, xod + 1) or F(kamni * 2, xod + 1)
    else:
        return F(kamni + 1, xod + 1) and F(kamni * 2, xod + 1)

for kamni in range(1, 29):
    if F(kamni, 1):
        print(f'№_21: {kamni}')
        break # так как 14 мы получили в 19"""


"""def F(k, x):
    if x == 3 and k <= 16:
        return True
    if x == 3 and k > 16:
        return False
    if k <= 16:
        return False
    
    if x % 2 == 0:
        return F(k - 3, x + 1) or F(k - 8, x + 1) or F(k // 3, x + 1)
    else:
        return F(k - 3, x + 1) and F(k - 8, x + 1) and F(k // 3, x + 1)

for k in range(17, 1000):
    if F(k, 1):
        print(f'№_19: {k}')

def F(k, x):
    if x == 4 and k <= 16:
        return True
    if x == 4 and k > 16:
        return False
    if k <= 16:
        return False
    
    if x % 2 == 1:
        return F(k - 3, x + 1) or F(k - 8, x + 1) or F(k // 3, x + 1)
    else:
        return F(k - 3, x + 1) and F(k - 8, x + 1) and F(k // 3, x + 1)

for k in range(17, 1000):
    if F(k, 1):
        print(f'№_20: {k}')

def F(k, x):
    if (x == 3 or x == 5) and k <= 16:
        return True
    if x == 5 and k > 16:
        return False
    if k <= 16:
        return False
    
    if x % 2 == 0:
        return F(k - 3, x + 1) or F(k - 8, x + 1) or F(k // 3, x + 1)
    else:
        return F(k - 3, x + 1) and F(k - 8, x + 1) and F(k // 3, x + 1)

for k in range(17, 1000):
    if F(k, 1):
        print(f'№_21: {k}')"""

"""def F(k1, k2, x):
    if (k1 + k2) >= 77 and x == 3:
        return True
    if (k1 + k2) < 77 and x == 3:
        return False
    if (k1 + k2) >= 77:
        return False
    
    if x % 2 == 0:
        return F(k1 + 1, k2, x + 1) or F(k1 * 2, k2, x + 1) or F(k1, k2 + 1, x + 1) or F(k1, k2 * 2, x + 1)
    else:
        return F(k1 + 1, k2, x + 1) or F(k1 * 2, k2, x + 1) or F(k1, k2 + 1, x + 1) or F(k1, k2 * 2, x + 1) # Неудачный ход в условии
    
for k2 in range(1, 70):
    if F(7, k2, 1):
        print(k2)"""


"""def F(k, x):
    if k >= 200 and x == 3:
        return True
    if k < 200 and x == 3:
        return False
    if k >= 200:
        return False
    
    if x % 2 == 0:
        return F(k + 1, x + 1) or F(k * 3, x + 1)
    else:
        return F(k + 1, x + 1) and F(k * 3, x + 1)
for k in range(1, 200):
    if F(k, 1):
        print(f'№_19: {k}')


def F(k, x):
    if k >= 200 and x == 4:
        return True
    if k < 200 and x == 4:
        return False
    if k >= 200:
        return False
    
    if x % 2 == 1:
        return F(k + 1, x + 1) or F(k * 3, x + 1)
    else:
        return F(k + 1, x + 1) and F(k * 3, x + 1)
for k in range(1, 200):
    if F(k, 1):
        print(f'№_20: {k}')

def F(k, x):
    if k >= 200 and (x == 3 or x == 5):
        return True
    if k < 200 and x == 5:
        return False
    if k >= 200:
        return False
    
    if x % 2 == 0:
        return F(k + 1, x + 1) or F(k * 3, x + 1)
    else:
        return F(k + 1, x + 1) and F(k * 3, x + 1)
for k in range(1, 200):
    if F(k, 1):
        print(f'№_21: {k}')"""

"""def F(k, x):
    if x == 2 and k >= 52:
        return True
    if x == 2 and k < 52:
        return False
    if k >= 52:
        return False
    
    if x % 2 == 1:
        return F(k + 1, x + 1) or F(k * 2, x + 1)
    else:
        return F(k + 1, x + 1) and F(k * 2, x + 1)
for k in range(1, 52):
    if F(k, 1):
        print(f'№_19: {k}')
        break

def F(k, x):
    if x == 3 and k >= 52:
        return True
    if x == 3 and k < 52:
        return False
    if k >= 52:
        return False
    
    if x % 2 == 0:
        return F(k + 1, x + 1) or F(k * 2, x + 1)
    else:
        return F(k + 1, x + 1) or F(k * 2, x + 1)
for k in range(1, 52):
    if F(k, 1):
        print(f'№_20: {k}')
        break

def F(k, x):
    if x == 4 and k >= 52:
        return True
    if x == 4 and k < 52:
        return False
    if k >= 52:
        return False
    
    if x % 2 == 1:
        return F(k + 1, x + 1) or F(k * 2, x + 1)
    else:
        return F(k + 1, x + 1) and F(k * 2, x + 1)
for k in range(1, 52):
    if F(k, 1):
        print(f'№_21: {k}')
        break"""


"""def F(k1, k2, x):
    if (x == 3 or x == 5) and (k1 + k2) <= 46:
        return True
    if (x == 3 or x == 5) and (k1 + k2) > 46:
        return False
    if (x == 2 or x == 4) and (k1 + k2) <= 46:
        return True
    if (x == 2 or x == 4) and (k1 + k2) > 46:
        return False
    if (k1 + k2) <= 46:
        return False
    
    if x % 2 == 0 and k1 % 2 == 0:
        return F(k1 - 2, k2, x + 1) or F(k1 // 2, k2, x + 1)
    if x % 2 == 0 and k1 % 2 != 0:
        return F(k1 - 2, k2, x + 1) or F(((k1 + 1) // 2), k2, x + 1)
    if x % 2 == 0 and k2 % 2 == 0:
        return F(k1, k2 - 2, x + 1) or F(k1, k2 // 2, x + 1)
    if x % 2 == 0 and k2 % 2 != 0:
        return F(k1, k2 - 2, x + 1) or F(k1, (k2 + 1) // 2, x + 1)
    
    if x % 2 == 1 and k1 % 2 == 0:
        return F(k1 - 2, k2, x + 1) or F(k1 // 2, k2, x + 1)
    if x % 2 == 1 and k1 % 2 != 0:
        return F(k1 - 2, k2, x + 1) or F(((k1 + 1) // 2), k2, x + 1)
    if x % 2 == 1 and k2 % 2 == 0:
        return F(k1, k2 - 2, x + 1) or F(k1, k2 // 2, x + 1)
    if x % 2 == 1 and k2 % 2 != 0:
        return F(k1, k2 - 2, x + 1) or F(k1, (k2 + 1) // 2, x + 1)
    
    return False

for k2 in range(27, 1000):
    k1 = 20
    
    moves = []
    if k1 >= 2:
        moves.append((k1 - 2, k2))
    if k1 % 2 == 0:
        moves.append((k1 // 2, k2))
    else:
        moves.append(((k1 + 1) // 2, k2))
    if k2 >= 2:
        moves.append((k1, k2 - 2))
    if k2 % 2 == 0:
        moves.append((k1, k2 // 2))
    else:
        moves.append((k1, (k2 + 1) // 2))
    for nk1, nk2 in moves:
        if nk1 + nk2 > 46:
            win = False
            if nk1 >= 2:
                if nk1 - 2 + nk2 <= 46:
                    win = True
            if nk1 % 2 == 0:
                if nk1 // 2 + nk2 <= 46:
                    win = True
            else:
                if (nk1 + 1) // 2 + nk2 <= 46:
                    win = True
            if nk2 >= 2:
                if nk1 + nk2 - 2 <= 46:
                    win = True
            if nk2 % 2 == 0:
                if nk1 + nk2 // 2 <= 46:
                    win = True
            else:
                if nk1 + (nk2 + 1) // 2 <= 46:
                    win = True
            
            if win:
                print(k2)
                break"""


"""def F(k, x):
    if x == 3 and k >= 33:
        return True
    if x == 3 and k < 33:
        return  False
    if k >= 33:
        return False

    if x % 2 == 0:
        return F(k + 3, x + 1) or F(k * 2, x + 1)
    else:
        return F(k + 3, x + 1) and F(k * 2, x + 1)

for k in range(1, 33):
    if F(k, 1):
        print(f'19: {k}')


def F(k, x):
    if x == 4 and k >= 33:
        return True
    if x == 4 and k < 33:
        return  False
    if k >= 33:
        return False

    if x % 2 == 1:
        return F(k + 3, x + 1) or F(k * 2, x + 1)
    else:
        return F(k + 3, x + 1) and F(k * 2, x + 1)
ss = 0
for k in range(1, 33):
    if F(k, 1):
        ss += 1
print(f'20: {ss}')

def F(k, x):
    if (x == 3 or x == 5) and k >= 33:
        return True
    if x == 5 and k < 33:
        return  False
    if k >= 33:
        return False

    if x % 2 == 0:
        return F(k + 3, x + 1) or F(k * 2, x + 1)
    else:
        return F(k + 3, x + 1) and F(k * 2, x + 1)

for k in range(1, 33):
    if F(k, 1):
        print(f'21: {k}')"""


"""def F(k, x):
    if x == 3 and k >= 36:
        # Вместо return True, проверяем кто выиграл
        return k < 60  # True только если Петя выиграл (k > 60)
    if x == 3 and k < 36:
        return False
    if k >= 36:
        # Если игра закончилась раньше x=3
        return k > 60  # True если выиграл Петя

    if x % 2 == 0:
        return F(k + 1, x + 1) or F(k * 2, x + 1) or F(k * 3, x + 1)
    else:
        return F(k + 1, x + 1) and F(k * 2, x + 1) and F(k * 3, x + 1)


for k in range(1, 36):
    if F(k, 1):
        print(k)"""

"""def F(k, x):
    if x == 3 and k >= 62:
        return True
    if x == 3 and k < 62:
        return False
    if k >= 62:
        return False

    if x % 2 == 0:
        return F(k + 1, x + 1) or F(k * 2, x + 1)
    else:
        return F(k + 1, x + 1) and F(k * 2, x + 1)

for k in range(1, 62):
    if F(k, 1):
        print(f'19: {k}')

def F(k, x):
    if x == 4 and k >= 62:
        return True
    if x == 4 and k < 62:
        return False
    if k >= 62:
        return False

    if x % 2 == 1:
        return F(k + 1, x + 1) or F(k * 2, x + 1)
    else:
        return F(k + 1, x + 1) and F(k * 2, x + 1)

for k in range(1, 62):
    if F(k, 1):
        print(f'20: {k}')

def F(k, x):
    if (x == 3 or x == 5) and k >= 62:
        return True
    if x == 5 and k < 62:
        return False
    if k >= 62:
        return False

    if x % 2 == 0:
        return F(k + 1, x + 1) or F(k * 2, x + 1)
    else:
        return F(k + 1, x + 1) and F(k * 2, x + 1)

for k in range(1, 62):
    if F(k, 1):
        print(f'21: {k}')"""

"""def F(k, x):
    if x == 3 and k <= 15:
        return True
    if x == 3 and k > 15:
        return False
    if k <= 15:
        return False

    if x % 2 == 0:
        return F(k - 3, x + 1) or F(k - 4, x + 1) or F(k // 2, x + 1)
    else:
        return F(k - 3, x + 1) and F(k - 4, x + 1) and F(k // 2, x + 1)

for k in range(17, 1000):
    if F(k, 1):
        print(f'19: {k}')

def F(k, x):
    if x == 4 and k <= 15:
        return True
    if x == 4 and k > 15:
        return False
    if k <= 15:
        return False

    if x % 2 == 1:
        return F(k - 3, x + 1) or F(k - 4, x + 1) or F(k // 2, x + 1)
    else:
        return F(k - 3, x + 1) and F(k - 4, x + 1) and F(k // 2, x + 1)

for k in range(17, 1000):
    if F(k, 1):
        print(f'20: {k}')

def F(k, x):
    if (x == 3 or x == 5) and k <= 15:
        return True
    if x == 5 and k > 15:
        return False
    if k <= 15:
        return False

    if x % 2 == 0:
        return F(k - 3, x + 1) or F(k - 4, x + 1) or F(k // 2, x + 1)
    else:
        return F(k - 3, x + 1) and F(k - 4, x + 1) and F(k // 2, x + 1)

for k in range(17, 1000):
    if F(k, 1):
        print(f'21: {k}')"""

"""def F(k, x):
    if x == 3 and k >= 229:
        return True
    if x == 3 and k < 229:
        return False
    if k >= 229:
        return False

    if x % 2 == 0:
        return F(k + 2 or 3 or 4, x + 1) or F(k * 2, x + 1)
    else:
        return F(k + 2 or 3 or 4, x + 1) and F(k * 2, x + 1)
for k in range(229):
    if F(k, 1):
        print(f'19: {k}')

def F(k, x):
    if x == 4 and k >= 229:
        return True
    if x == 4 and k < 229:
        return False
    if k >= 229:
        return False

    if x % 2 == 1:
        return F(k + 2 or 3 or 4, x + 1) or F(k * 2, x + 1)
    else:
        return F(k + 2 or 3 or 4, x + 1) and F(k * 2, x + 1)
for k in range(229):
    if F(k, 1):
        print(f'20: {k}')

def F(k, x):
    if (x == 3 or x == 5) and k >= 229:
        return True
    if x == 5 and k < 229:
        return False
    if k >= 229:
        return False

    if x % 2 == 0:
        return (F(k + 2, x + 1) or F(k + 3, x + 1) or F(k + 4, x + 1) or F(k * 2, x + 1))
    else:
        return (F(k + 2, x + 1) and F(k + 3, x + 1) and F(k + 4, x + 1) and F(k * 2, x + 1))

for k in range(1, 229):
    if F(k, 1):
        print(f'21: {k}')"""



"""def F(k1, k2, x):
    if x == 3 and (k1 + k2) >= 81:
        return True
    if x == 3 and (k1 + k2) < 81:
        return False
    if (k1 + k2) >= 81:
        return False

    if x % 2 == 0:
        return F(k1 + 1, k2, x + 1) or F(k1 + 2, k2, x + 1) or F(k1 * 2, k2, x + 1)
    else:
        return F(k1 + 1, k2, x + 1) and F(k1 + 2, k2, x + 1) and F(k1 * 2, k2, x + 1)

for k2 in range(1, 69):
    if F(12, k2, 1):
        print(f'19: {k2}')

def F(k1, k2, x):
    if x == 4 and (k1 + k2) >= 81:
        return True
    if x == 4 and (k1 + k2) < 81:
        return False
    if (k1 + k2) >= 81:
        return False

    if x % 2 == 1:
        return F(k1 + 1, k2, x + 1) or F(k1 + 2, k2, x + 1) or F(k1 * 2, k2, x + 1)
    else:
        return F(k1 + 1, k2, x + 1) and F(k1 + 2, k2, x + 1) and F(k1 * 2, k2, x + 1)

for k2 in range(1, 69):
    if F(12, k2, 1):
        print(f'20: {k2}')

def F(k1, k2, x):
    if (x == 3 or x == 5) and (k1 + k2) >= 81:
        return True
    if x == 5 and (k1 + k2) < 81:
        return False
    if (k1 + k2) >= 81:
        return False

    if x % 2 == 0:
        return F(k1 + 1, k2, x + 1) or F(k1 + 2, k2, x + 1) or F(k1 * 2, k2, x + 1)
    else:
        return F(k1 + 1, k2, x + 1) and F(k1 + 2, k2, x + 1) and F(k1 * 2, k2, x + 1)

for k2 in range(1, 69):
    if F(12, k2, 1):
        print(f'21: {k2}')"""

def F(k1, k2, x):
    if x == 3 and (k1 + k2) >= 131:
        return True
    if x == 3 and (k1 + k2) < 131:
        return False
    if (k1 + k2) >= 131:
        return False

    if x % 2 == 0:
        return F(k1 + 2, k2, x + 1) or F(k1 * 2, k2, x + 1) or F(k1, k2 + 2, x + 1) or F(k1, k2 * 2, x + 1)
    else:
        return F(k1 + 2, k2, x + 1) or F(k1 * 2, k2, x + 1) or F(k1, k2 + 2, x + 1) or F(k1, k2 * 2, x + 1)

for k2 in range(1, 120):
    if F(11, k2, 1):
        print(f'19: {k2}')
        break


def F(k1, k2, x):
    if x == 4 and (k1 + k2) >= 131:
        return True
    if x == 4 and (k1 + k2) < 131:
        return False
    if (k1 + k2) >= 131:
        return False

    if x % 2 == 1:
        return F(k1 + 2, k2, x + 1) or F(k1 * 2, k2, x + 1) or F(k1, k2 + 2, x + 1) or F(k1, k2 * 2, x + 1)
    else:
        return F(k1 + 2, k2, x + 1) and F(k1 * 2, k2, x + 1) and F(k1, k2 + 2, x + 1) and F(k1, k2 * 2, x + 1)

for k2 in range(1, 120):
    if F(11, k2, 1):
        print(f'20: {k2}')

def F(k1, k2, x):
    if (x == 3 or x == 5) and (k1 + k2) >= 131:
        return True
    if x == 5 and (k1 + k2) < 131:
        return False
    if (k1 + k2) >= 131:
        return False

    if x % 2 == 0:
        return F(k1 + 2, k2, x + 1) or F(k1 * 2, k2, x + 1) or F(k1, k2 + 2, x + 1) or F(k1, k2 * 2, x + 1)
    else:
        return F(k1 + 2, k2, x + 1) and F(k1 * 2, k2, x + 1) and F(k1, k2 + 2, x + 1) and F(k1, k2 * 2, x + 1)

for k2 in range(1, 120):
    if F(11, k2, 1):
        print(f'21: {k2}')























print('Андрей лох')