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