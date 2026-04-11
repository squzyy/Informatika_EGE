"""# network_address - Сетевой адрес — идентификатор устройства, работающего в компьютерной сети
# Широковещательный адрес — условный адрес, который используется для передачи широковещательных пакетов в
компьютерных сетях."""
"""
print('.'.join(bin(x)[2:].zfill(8) for x in [215,181,200,27]))
print('.'.join(bin(x)[2:].zfill(8) for x in [215,181,192,0]))

from ipaddress import *

for m in range(1, 31 + 1):
    ip = ip_network(f'215.181.200.27/{m}', 0)
    print(ip, ip.netmask) # например нужно определить како-то бит маски там число бим бам бум пон?

"""

"""from ipaddress import *

for m in range(1, 33):
    ip = ip_network(f'76.155.48.2/{m}', 0)
    print(ip)"""

"""from ipaddress import *

for m in range(1, 31 + 1):
    ip = ip_network(f'108.133.75.91/{m}', 0)
    print(ip, ip.num_addresses) # КОЛИЧЕСТВО АДРЕСОВ СЕТЕЙ"""

"""from ipaddress import *


for m in range(33):
    ip1 = ip_network(f'157.127.182.76/{m}', 0)
    ip2 = ip_network(f'157.127.190.80/{m}', 0)
    if ip1 != ip2:
        print(ip1)"""

"""from ipaddress import *

for m in range(33):
    ip1 = ip_network(f'118.187.59.255/{m}', 0)
    ip2 = ip_network(f'118.187.65.115/{m}', 0)
    if ip1 != ip2:
        if ip_address('118.187.59.255') != ip1.broadcast_address and \
        ip_address('118.187.59.255') != ip1.network_address and \
        ip_address('118.187.65.115') != ip2.broadcast_address and \
        ip_address('118.187.65.115') != ip2.network_address:
            print(ip1, 32-m)"""
"""from ipaddress import *       
net = ip_network('105.224.200.224/255.255.255.224', 0)
k = 0
for ip in net:
    s = f'{ip:b}'
    d = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 4 == 0:
        k += 1
print(k)
"""

"""from ipaddress import *
net = ip_network('45.172.106.203/255.255.252.0', 0)
print(net[-2])"""

"""from ipaddress import *
k = 0
net = ip_network('172.30.0.0/255.254.0.0', 0)
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 12 != 0:
        k += 1
print(k)"""



"""from ipaddress import *

for m in range(33):
    net = ip_network('45.172.106.203/255.255.252.0', 0)
    print(net[-2])"""

"""from ipaddress import *

for m in range(33):
    ip = ip_network(f'117.73.208.27/{m}', 0)
    print(ip)"""

"""from ipaddress import *

net = ip_network('191.128.66.83/255.192.0.0', 0)
print(net[-2])"""

"""from ipaddress import *

for m in range(33):
    ip = ip_network(f'172.17.67.127/{m}', 0)
    print(ip, ip.netmask)"""

"""from ipaddress import *

net = ip_network('190.202.83.62/255.255.252.0', 0)
print(net[-2])
print(net[1])
print(190 + 190 + 202 + 202 + 83 + 80 + 254 + 1)"""

"""from ipaddress import *

for m in range(33):
    ip = ip_network(f'111.81.27.84/{m}', 0)
    print(ip, ip.netmask)"""


"""from ipaddress import *

for m in range(33):
    ip = ip_network(f'133.57.64.130/{m}', 0)
    print(ip, ip.netmask)"""

"""from  ipaddress import *

for m in range(33):
    ip1 = ip_network(f'200.154.190.12/{m}', 0)
    ip2 = ip_network(f'200.154.184.0/{m}', 0)
    if ((ip_address('200.154.190.12') != ip1.broadcast_address and \
        ip_address('200.154.190.12') != ip1.network_address) and \
        (ip_address('200.154.184.0') != ip2.broadcast_address and \
        ip_address('200.154.184.0') != ip2.network_address)):
        print(ip1, ip1.netmask)"""


