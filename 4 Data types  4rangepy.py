#Range


x = range(6)
for n in x:
  print(n) 
  
  
for n in range(1, 7): 
	print  ('number ')
	print (n)

import subprocess
import os

for n in range(1, 10):
    ip="192.168.1.{0}".format(n)
    subprocess.call(["ping", ip])
