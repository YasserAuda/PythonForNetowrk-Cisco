#Example 1
def main():
    testfunc()

def testfunc():
    pass

if __name__ == "__main__": main()

#Example 2
def main():
    testfunc()

def testfunc():
    print('This is a test function')

if __name__ == "__main__": main()

#Example 3 , to pass argument to our function
def main():
    testfunc(42)

def testfunc(num):
    print('This is a test function', num)

if __name__ == "__main__": main()

#Example 4
def main():
    testfunc(42, 9)

def testfunc(num, num2):
    print('This is a test function', num, num2)

if __name__ == "__main__": main()

#Example 5
def main():
    testfunc(42)

def testfunc(num, num2 = 9):
    print('This is a test function', num, num2)

if __name__ == "__main__": main()

#Example 6
def main():
    testfunc(42, 10)

def testfunc(num, num2 = 9):
    print('This is a test function', num, num2)

if __name__ == "__main__": main()

#Example 7
def main():
    testfunc(42)

def testfunc(num, num2 = None):
    if num2 is None:
        num2 = 10
    print('This is a test function', num, num2)

if __name__ == "__main__": main()

#Example 8
#The asterisk is special in this place as it means that this is just a list of optional arguments
def main():
    testfunc(1, 2, 3, 4, 5, 6, 7)

def testfunc(n1, n2, n3, *args):
    print(n1, n2 ,n3)

if __name__ == "__main__": main()

#Example 9
#args will be tuple
def main():
    testfunc(1, 2, 3, 4, 5, 6, 7)

def testfunc(n1, n2, n3, *args):
    print(n1, n2 ,n3, args)

if __name__ == "__main__": main()

#*args and **kwargs are mostly used in function definitions.
#*args and **kwargs allow you to pass a variable number of arguments to a function. 
#What variable means here is that you do not know beforehand how many arguments can 
#be passed to your function by the user so in this case you use these two keywords.

#Example 10
def main():
    testfunc(n1 = 1, n2 =2)

def testfunc(**kwargs):
    print('This is a test function', kwargs['n1'], kwargs['n2'])

if __name__ == "__main__": main()

#arguments are not named on the receiving end,So these are specified 
#with the two asterisks and very commonly called kwargs
##kwargs is actually a dictionary and so I can say kwargs sub 'n1', like 
#that, and kwargs sub 'n2' then I save these and run it,

#Example 11
def main():
    print(testfunc())

def testfunc():
    return 'This is a test function'

if __name__ == "__main__": main()


#Example 12
def main():
    print(testfunc())

def testfunc():
    return 42

if __name__ == "__main__": main()
#Example 13
def main():
    print(testfunc())

def testfunc():
    return range(25)

if __name__ == "__main__": main()

#Example 124
def main():
    for n in testfunc(): print(n, end= ' ')

def testfunc():
    return range(25)

if __name__ == "__main__": main()


