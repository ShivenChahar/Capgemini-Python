'''
Write a Python function that takes two inputs from the user:
-A string
-A character
The function should search for the given character in the string and print all the index positions where that character appears
'''

def fun (a, b) :
  for i in range (0, len(a)) :
    if a[i] == b :
      return i 

a = input("Enter String")
b = input("Enter Character")
print(fun(a, b)) 