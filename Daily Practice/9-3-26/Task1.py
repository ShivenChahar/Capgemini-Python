# Creating Class
class College() :

    # Creating Constructor
    def __init__(self,name,age,id):
        self.name = name
        self.age = age 
        self.id = id

student1 = College('Shiven', 22, 1097)
student2 = College('Harsh', 21, 947)
print ('Student-1 details')
print ("Student Name: ", student1.name)
print ('Age :', student1.age)
print ('Id: ', student1.id)        
print()
print ('Student-2 details')
print ("Student Name: ", student2.name)
print ('Age :', student2.age)
print ('Id: ', student2.id)