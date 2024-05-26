class Student():
    name = ""
    age = 12
    house = ""
    teacher = "Mr Table"
    def __init__(self):
        print("Making instance")
    def change_details(self):
        self.name = input('What is your name?')
        self.house = input('What is your house?')
    def show_details(self):
        print(f"The student's details are: \n {self.name} \n {self.age} \n {self.house} \n {self.teacher}")

Stavya = Student()
Stavya.change_details()
Stavya.show_details()