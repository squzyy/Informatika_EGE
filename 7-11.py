"""
A^L = количество разных серийных номеров, которые можно составить.
"""

"""fps = 10
xy = 1280 * 960
i = 11

gl = 1          # каналов (моно)
kod = 16        # глубина кодирования
gc = 32000      # частота дискретизации

kanal = 96468992
time = 200

# Размер данных за 1 секунду
V_izobr_1s = xy * i * fps
V_zvuka_1s = gl * kod * gc
V_obch_1s = V_izobr_1s + V_zvuka_1s

# Максимальный размер файла, который можно передать за 200 секунд
max_file_size = kanal * time

# Максимальная продолжительность видео
max_duration = max_file_size // V_obch_1s

print(max_duration)"""

"""xy = 640 * 480
fps = 24

mon = 1
gc = 24000           # 24 кГц = 24000 Гц
bt = 8
chas = 60 * 60          # секунд в часе

# Максимальный объём файла за час (25 Гбайт в битах)
V_chas_max = 25 * 1024 * 1024 * 1024 * 8

# Объём звука за час
V_zvuka_chas = mon * gc * bt * chas

# Максимальный объём видео за час
V_video_chas = V_chas_max - V_zvuka_chas

# Количество кадров за час
fps_per_hour = fps * chas

# Бит на пиксель
i = V_video_chas // (xy * fps_per_hour)

# Количество цветов
N = 2 ** i

print(N)"""


"""ster = 2
V_zvuka = 48 * 1024 * 1024 * 8

mon = 1
gc = V_zvuka // 2 * 1.5 // 3

DA = gc // 1024 // 1024 // 8
print(DA)"""


"""kanal_1 = 2 ** 23
kanal_2 = 2 ** 11

V_obch = 20 * 1024 * 1024 * 8

ogran_V = 1 * 1024 * 1024 * 8

V_kanal2 = V_obch // kanal_2

ogran = ogran_V // kanal_1

otv = V_kanal2 + ogran
print(otv)"""

"""chet = 4
grom = 8 
vrem = 8 * 60 + 32
V = 62.5 * 1024 * 1024 * 8

gc = V // grom // vrem // chet

print(gc)"""

"""import math

# Дано
alphabet_size = 10 + 27  # 37 символов
total_numbers = 3548
min_memory_kb = 12  # Кбайт
min_memory_bytes = min_memory_kb * 1024  # 12288 байт

# Вычисляем биты на символ
bits_per_symbol = math.ceil(math.log2(alphabet_size))  # 6

# Для каждого L считаем байт на номер и проверяем условие
# L = 4
L = 4
bits_per_number_4 = L * bits_per_symbol  # 24 бита
bytes_per_number_4 = math.ceil(bits_per_number_4 / 8)  # 3 байта
total_bytes_4 = total_numbers * bytes_per_number_4  # 10644
condition_4 = total_bytes_4 > min_memory_bytes  # False

# L = 5
L = 5
bits_per_number_5 = L * bits_per_symbol  # 30 бит
bytes_per_number_5 = math.ceil(bits_per_number_5 / 8)  # 4 байта
total_bytes_5 = total_numbers * bytes_per_number_5  # 14192
condition_5 = total_bytes_5 > min_memory_bytes  # True

# Результат
min_L = 5 if condition_5

print(f"Бит на символ: {bits_per_symbol}")
print(f"L = 4: {total_bytes_4} байт > {min_memory_bytes}? {condition_4}")
print(f"L = 5: {total_bytes_5} байт > {min_memory_bytes}? {condition_5}")
print(f"Минимальная длина серийного номера: {min_L}")"""

"""import math
alph = 10 + 26
simvol = 31
i = math.ceil(math.log2(alph))
users = 128
size = 12 * 1024

simvol_byt = math.ceil((simvol * i) / 8)
odin = size // users

otvet = odin - simvol_byt
print(otvet)"""

"""import math
alph = 10 + 17
nomers = 7564230
size = 31 * 1024 * 1024 * 8

i = math.ceil(math.log2(alph))

a = []
for L in range(1, 100):
    da = L * nomers * i
    if da > size:
        print(L)
        break"""
"""import math
alph = 4

i = math.ceil(math.log2(alph))

for l in range(1, 100):
    neda = alph ** l
    if neda >= 56:
        print(l)
        break"""
"""import math
dlina = 10
alf = 33
loshad = 52
diap = 1000

i = math.ceil(math.log2(alf))
i2 = math.ceil(math.log2(diap))
bit_na1 = math.ceil((i * dlina + i2) / 8)

otv = loshad * bit_na1
print(otv)"""

"""import math
alf = 8
dl = 48
i = math.ceil(math.log2(alf))
users = 250
size = 5750

na1 = size // users
simv_byt = math.ceil(i * dl / 8)

otv = na1 - simv_byt
print(otv)"""

"""import math
alf = 10 + 52 + 500
i = math.ceil(math.log2(alf))
nom = 45877
size = 49 * 1024 * 1024 * 8

for l in range(1, 1001):
    da = nom * i * l
    if da > size:
        print(l)
        break"""

"""import math

dl = 246
nomers = 703569
max_memory_bytes = 77 * 1024 * 1024

for a in range(1, 1000):
    # Сколько бит на символ?
    i = math.ceil(math.log2(a))

    # Сколько байт на один номер?
    bytes_per_number = math.ceil(dl * i / 8)

    # Сколько всего байт?
    total_bytes = nomers * bytes_per_number

    # Проверяем оба условия
    if a ** dl >= nomers and total_bytes <= max_memory_bytes:
        print(a)"""


