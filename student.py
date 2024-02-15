class Student:
    def __init__(self, name:str, age:int, gender:str) -> None:
        self.name = name
        self.age = age
        self.gender = gender

    def display(self) -> None:
        print(f"Name = {self.name}")
        print(f"Age = {self.age}")
        print(f"Gender = {self.gender}")