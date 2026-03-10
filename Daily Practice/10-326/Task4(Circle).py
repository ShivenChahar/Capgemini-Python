#  FIND AREA AND PARAMETER OF CIRCLE 

class Circle:
      def __init__(self,radius):
            self.radius=radius
      def area(self):
            print("The area of circle is:",3.14*self.radius*self.radius)
      def parameter(self):
            print("The parameter of given circle is:",2*3.14*self.radius)
rad=int(input("enter the radius:"))
c1=Circle(rad)
c1.area()
c1.parameter()