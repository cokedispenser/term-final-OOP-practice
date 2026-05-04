class Citizen:

    __name = None
    __age = None

    def __init__(self , name , age):

        self.__name = name
        self.__age = age

    def __charter(self):

        if 0 <= self.__age <= 17:
            return "a child"

        elif 18 <= self.__age <= 65:
            return "an adult"

        elif self.__age > 65:
            return "a senior citizen"

        else:
            return "unclassified"

    def display(self):
        rank = self.__charter()
        print(f"{self.__name} is {rank}")

citizen1 = Citizen("Sam" ,3)

citizen1.display()
