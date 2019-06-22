
import hashlib
BLOCKSIZE = 65536
hasher = hashlib.md5()
with open('watermark.jpg', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())

import hashlib
BLOCKSIZE = 65536
hasher = hashlib.sha1()
with open('watermark.jpg', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(BLOCKSIZE)
print(hasher.hexdigest())

#The code above calculates the MD5 digest of the file. 
#The file is opened in rb mode, which means that you are going to read the file in binary mode. 
#This is because the MD5 function needs to read the file as a sequence of bytes. 
#This will make sure that you can hash any type of file, not only text files.
#It is important to notice the read function. 
#When it is called with no arguments, like in this case, it will read all the contents of the file and load them into memory. 
#This is dangerous if you are not sure of the file's size. 
