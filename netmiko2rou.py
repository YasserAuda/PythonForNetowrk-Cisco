#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '10.6.0.50',
    'username': 'yasser',
    'password': 'cisco',
}


iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '10.6.0.51',
    'username': 'yasser',
    'password': 'cisco',
}
with open('iosv_l2_config1.txt') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [iosv_l2_s1, iosv_l2_s2]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output) 
