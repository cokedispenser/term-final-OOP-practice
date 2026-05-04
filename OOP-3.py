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

    def perimeter(self):

        h = int(self.height)
        w = int(self.width)

        return 2 * (h + w)

    def area(self):
        h = int(self.height)
        w = int(self.width)

        return h * w
class Person:

    def __init__(self , name , age):

        self.name = name
        self.age = age

    def __str__(self):
        return "My name is {} and I am {} years old".format(self.name , self.age)

    def say_hi(self):

        print(f"{self.name} says hi!")


class Student(Person):

    school_name = "St. Gregory Higher Secondary School"

    def __init__(self , name , age , id_no , grade):

        super().__init__(name , age)
        self.id_no = id_no
        self.grade = grade

    def __str__(self):
        return "My name is {} and I read in class {}".format(self.name , self.grade)

    def print_roll(self):
        print(f"My roll is {self.id_no}")

    def print_grade(self):
        print(f"I read in class {self.grade}")




student1 = Student("Arko" , 21 , 2410147 , 11)

person1 = Person("Arko" , 21)

student1.print_roll()
student1.print_grade()
student1.say_hi()

print(person1)
print(student1)
