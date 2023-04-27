class Geometry:

    #method overloading
    def area(self,a,b=0):
        if b == 0:
            print("Circle",3.14*a*a)
        else:
            print("Rect",a*b)




