import os
# with is the best to perform IO operation in python
# as the file will automatically close with statement
with open("File IO/sample.txt",'r') as f:
    print(f.read())
with open('File IO/sample.txt','a') as f:
    f.write("\nHello")