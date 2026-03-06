'''
Write a Python function that takes four parameters and prints them. Then call the function by unpacking a string using the * operator, so that each character of the string is passed as a separate argument to the function.
'''

def unpack(a, b, c, d):
  print (a, b, c, d)
unpack(*'shiv')