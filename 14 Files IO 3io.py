import os
file_created = os.path.getctime("mycv.txt")
print("this file was created {} seconds after the unix epoch.".format(file_created))

