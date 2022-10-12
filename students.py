from bleach import clean


class Student:
    def __init__(self,name,house):
        # if not name:
        #     raise ValueError("Missing name")
        # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        #     raise ValueError("Invalid house")

        self.name = name.title()
        self.house = house.title()
    
    def __str__(self):
        return (f"{self.name} from {self.house}")

    # def print_data(self):
    #     print(f"{self.name} from {self.house}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing Name.")
        self._name = name

    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self,house):
        if house not in ["Ananda","Nalanda","Mahinda"]:
            raise ValueError("Invalid house")
        self._house = house

    @classmethod
    def get_student(cls):
        name = input("Student Name : ")
        house = input("Student House : ")
        return cls(name,house)

def main():
    student = Student.get_student()
    print(student)

# def get_student_data():
#     name = input("Student Name : ")
#     house = input("Student House : ")
#     student = Student(name,house)
#     return student

main()