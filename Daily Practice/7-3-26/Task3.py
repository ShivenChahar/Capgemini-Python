# Write a Python function that finds the sum of digits of a number, but the function should only work for numbers with length min 2 and max 5?

def fun (a) :
  if a > 99999 or a < 10 :
    print("Wont work")
  else :
    sum = 0
    while a > 0 :
      t = a % 10
      sum += t
      a = a // 10
    return sum
i = int(input('Enter: '))
print(fun(i))