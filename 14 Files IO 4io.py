import os 
if os.path.isfile("mycv.txt"):
   print('file exists')
mycv_file = open("mycv.txt", "w")
#print(type(mycv_file))
mycv_file.write("this is a test")
mycv_file.close()

