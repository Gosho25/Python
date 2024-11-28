class Polygon:
    def p_disp(self):
        print("object is a Polygon")

class Rectangle(Polygon):
    def r_disp(self):
        print("object is a Rectangle")


class Square(Rectangle):
    def s_disp(self):
        print("object is a Square")



polygon = Polygon()
rectangle = Rectangle()
square = Square()


polygon.p_disp()   
rectangle.p_disp() 
rectangle.r_disp() 
square.p_disp()    
square.r_disp()    
square.s_disp()    