# sorted (a = sorted([int(x) for x in i.split()]))), set - это когда все числа разные (if len(a) == len(set(a)))
'''
cnt = 0
for i in open('da.txt'):
    a = sorted([int(x) for x in i.split()])
    if (a[0] + a[2])**2 > a[1]**2 :
        cnt += 1
print(cnt)
'''
'''
a = [12, 102, 26, 102, 21, 12, 73]
da = [x for x in a if a.count(x) == 2] # только те эелементы которые повторяются 2 раза
da_1 = [x for x in a if a.count(x) == 1] # уникальные
if len(da) == 4 and len(da_1) == 3: # тут крч 4 и 3 это общее количество наших числе в скобках (сделано чтоб среднее арефметичское посчитать)
    if sum(da) / len(da): # среднее арефметическое
        print(da) 
'''   
'''
cnt = 0
for i in open('da.txt'):
    a = ([int(x) for x in i.split()])
    if len(a) == len(set(a)):
        if sum(a) % 3 == 0:
            cnt += 1
print(cnt)
'''
'''
k = 0
for i in open('da.txt'):
    a = sorted([int(x) for x in i.split()])
    if sum(a) > a[2]*2:
        k +=1
print(k)
'''
k = 0
for i in open('da.txt'):
    a = ([int(x) for x in i.split()])
    da_b = sum(x for x in a if x > 0)
    da_m = sum(x for x in a if x < 0)
    count3 = sum(1 for x in a if abs(x) % 10 == 3) # квадрат суммы положительных чисел меньше квадрата суммы отрицательных чисел. (abs() - это модуль)
    if count3 == 3 and da_b**2 < da_m**2:
        k += 1
print(k)