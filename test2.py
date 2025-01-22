class Student:
    college_name = "PESCE Mandya"

    def __init__(self,name,subject,marks):
        self.name = name
        self.subject = subject
        self.marks = marks

    def student_details(self):
        print("Name     : ", self.name)
        print("Subject  : ", self.subject)
        print("Marks    : ", self.marks)

print(Student.college_name)
s1 = Student("Avinash","Math",98)
s1.student_details()

s2 = Student("Rajeev","Phy",99)
s2.student_details()

s3 = Student("Ravindra","Chem",96)
s3.student_details()