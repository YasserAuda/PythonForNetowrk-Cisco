#List

years = [2000, 2001, 2002]
print(years)
Repeatable = [2000, 2001, 2000]
print(Repeatable)
mix = [2000, "yasser", 2002]
print(mix)

x = ["A", "B", "C"]
y = ["D", "E"]
z = x + y
print(z)
z = x * 3
print(z)
z = "A" in y
print(z)

fastethernet_speed=['auto', '10', '100']
print(fastethernet_speed)
print(fastethernet_speed[0])

portList = []
portList.append(21)
portList.append(80)
portList.append(443)
portList.append(25)
print(portList)

portList.sort()
print(portList)

pos = portList.index(80)
print ("[+] There are "+str(pos)+" ports to scan before 80.")
portList.remove(443)
print(portList)

test = 'CCIE CCNP CCNA and CCNT'
print(test.split())



fastethernet_duplex = 'auto half full'
fastethernet_duplex_list = fastethernet_duplex.split()
print(fastethernet_duplex_list)
  
fastethernet_duplex_list[0] = 'Auto'
fastethernet_duplex_list[1] = 'Half'
fastethernet_duplex_list[2] = 'Full'
print(fastethernet_duplex_list)
print(fastethernet_duplex_list[0])

del fastethernet_duplex_list[0]
print(fastethernet_duplex_list)
 
print('Auto' in fastethernet_duplex_list)
