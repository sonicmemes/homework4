from statistics import mean
import itertools

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name}\
        Фамилия: {self.surname}\
        Средняя оценка за домашние задания: {mean([item for sublist in list(itertools.chain(self.grades.values())) for item in sublist])}\
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\
        Завершенные курсы: {', '.join(self.finished_courses)}"
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}

    def __str__(self):
        return f"Имя: {self.name}\
        Фамилия: {self.surname}\
        Средняя оценка за лекции: {mean([item for sublist in list(itertools.chain(self.grades.values())) for item in sublist])}"
        
class Reviewer(Mentor):
    def __str__(self):
        return f"Имя: {self.name}\
        Фамилия: {self.surname}"
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
def compare_opposite(lecturer, student):
    avg_rate_lc = mean([item for sublist in list(itertools.chain(lecturer.grades.values())) for item in sublist])
    avg_rate_stu = mean([item for sublist in list(itertools.chain(student.grades.values())) for item in sublist])

    if avg_rate_lc == avg_rate_stu:
        return('Оценки равны')
    if avg_rate_lc != avg_rate_stu:
        return('Оценки не равны')
    if avg_rate_lc > avg_rate_stu:
        return('У лектора оценка больше')
    if avg_rate_lc < avg_rate_stu:
        return('У лектора оценка меньше')
    if avg_rate_lc >= avg_rate_stu:
        return('У лектора оценка больше или равна')
    if avg_rate_lc <= avg_rate_stu:
        return('У лектора оценка меньше или равна')
    

def compare_students(student, student2):
    avg_rate_stu1 = mean([item for sublist in list(itertools.chain(student.grades.values())) for item in sublist])
    avg_rate_stu2 = mean([item for sublist in list(itertools.chain(student2.grades.values())) for item in sublist])

    if avg_rate_stu1 == avg_rate_stu2:
        return('Оценки равны')
    # if avg_rate_stu1 != avg_rate_stu2:
    #     return('Оценки не равны')
    if avg_rate_stu1 > avg_rate_stu2:
        return(f'У {student.name + " " + student.surname} оценка больше чем у {student2.name + " " + student2.surname}')
    if avg_rate_stu1 < avg_rate_stu2:
        return(f'У {student.name + " " + student.surname} оценка меньше чем у {student2.name + " " + student2.surname}')
    # if avg_rate_stu1 >= avg_rate_stu2:
    #     return(f'У {student.name + " " + student.surname} оценка больше или равна оценке {student2.name + " " + student2.surname}')
    # if avg_rate_stu1 <= avg_rate_stu2:
    #     return(f'У {student.name + " " + student.surname} оценка меньше или равна оценке {student2.name + " " + student2.surname}')

def compare_lc(lecturer, lecturer2):
    avg_rate_lc1 = mean([item for sublist in list(itertools.chain(lecturer.grades.values())) for item in sublist])
    avg_rate_lc2 = mean([item for sublist in list(itertools.chain(lecturer2.grades.values())) for item in sublist])

    if avg_rate_lc1 == avg_rate_lc2:
        return('Оценки равны')
    # if avg_rate_lc1 != avg_rate_lc2:
    #     return('Оценки не равны')
    if avg_rate_lc1 > avg_rate_lc2:
        return(f'У {lecturer.name + " " + lecturer.surname} оценка больше чем у {lecturer2.name + " " + lecturer2.surname}')
    if avg_rate_lc1 < avg_rate_lc2:
        return(f'У {lecturer.name + " " + lecturer.surname} оценка меньше чем у {lecturer2.name + " " + lecturer2.surname}')
    # if avg_rate_lc1 >= avg_rate_lc2:
    #     return(f'У {lecturer.name + " " + lecturer.surname} оценка больше или равна оценке {lecturer2.name + " " + lecturer2.surname}')
    # if avg_rate_lc1 <= avg_rate_lc2:
    #     return(f'У {lecturer.name + " " + lecturer.surname} оценка меньше или равна оценке {lecturer2.name + " " + lecturer2.surname}')

   
some_student = Student('Ruoy', 'Eman', 'Male')
some_student2 = Student('Pavel', 'Romanov', 'Male')
some_student2.courses_in_progress += ['Python']
some_student2.courses_in_progress += ['Git']
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer2 = Reviewer('Buddy', 'Some')
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer2 = Lecturer('Buddy', 'Some')
cool_lecturer.courses_attached += ['Python']
cool_lecturer2.courses_attached += ['Python']

cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']
cool_reviewer.rate_hw(some_student, 'Python', 10)
cool_reviewer.rate_hw(some_student, 'Python', 10)
cool_reviewer.rate_hw(some_student, 'Python', 7)
cool_reviewer.rate_hw(some_student, 'Git', 4)
cool_reviewer.rate_hw(some_student2, 'Git', 10)
cool_reviewer.rate_hw(some_student2, 'Python', 4)
some_student.rate_lc(cool_lecturer, 'Python', 10)
some_student.rate_lc(cool_lecturer, 'Python', 2)
some_student2.rate_lc(cool_lecturer2, 'Python', 10)

print(compare_students(some_student, some_student2))
print(compare_lc(cool_lecturer, cool_lecturer2))
print(mean([item for sublist in list(itertools.chain(cool_lecturer.grades.values())) for item in sublist]))
print(mean([item for sublist in list(itertools.chain(cool_lecturer2.grades.values())) for item in sublist]))


 
print(some_student)
print(some_student2)