"""import math

alf = 10 + 52 + 9
dl = 13
i = math.ceil(math.log2(alf))           # бит на символ
bits_per_password = i * dl               # бит на пароль
bytes_per_password = math.ceil(bits_per_password / 8)  # байт на пароль

login_bytes = 21
per_user = bytes_per_password + login_bytes
total = per_user * 600

print(total)"""
"""import math
dl = 55
alf = 127
i = math.ceil(math.log2(alf))
koli = 71902

bit_na_pas = math.ceil((dl * i))
otv = (koli * bit_na_pas) / 1024 / 1024 / 8
print(otv)"""

"""import math
alf = 10 + 52
i = math.ceil(math.log2(alf))
ind = 1000
size = 10 * 1024 * 8

for l in range(1, 10020):
    da = i * l * ind
    if da <= size:
        print(l)"""

"""import math
dl = 200
alf = 10 + 2040
i = math.ceil(math.log2(alf))
ind = 98304

size = i * dl * ind
print(size / 1024 / 8)"""

"""import math
dl = 172
nomers = 356_984
size = 54 * 1024 * 1024 * 8

for alf in range(1, 1000):
    i = math.ceil(math.log2(alf))
    da = dl * i * nomers
    if da >= size:
        print(alf)
        break"""
"""import math
dl = 42
alf = 11
i = math.ceil(math.log2(alf))
users = 320
size = 10 * 1024 * 8

resh = dl * i
resh_1 = size / users
otv = (resh_1 - resh) / 8
print(otv)"""
"""import math
dl = 4
alf = 26
i = math.ceil(math.log2(alf))      # 5 бит на букву
users = 10
bytes_per_password = math.ceil(dl * i / 8)   # 3 байта на пароль
otv = bytes_per_password * users              # 30 байт
print(otv)"""
"""import math
dl = 60
alf = 10 + 250
i = math.ceil(math.log2(alf))      # 9 бит на символ
ind = 65_536

bits_per_id = dl * i                # 540 бит
bytes_per_id = math.ceil(bits_per_id / 8)   # ceil(67.5) = 68 байт
total_bytes = bytes_per_id * ind
total_kb = total_bytes // 1024      # целое число Кбайт

print(total_kb)"""

"""import math

dl = 251  # длина идентификатора в символах
users = 796  # количество пользователей
limit_kb = 171  # лимит в Кбайт
limit_bytes = limit_kb * 1024  # 175104 байта

for alf in range(1, 10000):
    i = math.ceil(math.log2(alf))  # бит на символ
    bits_per_id = dl * i  # бит на идентификатор
    bytes_per_id = math.ceil(bits_per_id / 8)  # байт на идентификатор (целое число)
    total_bytes = bytes_per_id * users  # всего байт на всех

    if total_bytes > limit_bytes:  # строго больше 171 Кбайт
        print(alf)
        break"""

"""import math
alf = 10 + 17
i = math.ceil(math.log2(alf))
nomers = 7_564_230
size = 31 * 1024 * 1024

for l in range(1, 1000):
    da = i * l
    net = math.ceil(da / 8)
    dada = net * nomers
    if dada > size:
        print(l)
        break"""

"""import math

alf = 10 + 16
i = math.ceil(math.log2(alf))
nom = 7_564_230
size = 31 * 1024 * 1024

for l in range(1000, 1, -1):
    da = l * i
    net = math.ceil(da / 8)
    otv = nom * net
    if otv > size:
        print(l)"""
"""import math
dl = 31
alf = 10 + 26
i = math.ceil(math.log2(alf))
users = 128
size = 12 * 1024

odin = i * dl
od_byt = math.ceil(odin / 8)

na_od = size / users

otv = na_od - od_byt
print(otv)"""

"""import math
dl = 33
alf = 257
i = math.ceil(math.log2(alf))
ind = 2 ** 20

naod = dl * i
naod_byt = math.ceil(naod / 8)

size = naod_byt * ind
otv = size / 1024 / 1024
print(otv)"""

"""import math
dl = 116
alf = 16 + 2035
i = math.ceil(math.log2(alf))
ind = 65_536

na_od = dl * i
naod_byt = math.ceil(na_od / 8)

size = ind * naod_byt
otv = math.ceil(size / 1024 / 1024)

print(otv)"""
"""import math
dl = 197
ind = 178_080
size = 25 * 1024 * 1024

for alf in range(1000, 1, -1):
    i = math.ceil(math.log2(alf))
    naind = dl * i
    naind_byt = math.ceil(naind / 8)
    otv = naind_byt * ind
    if otv > size:
        print(alf)"""
"""import math
dl = 163
alf = 10 + 1500
i = math.ceil(math.log2(alf))
ind = 65_536

naod_bit = dl * i
naod_byt = math.ceil(naod_bit / 8)

size = naod_byt * ind
otv = math.ceil(size / 1024)

print(otv)"""

"""import math
dl = 200
alf = 10 + 2040
i = math.ceil(math.log2(alf))
ind = 98_304

nod_bit = dl * i
nod_byt = math.ceil(nod_bit / 8)

size = nod_byt * ind
otv = math.ceil(size / 1024)
print(otv)"""

"""import math
dl = 89
alf = 26 * 2
i = math.ceil(math.log2(alf))
dop = 23 * 8
ind = 1536

nod = (dl * i) + dop
nod_byt = math.ceil(nod / 8)

size = ind * nod_byt
otv = math.ceil(size / 1024)
print(otv)"""

"""import math
xy = 1920 * 1080
i = math.ceil(math.log2(32786))
pak = 300
U = 1474560

V = i * xy
odpak = V * pak
otv = odpak / U

print(otv / 60)"""