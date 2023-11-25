from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f"Имя: {self.name}\
        Фамилия: {self.surname}\
        Средняя оценка за домашние задания: {mean(self.grades.get(self.courses_in_progress))}\
        Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\
        Завершенные курсы: {', '.join(self.finished_courses)}"
    
    def __lt__(self, other):
        return self.grades.values() < other.grades.values()

    def __le__(self, other):
        return self.grades.values() <= other.grades.values()

    def __eq__(self, other):
        return self.grades.values() == other.grades.values()

    def __ne__(self, other):
        return self.grades.values() != other.grades.values()

    def __gt__(self, other):
        return self.grades.values() > other.grades.values()

    def __ge__(self, other):
        return self.grades.values() >= other.grades.values()

    
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
        Средняя оценка за лекции: {self.grades}"
        
    def __lt__(self, other):
        return self.grades.values() < other.grades.values()

    def __le__(self, other):
        return self.grades.values() <= other.grades.values()

    def __eq__(self, other):
        return self.grades.values() == other.grades.values()

    def __ne__(self, other):
        return self.grades.values() != other.grades.values()

    def __gt__(self, other):
        return self.grades.values() > other.grades.values()

    def __ge__(self, other):
        return self.grades.values() >= other.grades.values()
 
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



some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Git']
some_student.finished_courses += ['Введение в программирование']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']

cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(some_student, 'Python', 10)
cool_reviewer.rate_hw(some_student, 'Python', 10)
cool_reviewer.rate_hw(some_student, 'Python', 10)
 
print(some_student)