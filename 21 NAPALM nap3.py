import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.3.50', 'yasser', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
print (json.dumps(ios_output,  indent=4))


ios_output = iosvl2.get_interfaces()
print (json.dumps(ios_output, sort_keys=True,  indent=4))

ios_output = iosvl2.get_interfaces_counters()
print (json.dumps(ios_output,  indent=4))

ios_output = iosvl2. get_interfaces_ip()
print (json.dumps(ios_output,  indent=4))

ios_output = iosvl2. get_config()
print (json.dumps(ios_output,  indent=4))

ios_output = iosvl2.ping('google.com')
print (json.dumps(ios_output,  indent=4))
