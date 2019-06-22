import json
from napalm import get_network_driver
bgplist = ['192.168.3.50' , '192.168.3.60']
for ip_address in bgplist:
    print("connection to " + str(ip_address))
    driver = get_network_driver('ios')
    iosvl2 = driver('ip_address', 'yasser', 'cisco')
    iosvl2.open()
    bgp_neighbors = iosvl2.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors,  indent=4))
    isovl2.close()
