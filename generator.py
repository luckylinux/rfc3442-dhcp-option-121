#!/usr/bin/env python3

# Import the ipaddress module
from ipaddress import *

# Import the static routes definition
from routes import routes

# Declare bytes array
route_bytes = []

# Loop over all Routes and build the required String
for dest, router in routes:
    netmask_cidr = int(dest.split("/")[-1])
    destnet = ip_network(dest)
    dest = list(destnet.network_address.packed)
    netmask = destnet.netmask.packed

    for octet in netmask[::-1]:
        if octet == 0:
            dest = dest[:-1]

    router = list(ip_address(router).packed)

    route_bytes += [netmask_cidr]
    route_bytes += dest
    route_bytes += router

# Variant 1
var1=''.join([f'{o:02x}' for o in route_bytes])
print(f'Variant 1                                   : 0x{var1}')

# Variant 2
var2=':'.join([f'{o:02x}' for o in route_bytes])
print(f'Variant 2 (OPNSense, PFSense, Ubiquiti, ...):   {var2}')
