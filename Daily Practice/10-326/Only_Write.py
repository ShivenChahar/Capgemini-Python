file=open('temp1.txt','w+')
file.write('I am The new data\n')
file.writelines(["I am the new line\n","Second line\n","Third Line\n"])
file.writelines(["first line 1\n",
                 "second line 2\n",
                 "third line 3\n",
                 "fourth line 4\n"])
print(file.read())
file.close()
