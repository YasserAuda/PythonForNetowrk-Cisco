import getpass
p = getpass.getpass(prompt='What is your password? ')
if p.lower() == 'cisco':
    print ('Right.  Off you go.')
else:
    print ('Auuuuugh!')

