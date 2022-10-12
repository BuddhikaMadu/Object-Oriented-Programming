import random


class Hat:
    houses = ["Ananda","Nalanda","Mahinda","Dharmaraja"]

    def __init__(self,name,house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} is in {self.house}"

    @classmethod
    def get_student(cls):
        name = input("Name : ").title()
        house = random.choice(cls.houses)
        return cls(name,house)

def main():
    student = Hat.get_student()
    print(student)

main()