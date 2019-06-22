#CCIE/CCSI:Yasser Ramzy Auda
#https://www.facebook.com/yasser.auda
#https://www.linkedin.com/in/yasserauda/
#https://github.com/YasserAuda/PythonForNetowrk-Cisco

rtr = input('Enter Neighbor Device Type:')
Interface = input('Enter Local Interface Name:')
Speed = input('Enter Interface Speed Required:')
if ('hub' in rtr):
    print ('Remeber speed should be always auto')
elif ('10' in Speed) or ('100' in Speed):
    print ('you should set speed to auto')
else:
    print ('your setting is acceptable')

print ('\nExiting program...')
