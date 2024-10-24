from sys import stdin
from ipaddress import IPv4Network

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    n = Input()
    net = IPv4Network(n, False)
    print(f'{net.network_address}/{net.broadcast_address}')
