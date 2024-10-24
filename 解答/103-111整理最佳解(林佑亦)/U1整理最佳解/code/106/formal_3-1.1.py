from sys import stdin
from ipaddress import IPv4Network

def Input():
    return stdin.readline().strip()

for _ in range(int(Input())):
    n = Input()
    net = IPv4Network(n, False)
    print(net.broadcast_address)

