'''
def fact(x) :
  facto = 1
  while x > 0 :
    facto = facto * x
    x = x - 1
  return facto

i = int(input("Enter"))
print(fact(i))
'''

# With Recursion

def fact(n) :
  if n == 1 or n == 0 :
    return 1
  return n * fact(n - 1)

print (fact (int(input('Num: '))))