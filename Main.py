from Student import Student



print("Starting the program...")

firstStudent = Student("Kacper","Milejski",5)
secondStudent = Student("Anna","Milejska",3)
thirdStudent = Student("Piotr","Johnson",4)
fourthStudent = Student("Paul","McEntire",6)
fourthStudent = Student("Katarzyna","Walny",1)

print("Full name of the first student: {}".format(firstStudent.fullName()))
print("Full name of the second student: {}".format(secondStudent.fullName()))
print("Full name of the third student: {}".format(thirdStudent.fullName()))
print("Full name of the fourth student: {}".format(fourthStudent.fullName()))

print("Grade of the first student: {}".format(firstStudent.grade))
print("Grade of the second student: {}".format(secondStudent.grade))
print("Grade of the third student: {}".format(thirdStudent.grade))
print("Grade of the fourth student: {}".format(fourthStudent.grade))

listOfStudents = list()

listOfStudents.append(firstStudent)
listOfStudents.append(secondStudent)
listOfStudents.append(thirdStudent)
listOfStudents.append(fourthStudent)

#How many womens among students?

numberOfWomen = 0
for x in listOfStudents:
    if(x.isWoman()):
        numberOfWomen += 1

print("There are {} students among women".format(numberOfWomen))

#Write results into the file
for student in listOfStudents:
    with open('Results.txt','a') as file:
        file.write(student.fullName())
        file.write(" ")
        file.write(str(student.grade))
        file.write("\n")
        file.close()