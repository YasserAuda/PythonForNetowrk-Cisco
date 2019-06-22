#Regular expressions are used for a variety of purposes, from simple search and replace operations to complex text and data file manipulation.
#Regular expressions are actually a small language in itself.
#This is Python's regular expression module and it's distributed with Python.
#You import re module and you compile a pattern and then you use the pattern to search.

import re

def main():
    fh = open('Router0_startup-config.txt')
    for line in fh:
        match = re.search('(Cisco|cisco)', line)
        if match:
            print (line.replace(match.group(), '###'), end =' ') 
if __name__ == "__main__": main()
