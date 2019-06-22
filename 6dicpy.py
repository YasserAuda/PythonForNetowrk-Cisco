


dict = {"R1":2911, "R2":2811, "R3":2911}
print(dict["R2"])
dict["R4"] = 1841
print(dict)

service = {"FTP":21,"SSH":22, "SMTP":25, "HTTP":80}
dir(service)
print(service.keys())
print(service.items())

dict2 = {"SW1VLAN":[123,456,789]}
print(dict2)


mydict={"R1":"10.0.0.1", "R2":"10.0.0.2", "R3":"10.0.0.3"}
print(mydict["R2"])

myinterface={'interface Loopback0': [                        
    'ip address 10.10.10.10 255.255.255.255',  
    'ip flow ingress',                         
    'h323-gateway voip interface',               
    'h323-gateway voip bind srcaddr 10.10.10.10',
    ]}
print(myinterface)

#Add a Key-Value Pair to the Dictionary 
key=str(input("Enter the Device name to be added:"))
value=int(input("Enter the Device model to be added:"))
d={}
d.update({key:value})
print("Updated dictionary is:")
print(d)

#we can change str  to int
