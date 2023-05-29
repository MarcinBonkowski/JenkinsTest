import unittest
from Student import Student

class TestStudents(unittest.TestCase):
    def test_isWoman(self):
        test_Student_1 = Student("Anna","Malciag",5)
        test_Student_2 = Student("Piotr","Kaczmarczyk",5)

        self.assertEqual(test_Student_1.isWoman(), True)
        self.assertEqual(test_Student_2.isWoman(), False)
    def test_isGradeGood(self):

        test_Student_1 = Student("Anna","Malciag",1)
        test_Student_2 = Student("Piotr","Kaczmarczyk",3)
        test_Student_3 = Student("Piotr","Kaczmarczyk",5)

        self.assertEqual(test_Student_1.isGradeGood(), False)
        self.assertEqual(test_Student_2.isGradeGood(), False)
        self.assertEqual(test_Student_3.isGradeGood(), True)
   
    def test_fullName(self):

        test_Student_1 = Student("Anna","Malciag",1)
        self.assertEqual(test_Student_1.fullName(), "Anna Malciag")

    def test_amendGrade(self):

        test_grade = 1
        test_Student_1 = Student("Anna","Malciag",test_grade)
        self.assertEqual(test_Student_1.grade, test_grade)
        test_newGrade = 5
        test_Student_1.amendGrade(test_newGrade)
        self.assertEqual(test_Student_1.grade, test_newGrade)

#add -v to the script

if __name__ == '__main__':
    unittest.main()