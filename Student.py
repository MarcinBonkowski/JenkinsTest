
class Student:
    def __init__(self,name,surname,grade) -> None:
        self.name = name
        self.surname = surname
        self.grade = grade

    def isGradeGood(self) -> bool:
        if(self.grade > 3):
            return True
        return False
    def fullName(self):
        return self.name + " " + self.surname
    def isWoman(self):
        if(self.name[-1] == 'a'):
            return True
        return False
    def amendGrade(self,newGrade) -> None:
        self.grade = newGrade

        