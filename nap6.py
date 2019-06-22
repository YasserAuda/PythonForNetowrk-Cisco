from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('192.168.3.51', 'yasser', 'cisco')
iosvl2.open()
print('Accessing 192.168.3.51')
iosvl2.load_merge_candidate(filename='ACL.cfg')
iosvl2.commit_config()
isovl2.close
