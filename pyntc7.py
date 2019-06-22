import json
from pyntc import ntc_device as NTC

iosvl2 = NTC(host='192.168.1.50', username='yasser', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()

ios_run = iosvl2.backup_running_config('R100.cfg')
