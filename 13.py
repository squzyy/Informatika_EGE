# network_address - Сетевой адрес — идентификатор устройства, работающего в компьютерной сети
# Широковещательный адрес — условный адрес, который используется для передачи широковещательных пакетов в компьютерных сетях.
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

