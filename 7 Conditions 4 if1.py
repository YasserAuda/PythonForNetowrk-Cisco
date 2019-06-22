#CCIE/CCSI:Yasser Ramzy Auda
#https://www.facebook.com/yasser.auda
#https://www.linkedin.com/in/yasserauda/
#https://github.com/YasserAuda/PythonForNetowrk-Cisco


rtr = input('Enter the hostname:')
vendor = input('Enter the type of device:')
if ('Hawaii' in vendor) or ('hawaii' in vendor):
    print ('display current')
elif ('Juniper' in vendor) or ('juniper' in vendor):
    print ('sh configuration')
else:
    print ('sh run')
    
print ('\nExiting program...')
