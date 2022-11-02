from posixpath import supports_unicode_filenames
from tokenize import cookie_re
from unicodedata import name


class Student:
    l_student = []
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        Student.l_student.append(self)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def _mid_grades(self):
        sum = 0
        s_grades = list(self.grades.values())[0]
        for grade in s_grades:
            sum += grade
        mid = sum / len(s_grades)
        return mid

    def __str__(self):
        res = (f' Имя: {self.name} \n Фамилия: {self.surname} \n '
        f'Средняя оценка за лекции: {self._mid_grades():0.2f} \n '
        f'Курсы в процессе обучения: {", ".join(self.courses_in_progress)} \n '
        f'Завершенные курсы: {",".join(self.finished_courses)}\n')
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Студент не найден')
            return
        return self._mid_grades() < other._mid_grades()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    
class Lecturer(Mentor):
    l_lecturer = []
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        Lecturer.l_lecturer.append(self)

    def _mid_grades(self):
        sum = 0
        l_grades = list(self.grades.values())[0]
        for grade in l_grades:
            sum += grade
        mid = sum / len(l_grades)
        return mid
    
    def __str__(self):
        res = f' Имя: {self.name} \n Фамилия: {self.surname} \n Средняя оценка за лекции: {self._mid_grades():0.2f}\n' 
        return res
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Лектор не найден')
            return
        return self._mid_grades() < other._mid_grades()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f' Имя: {self.name} \n Фамилия: {self.surname}\n' 
        return res
        

first_student = Student('Влада', 'Майорова', 'young_gender')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['GIT']
first_student.finished_courses += ['SQL']
second_student = Student('Максим', 'Толстиков', 'young_gender')
second_student.courses_in_progress += ['Python']
second_student.finished_courses += ['Введение в программирование']

first_reviewer = Reviewer('Артем', 'Мальцев')
first_reviewer.courses_attached += ['Python']
first_reviewer.courses_attached += ['GIT']
second_reviewer = Reviewer('Антон', 'Парохин')
second_reviewer.courses_attached += ['SQL']
second_reviewer.courses_attached += ['Python']

best_lecturer = Lecturer('Олег', 'Булыгин')
best_lecturer.courses_attached += ['Python']
best_lecturer.courses_attached += ['GIT']
cool_lecturer = Lecturer('Максим', 'Мальчук')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['SQL']

first_reviewer.rate_hw(first_student, 'Python', 10)
first_reviewer.rate_hw(first_student, 'GIT', 9)
second_reviewer.rate_hw(first_student, 'Python', 8)
second_reviewer.rate_hw(first_student, 'Python', 10)

first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 9)
first_reviewer.rate_hw(second_student, 'Python', 8)

first_student.rate_lec(cool_lecturer, 'Python', 9)
second_student.rate_lec(cool_lecturer, 'Python', 8)
first_student.rate_lec(best_lecturer, 'Python', 10)
first_student.rate_lec(best_lecturer, 'Python', 10)
first_student.rate_lec(best_lecturer, 'GIT', 10)


def mid_student_grades(courses):
    all_grades = []
    for student in Student.l_student:
        if courses in student.courses_in_progress or student.finished_courses:
            for grade in student.grades.get(courses):
              all_grades.append(grade)
    medium = sum(all_grades) / len(all_grades)
    return print(f'Средняя оценка студентов по курсу {courses}: {medium:0.2f}')


def mid_lecturer_grades(courses):
    all_grades = []
    for lecturer in Lecturer.l_lecturer:
        if courses in lecturer.courses_attached:
            for grade in lecturer.grades.get(courses):
              all_grades.append(grade)
    medium = sum(all_grades) / len(all_grades)
    return print(f'Средняя оценка лекторов по курсу {courses}: {medium:0.2f}')


print(first_student.grades)
print(second_student.grades)
print(cool_lecturer.grades)
print(best_lecturer.grades)
print(first_reviewer)
print(second_reviewer)
print(cool_lecturer)
print(best_lecturer)
print(first_student)
print(second_student)
print(first_student > second_student)
print(best_lecturer > cool_lecturer)

mid_student_grades('Python')
mid_lecturer_grades('Python')