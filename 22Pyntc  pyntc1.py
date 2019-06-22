#pip install urllib3
#pip install pyntc
import json
from pyntc import ntc_device as NTC

iosvl2 = NTC(host='192.168.1.50', username='yasser', password='cisco', device_type='cisco_ios_ssh')
iosvl2.open()

ios_output =iosvl2.facts
print(json.dumps(ios_output, indent=4))
