class Student:

    def __init__(self , name , marks):

        self.name = name
        self.marks = marks

    def grade(self):

        if self.marks > 90:
            return "A"
        elif 75 <= self.marks <= 89:
            return "B"
        elif 74 <= self.marks <= 50:
            return "C"
        elif 50 < self.marks:
            return "D"
        else:
            return "Invalid number entered"

    def group(self):

        print(self.name , self.grade())


arko = Student("Arko" , 100)

abesh = Student("Abesh" , 93)

arko.group()
abesh.group()


