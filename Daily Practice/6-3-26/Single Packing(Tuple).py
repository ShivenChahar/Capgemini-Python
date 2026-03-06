'''
Packing (*args) collects multiple input values into a tuple automatically when we don’t know how many arguments will be passed.

Example Idea:
*t → packs all extra arguments into a tuple t.
'''

def packfun (v, *t) :
  for i in range (len(t)) :
    if t[i] == v :
      print (t)
      return i 

print(packfun(100, 20,30, 40, 60, 70, 100, 110)) 
