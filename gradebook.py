from enum import Enum
import uuid

class activestatus(Enum):
    deceased = 0
    alive = 1

class person:
    def __init__(self, firstname, lastname, dob,alive):
        self.firstname = firstname
        self.lastname = lastname
        self.dob = dob
        self.alive = alive

    def update_first_name(self,student_record,student_id,vfname):
        student_list = list(student_record)
        student_list[student_id][0] = vfname
        return tuple(student_list)


    def update_last_name(self,student_record,student_id,vlname):
        student_list = list(student_record)
        student_list[student_id][1] = vlname
        return tuple(student_list)

    def update_dob(self,student_record,student_id,vdob):
        student_list = list(student_record)
        student_list[student_id][2] = vdob
        return tuple(student_list)

    def update_alive(self,student_record,student_id,valive):
        student_list = list(student_record)
        student_list[student_id][3] = valive
        return tuple(student_list)


class instructor(person):
    def __init__(self):
        self.instructor_id = 'Instructor_' + str(uuid.uuid4())
        #super().__init__(firstname,lastname,dob,alive)      
        

class student(person):
    def __init__(self):
        #super().__init__(frstname, lastname, dob, alive)
        self.student_id = 'Student_' + str(uuid.uuid4())

class zipcodestudent(student):
    pass

class prekstudent(student):
    pass

class classroom:
    def __init__(self, students, instructors):
        self.students = students
        self.instructors = instructors

    def add_instructor(self, instructid):
        self.instructors.update({instructid: (self.instructors.firstname, self.instructors.lastname, self.instructors.dob, self.instructors.alive)})

    def remove_instructor(self, instructorid):
        del self.instructors[instructorid]

    def add_student(self, studentid):
        self.students.update({studentid: (self.students.firstname, self.students.lastname, self.students.dob, self.students.alive)})

    def remove_student(self, studentid):
        del self.students[studentid]

    def print_instructors(self ):
        for record in self.instructors:
            print (record)

    def print_students(self):
        for record in self.students:
            print (record)


    
c_instructor = instructor()
c_student = student()
c_classroom = classroom(c_student,c_instructor)