"""from ipaddress import *
ip1 = ip_address('200.154.190.12')
ip2 = ip_address('200.154.184.0’)
for m in range(33):
 net1 = ip_network(f'200.154.190.12/{m}', 0)
 net2 = ip_network(f'200.154.184.0/{m}', 0)
 if net1==net2 and ip1 not in [net1[0],net1[-1]] and ip2 not
in [net2[0],net2[-1]]:
  print(net1)"""


"""from ipaddress import *

ip1 = ip_address('201.44.240.33')
ip2 = ip_address('201.44.240.107')
k = 0
for m in range(33):
    net1 = ip_network(f'201.44.240.33/{m}', 0)
    net2 = ip_network(f'201.44.240.107/{m}', 0)
    if net1 == net2:
        d = net1.network_address
        s = net1.network_address
        g = bin(int(d))[2:].zfill(32)
        l = bin(int(s))[2:].zfill(32)
        if g.count('1') >= 5 and l.count('1') >= 5:
            k += 1
            print(k)"""

"""from ipaddress import *

net = ip_network('98.81.154.195/255.252.0.0', 0)
print(net[-2])"""

"""from ipaddress import *
k = 0
net = ip_network('172.16.168.0/255.255.248.0', 0)
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 5 != 0:
        k += 1
        print(k)"""

"""from ipaddress import *

net = ip_network('203.111.195.0/255.255.240.0', 0)
k = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('0') % 3 == 0 and '111' in s and '000' in s:
        k += 1
        print(k)"""

"""from ipaddress import *

net = ip_network('123.22.111.192/255.255.255.248', 0)
k = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s[-8:].count('0') % 3 != 0:
        k += 1
        print(k)"""

"""from ipaddress import *

net = ip_network('191.128.66.83/255.192.0.0', 0)
print(net[-2])"""

"""from ipaddress import *

net = ip_network('172.95.116.174/255.255.192.0', 0)
print(net[1])
print(172+95+64+1)"""

"""from ipaddress import *
a = []
net = ip_network('192.168.12.207/255.192.0.0', 0)
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('0') == s.count('1'):
        a.append(ip)
print(max(a))"""

"""from ipaddress import *

net = ip_network('46.29.170.214/255.255.128.0', strict=False)
a = []

for ip in net.hosts():
    # Получаем октеты как числа
    octets = str(ip).split('.')
    d1 = int(octets[0])  # 46
    d2 = int(octets[1])  # 29
    d3 = int(octets[2])  # c
    d4 = int(octets[3])  # d

    # Проверяем: один октет = сумма трёх других
    if (d1 == d2 + d3 + d4 or
            d2 == d1 + d3 + d4 or
            d3 == d1 + d2 + d4 or
            d4 == d1 + d2 + d3):
        a.append(ip)

print(max(a))"""


"""from ipaddress import *

for m in range(33):
    ip1 = ip_network(f'200.154.190.12/{m}', 0)
    ip2 = ip_network(f'200.154.184.0/{m}', 0)
    if ip1 == ip2:
        if ip_address('200.154.190.12') != ip1.broadcast_address and ip_address('200.154.190.12') != ip1.network_address and ip_address('200.154.184.0') != ip2.broadcast_address and ip_address('200.154.184.0') != ip2.network_address:
            print(ip1)"""


"""from ipaddress import *
for m in range(32, 0, -1):
    net = ip_network(f'143.131.211.37/{m}', 0)
    k = 0
    for ip in net:
        s = bin(int(ip))[2:].zfill(32)
        if s.count('1') == 10:
            k += 1
    if k == 15:
        print(net)
        break
"""



"""from ipaddress import *

for A in range(256):
    da = True
    net = ip_network(f'192.214.{A}.184/255.255.255.224', 0)
    for ip in net:
        if bin(int(ip)).count('1') <= 15:
            da = False
            break
    if da == True:
        print(A)
        break"""


from ipaddress import *

for m in range(33):
    ip = ip_network(f'218.159.208.24/{m}', 0)
    print(ip, ip.netmask)