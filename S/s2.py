

class Student:
    def __init__(self,name,grades:list):
        self.grades =grades
        self.name =name

    def average_grade(self):
        self.average=sum(self.grades)//len(self.grades)



class average_grade:
    def __init__(self,student:Student):
        self.average=sum(student.grades)//len(student.grades)


