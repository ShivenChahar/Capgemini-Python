#  Creating Class
class College :
    
    # Creating Class Attribute
    clg_name = 'JECRC'
    loc = 'Jaipur'
    pincode = '302902'

s1 = College()
s1.clg_name = 'LPU'
s1.loc = 'Punjab'
s1.pincode = '202020'
s2 = College()
s2.clg_name = 'CU'
s2.loc = 'CHD'
s2.pincode = '111111'
print(College.clg_name)
print(s1.clg_name)
print(s2.loc)