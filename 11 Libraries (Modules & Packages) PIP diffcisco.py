#CCIE/CCSI:Yasser Ramzy Auda
#https://www.facebook.com/yasser.auda
#https://www.linkedin.com/in/yasserauda/
#https://github.com/YasserAuda/PythonForNetowrk-Cisco

#pip install diffios

#diffios is a Python library that provides a way to compare Cisco IOS 
#configurations against a baseline template, and generate an output 
#detailing the differences between them.

#https://github.com/robphoenix/diffios

import diffios
baseline = "R1.txt"
comparison = "R2.txt"
ignore = "ignore.txt"

diff = diffios.Compare(baseline, comparison, ignore)
print(diff.delta())
