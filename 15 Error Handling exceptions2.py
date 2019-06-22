def main():
  try:
    for line in readfile('xlines.txt'): print(line.strip())
  except FileNotFoundError as e:
    print("cannot read file:",e)	  
def readfile(filename):
    fh = open(filename)
    return fh.readlines()

if __name__ == "__main__": main()

#without rise exceptions
#def main():
#    for line in readfile('xlines.txt'): print(line.strip())
	  
#def readfile(filename):
#    fh = open(filename)
#   return fh.readlines()

#if __name__ == "__main__": main()
