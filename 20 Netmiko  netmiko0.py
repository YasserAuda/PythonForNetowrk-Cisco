#!/usr/bin/env python

from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.3.50',
    'username': 'yasser',
    'password': 'cisco',
}


net_connect = ConnectHandler(**iosv_l2)
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print (output)
output = net_connect.send_command('show version | in uptime')

print (output)
 
