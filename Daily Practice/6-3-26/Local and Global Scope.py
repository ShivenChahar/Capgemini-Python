def fname () :
  global a 
  a = 100
  b = 50
  print(a + b)
  def fname2() :
    nonlocal b
    b = 300
    print(b)
  fname2()
  print(b)
fname()
# print(b)
print(a)