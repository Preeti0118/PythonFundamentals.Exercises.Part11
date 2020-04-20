from enum import Enum
import uuid


class activestatus(Enum):
    deceased = 0
    alive = 1


class person:
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = activestatus.alive

    def update_first_name(self, first_name):
        self.first_name = first_name

    def update_last_name(self, last_name):
        self.last_name = last_name

    def update_dob(self, dob):
        self.dob = dob

    def update_alive(self, alive):
        self.alive = alive


class instructor(person):
    def __init__(self, first_name, last_name, dob):
        person.__init__(self, first_name, last_name, dob)
        self.instructor_id = f"Instructor_{uuid.uuid4()}"


class student(person):
    def __init__(self, first_name, last_name, dob):
        person.__init__(self, first_name, last_name, dob)
        self.student_id = f"Student_{uuid.uuid4()}"


class zipcodestudent(student):
    def __init__(self, first_name, last_name, dob):
        student.__init__(first_name, last_name, dob)


class prekstudent(student):
    def __init__(self, first_name, last_name, dob):
        student.__init__(first_name, last_name, dob)


class gradebook:
    pass


class classroom:
    def __init__(self):
        self.students = {}
        self.instructors = {}

    def add_instructor(self, instructor):
        self.instructors[instructor.instructor_id] = instructor

    def remove_instructor(self, instructor):
        if instructor.instructor_id in self.instructors:
            del self.instructors[instructor.instructor_id]

    def add_student(self, student):
        self.students[student.student_id] = student

    def remove_student(self, student):
        if student.student_id in self.students:
            del self.students[student.student_id]

    def print_instructors(self):
        for key, value in self.instructors.items():
            print(f"{key}: {value}")

    def print_students(self):
        for key, value in self.students.items():
            print(f"{key}: {value}")



#