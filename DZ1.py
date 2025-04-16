class Student:
    '''
    Создаём класс "Студент", который возвращает имя и фамилию студента, средний балл за ДЗ, а так курсы в процессе изучения и завершенные.
    '''
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средний балл за домашние задания: {sum([sum(values_list) for values_list in self.grades.values()])/sum([len(self.grades[i]) for i in self.grades])}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершённые курсы: {", ".join(self.finished_courses)}\n')
    
    def average_grade(self):
        if not self.grades:
            return 0
        total_grades = sum([sum(g) for g in self.grades.values()])
        count_grades = sum([len(g) for g in self.grades.values()])
        return total_grades / count_grades
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()
    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

        
class Mentor:
    '''
    Создаём класс "Преподаватель"
    '''
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] =  [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    '''
    Создаём унаследованный класс "Лектор" от родительского класса "Преподаватель", который возвращает имя и фамилию лектора, а так же средний балл за лекции.
    '''
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def grading(self, student, course, grade):
        if isinstance(student, Student) and 1 <= grade <= 10 and course in self.courses_attached:
            self.grades.setdefault(course, []).append(grade)
        else:
            return 'Ошибка'
        
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средний балл за лекции: {sum([sum(values_list) for values_list in self.grades.values()])/sum([len(self.grades[x]) for x in self.grades])}')
    
    def average_grade(self):
        if not self.grades:
            return 0
        total_grades = sum([sum(g) for g in self.grades.values()])
        count_grades = sum([len(g) for g in self.grades.values()])
        return total_grades / count_grades
    
    def __eq__(self, other):
        return self.average_grade() == other.average_grade()
    
    def __lt__(self, other):
        return self.average_grade() < other.average_grade()
    
    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

class Reviewer(Mentor):
    '''
    Создаём унаследованный класс "Эксперт" от родительского класса "Преподаватель", который вовращает имя и фамилию эксперта, проверяющего ДЗ.
    '''
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        super().rate_hw(student, course, grade)

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

# Функции для подсчета среднего балла.

def average_student_grade(students, course): 
    '''
    Функция для подсчета средней оценки студента.
    '''
    total = 0
    count = 0
    for student in students:
        if course in student.grades:
            total += sum(student.grades[course])
            count += len(student.grades[course])
    return total / count if count else 0

def average_lecturer_grade(lecturers, course):
    '''
    Функция для подсчета средней оценки лектора.
    '''
    total = 0
    count = 0
    for lecturer in lecturers:
        if course in lecturer.grades:
            total += sum(lecturer.grades[course])
            count += len(lecturer.grades[course])
    return total / count if count else 0

# Объекты классов, создадим студентов, лекторов и экспертов на основе соотв. классов.

student1 = Student('Ivan', 'Ivanchenko', 'male')
student1.courses_in_progress += ['Python']
student1.finished_courses += ['Git']

student2 = Student('Alena', 'Petrova', 'female')
student2.courses_in_progress += ['Python', 'Git']

lecturer1 = Lecturer('Sergey', 'Sergeev')
lecturer1.courses_attached += ['Python']

lecturer2 = Lecturer('Marina', 'Dorofeeva')
lecturer2.courses_attached += ['Git']

reviewer1 = Reviewer('Anna', 'Smirnova')
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Svetlana', 'Shapovalova')
reviewer2.courses_attached += ['Git']

# Балл за домашние задания.

reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student2, 'Python', 6)
reviewer2.rate_hw(student2, 'Git', 4)

# Балл за лекции.

lecturer1.grading(student1, 'Python', 5)
lecturer1.grading(student2, 'Python', 9)
lecturer2.grading(student2, 'Git', 7)

print(student1)
print(student2)
print(lecturer1)
print(lecturer2)
print(reviewer1)
print(reviewer2)

# Средний балл.

print("\nСредний балл за домашние задания по курсу 'Python':", average_student_grade([student1, student2], 'Python'))
print("\nСредний балл за лекции по курсу 'Python':", average_lecturer_grade([lecturer1, lecturer2], 'Python'))
