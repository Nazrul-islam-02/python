

# class Phone:
#     def call(self):
#         print("You can Call")
    
#     def message(self):
#         print("You can message")


# class Samsung(Phone):

#     def photo(self):
#         print("You can take photo")


# s1 = Samsung()
# s1.photo()
# s1.message()










class Shape:
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2


class Triangle(Shape):

    def area(self):
        areaOfTriangle = 0.5* self.dim1 * self.dim2
        print(areaOfTriangle)


class Rectangle(Shape):
    
    def area(self):
        areaOfRectangle = self.dim1* self.dim2


rect = Triangle(90,10)
rect.area()