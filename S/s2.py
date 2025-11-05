

class Student:
    def __init__(self,name,grades:list):
        self.grades =grades
        self.name =name

    def average_grade(self):
        self.average=sum(self.grades)//len(self.grades)



class Average_grade:
    def __init__(self,student:Student):
        self.average=sum(student.grades)//len(student.grades)


# s=Student("fkfyuf0",[98,10,75,65])
# s.average_grade()
# print(s.average)
# a=Average_grade(s)
# print(a.average)
