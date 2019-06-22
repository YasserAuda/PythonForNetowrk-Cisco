from netmiko import ConnectHandler

device = ConnectHandler(device_type='cisco_ios', ip='192.168.3.50', username='yasser', password='cisco')
output = device.send_command('show version')
print (output)
config_commands = ['config t', 'int loop 1', 'ip address 2.2.2.2 255.255.255.0']
output = device.send_config_set(config_commands)
print (output)
device.send_command("write memory")
device.disconnect()
