def form (name, mail,ph, age = 20, alt_phn = None) :
  print ('Name is: ', name)
  print ('Mail is: ', mail)
  print ('Phone is: ', ph)
  print ('Age is: ', age) 
  print ('Alt-Phn: ', alt_phn)
#form('Shiven', 'shiven@gmail.com', 9799824111)
form('Shiven', 'shiven@gmail.com', 9799824111, 22)   # if we give new value to the age again in the function argument...then the intial given value will be overwritten by the new argument. 


'''
There are 5 Types of Arguments :
1. Positional Arguments
2. Keyword Arguments
3. Default Arguments
4. Variable-Length Arguments (args)
5. Keyword Variable-Length Arguments (*kwargs)
'''