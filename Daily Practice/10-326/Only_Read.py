#read:display the file content as it is
#readline:display single line of data at a time
file=open("temp1.txt",'r')
# print(file.read())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.close()