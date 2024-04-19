class Student:
    def __init__(self, name, address, phoneNumber):
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
    
    def welcomeStudent(self):
        print("Welcome to our course\n")
        print("Name :", self.name)
        print("address :", self.address)
        print("phoneNumber :", self.phoneNumber)


name = str(input("What is your name?\n"))
address = str(input("Where do you live?\n"))
phone = str(input("What is your phone number?\n"))

object1 = Student(name, address, phone)

object1.welcomeStudent()
