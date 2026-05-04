class Car:

    def __init__(self , brand , model , year):

        self.brand = brand
        self.model = model
        self.year = year

    def age(self , cyear):

        return int(cyear) - int(self.year)


class Rectangle:

    def __init__(self , width , height):

        self.width = width
        self.height = height

    def __str__(self):

        return "Rectangle({} X {})".format(self.width , self.height)

    def perimetre(self):

        h = int(self.height)
        w = int(self.width)

        return 2 * (h + w)

    def area(self):
        h = int(self.height)
        w = int(self.width)

        return h * w

rec1 = Rectangle(5 , 6)

print(rec1)

