a = 'aaabbaabcc'
s= ''
count = 1
for i in range (len(a)) :
     if i < len(a)-1 and a[i] == a[i+1] :
          count +=1
     else :
          s += a[i] + str(count)
          count = 1
print(s)
