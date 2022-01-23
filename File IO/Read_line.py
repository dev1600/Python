import os
f=open('File IO/sample.txt')
# Read the 1st line 
data=(f.readline())
print(data[5:9])
# Read the 2nd line
data=f.readline()
# default type of file data
print(type(data))
print(data)
f.close()