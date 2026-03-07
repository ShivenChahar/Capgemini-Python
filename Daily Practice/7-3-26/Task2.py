# Write a Python function to find the sum of digits of a number?

def fun (a) :
  sum = 0
  while a > 0 :
    t = a % 10
    sum += t
    a = a // 10
  return sum
i = int(input('Enter: '))
print(fun(i))

