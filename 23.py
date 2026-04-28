"""def F(t, e):
    if t > e:
        return 0
    if t == e:
        return 1
    if t < e:
        return  F(t+1, e) + F(t + 3, e) + F(t*2, e)
print(F(1, 5))
def F(t, e):
    if t > e:
        return 0
    if t == e:
        return 1
    if t < e:
        return  F(t+1, e)+ F(t*2, e)
print(F(1, 10) * F(10, 20)) #траектория содержит число 10
# в обратную сторону
def F(t, e):
    if t < e:
        return 0
    if t == e:
        return 1
    if t > e:
        return  F(t-2, e)+ F(t//2, e)
print(F(28, 10) * F(10, 1)) #траектория содержит число 10
def F(x, y):
    if x > y or x == 17: # не содержит число 17
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x+2, y) + F(x+3, y) + F(x*2, y)
print(F(3, 10) * F(10, 25))

def F(x, y):
    if x < y or x == 13:
        return 0
    if x == y:
        return 1
    if x > y:
        return F(x-1, y) + F(x-2, y) + F(x//3, y)
print(F(19, 6) * F(6, 4))
# известно кол-во комманд
a = []
def F(x, y):
    if y > 9:
        return
    if y == 9:
        a.append(x)
        return
    F(x*2, y+1)
    F(x*2 + 1, y + 1)
F(1, 0)
print(len(set(a)))"""

"""def F(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return F(x+1, y) + F(x+2, y) + F(x*3, y)

# Через 15
a = F(6, 15) * F(15, 25)

# Через 21
b = F(6, 21) * F(21, 25)

# Через оба (15 И 21)
c = F(6, 15) * F(15, 21) * F(21, 25)

# Результат
result = a + b - 2 * c

print(result)"""

"""def F(x, y):
    if x < y or x == 13:
        return 0
    if x == y:
        return 1
    if x > y:
        return F(x-1, y) + F(x//2, y) + F(x//3, y)
print(F(26, 8) * F(8, 3))"""

"""def F(x, y):
    if x > y or x == 8: return 0
    if x == y: return 1
    if x < y:
        return F(x+2, y) + F(x*3, y)
a = F(2, 50) * F(50, 60)
print(a)"""

'''def F(x, y):
    if x < y or x == 12:
        return 0
    if x == y:
        return 1
    if x > y:
        return F(x-3, y) + F(x//2, y)
print(F(80, 23) * F(23, 3))'''

"""def F(x,y):
    if x > y or x == 13: return 0
    if x == y: return 1
    if x < y:
        return F(x + 1, y) + F(x*2, y) + F(x*3, y)
print(F(3, 8) * F(8, 18))"""

"""def F(x, y):
    if x < y or x == 8:
        return 0
    if x == y:
        return 1
    if x > y:
        return F(x-2, y) + F(x//2, y)
print(F(70, 22) * F(22, 5))
"""
"""def can_reach(start, target):
    if start > target:
        return False
    if start == target:
        return True
    # Иначе пробуем +3 или ×3
    return can_reach(start + 3, target) + can_reach(start * 3, target)

# Тогда для каждого нечётного n < 100 проверяем, достижимо ли оно из 10
count = 0
for n in range(1, 100):  # только нечётные
    if n % 2 != 0 and can_reach(10, n):
        count += 1
print(count)  # 26"""

"""def F(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return F(x-1, y) + F(x//2, y)
print(F(89, 30) * F(30, 7))"""

"""def F(x, y):
    if x > y or x == 7:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x + 1, y) + F(x + 3, y) + F(x * 2, y)
print(F(2, 15) * F(15, 25))"""

"""def F(x ,y):
    if x > y or x == 10:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x + 1, y) + F(x * 2, y)
print(F(1, 30))"""

"""a = []
def F(x, y):
    if y > 5:
        return
    if y == 5:
        a.append(x)
        return
    F(x*2, y+1)
    F(x+4, y + 1)
F(2, 0)
print(len(set(a)))"""


"""def F(x, y):
    if x > y or x == 35: return 0
    if x == y:
        return 1
    if x < y:
        return F(x+1, y) + F(x + 2, y) + F(x+4, y)
print(F(24, 33) * F(33, 42))"""

"""def F(x, y):
    if x > y or x == 321:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x+3, y) + F(x*2, y) + F(x*5, y)
print(F(7, 169) * F(169, 961))"""
"""def F(x, y):
    if x > y or x == 15:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x+1, y) + F(x*2, y) + F(x*3, y)
print(F(1, 11) * F(11, 25))"""

"""def F(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return F(x-2, y) + F(x-5, y)
print(F(24, 3))"""

"""def F(x, y):
    if x > y or x == 81:
        return 0
    if x == y:
        return 1
    if x < y:
        return F(x + int(str(x)[0]), y) + F(x+3, y) + F(2*x - 1, y)
print(F(42, 73) * F(73, 89))"""
"""def F(x, y):
  if x < y or x == 22: return 0
  if x == y: return 1
  if x > y: return F(x - 2, y) + F(x//2, y) + F(x//3, y)
print(F(40, 2))"""
"""def F(x, y):
  if x > y: return 0
  if x == y: return 1
  if x < y: return F(x + 2, y) + F(x * 2, y)
print(F(1, 18) * F(18, 52))"""
a = []
def F(x, y):
  if y > 4:
    return
  if y == 4:
    a.append(x)
    return
  F(x + 2, y+1)
  F(x * 3, y+1)
F(1, 0)
print(len(set(a)))