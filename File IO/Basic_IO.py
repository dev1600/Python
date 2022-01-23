import os
# Open to read the content of a file 
# r is default mode 
f=open("File IO/sample.txt",'r')
# To get first 5 characters of file
data=f.read(5)
print(data)
f.close()
# print(os.listdir())
# print(os.getcwd())
