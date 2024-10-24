from sys import stdin
from ipaddress import IPv4Network

def Input():
    return stdin.readline().rstrip()

for _ in range(int(Input())):
    s = Input()
    net = IPv4Network(s, False)
    print(net.network_address, '/', net.broadcast_address, sep='')

