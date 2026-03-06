''' A bank provides loans based on the following conditions:
If the applicant's age is ≥ 21
If income is ≥ 25,000
If credit score is ≥ 700 → Loan Approved
Else → Loan Rejected (Low Credit Score)
Else → Loan Rejected (Low Income)
Else → Loan Rejected (Age not eligible) '''

age = int(input('Enter age: '))
if age >= 21 :
     print ('Yes')
     income = int(input('Enter Income: '))
     if income >= 25000 :
          print ('Yes')
          cs = int(input('Enter CS:'))
          if cs >= 700 :
                print ('Yes, You are Eligible')
          else :
                print('No, Credit Score Not Met!')
     else :
            print ('No, Less Income!')
else :
     print ('No, Under Aged!')
