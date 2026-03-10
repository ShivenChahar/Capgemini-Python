# Creating Class
class College() :

    # Creating Constructor
    def __init__(self,name,age,id):
        self.name = name
        self.age = age 
        self.id = id

    # creating object method / Instance Method
    def display(self) :
        print(self.name, self.age, self.id, sep ='\n')

    # creating class method
    def c_display(cls) :
        print(cls.name, cls.id, cls.age, sep = '\n')

    # Correct Class Method acc to (GPT)
    @classmethod
    def c_display(cls):
        print("This is a class method")

# Creating Objects
student1 = College('Shiven', 22, 1097)
student2 = College('Harsh', 21, 947)

# Calling object method
student1.display()

# Calling Class method
College.c_display(student1)   

# Calling the Class in refrence to Objects
print(student1.display())
print ('Student-1 details')
print ("Student Name: ", student1.name)
print ('Age :', student1.age)
print ('Id: ', student1.id)        
print()
print ('Student-2 details')
print ("Student Name: ", student2.name)
print ('Age :', student2.age)
print ('Id: ', student2.id)