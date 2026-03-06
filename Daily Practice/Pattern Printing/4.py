'''
***#
**#@
*#@@
#@@@
'''
a = int(input('Enter Row= '))
b = int(input('Enter Col= '))
for i in range (1,a+1) :
  for j in range (1,b+1) :
    if ( i + j == a + 1) :
      print ('#', end="")
    elif (i + j < a + 1) :
      print ('*',end="")
    else :
      print (end="@")
  print()