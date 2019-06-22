#CCIE/CCSI:Yasser Ramzy Auda
#https://www.facebook.com/yasser.auda
#https://www.linkedin.com/in/yasserauda/
#https://github.com/YasserAuda/PythonForNetowrk-Cisco

#Example 1
X=100
Z=2
A='is your score Yasser'
Z=X*Z
device=""" Cisco R1
in subnet100 """
B='\'this test\''
print(Z)
print(A)
print(device)
print(B)
#Example 2 User Defined Function
def myf1(num1,num2):
    answer = num1 + num2
    print('num1 is ' ,num1)
    print(answer)
myf1(1,3)

#Example 3 Print Text with Numbers ( Intgers with strings)
A="The Result is ="
B=1490+10
C="Bytes MTU"
print (A+str(B)+str(C))

#Example 4 useing Input Function
firstname=input("what is your name?")
print("Hi "+firstname+"!")

#Example 5 useing format method tied with int
#Format 255 into a hexadecimal value:
#format(value, format)


a = format(255, 'x')
print(a)

a = format(255, 'X')
print(a)


a = format(0.5, '%')
print(a)








