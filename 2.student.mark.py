class input_students:

    def __init__(self, id_student, name_student, dob_student):
        self.id_students = id_student
        self.name = name_student
        self.dob = dob_student

    def __str__(self):
        return f"{self.id_students} {self.name} {self.dob}"

    def add_student(self):
        students2 = {'id': self.id_students, 'Name': self.name, 'Dob': self.dob}
        student_id_list.append(students2['id'])

        students1.append(students2)


student_id_list = []
course_id_list = []
mark_course = []
marks1 = []
marks2 = {}

course2 = {}
course1 = []
students1 = []
students2 = {}


def print_student_list():
    print("List of students:")
    for i in range(len(students1)):
        print(f"{i + 1} " + students1[i])


class input_number_student:
    def __init__(self, n2):
        self.n2 = n2


class input_courses:

    def __init__(self, id_course, name_course):
        self.id_course = id_course
        self.name = name_course

    def __str__(self):
        return f"{self.id_course} {self.name} "

    def add_course(self):
        course2 = {'id': self.id_course, 'Name': self.name}
        course_id_list.append(course2['id'])
        course1.append(course2)


def print_course_list():
    print("List of course:")
    for i in range(len(course1)):
        print(f"{i + 1} " + course1[i])


class input_number_course:
    def __init__(self, n3):
        self.n3 = n3


class Mark(input_students):
    def __init__(self, id_student, name_student, dob_student):
        super().__init__(id_student, name_student, dob_student)
        self.mark = mark

    def input_mark(self):
        marks2 = {'Id course': self.id_course, 'Id student': self.id_students, 'Mark': self.mark}
        marks1.append(marks2)


def input_marks(studentid, courseid, mark):
    for course in course_id_list:
        if courseid == course_id_list[course]:
            for student in student_id_list:
                if studentid == student_id_list[student]:
                    marks2 = {'Course Id': studentid, 'Student Id': courseid, 'Mark': mark}
                    mark_course.append(marks2['Course Id'])
                    marks1.append(marks2)

                    print("Mark added successfully!")
                    return
            print("Wrong student ID, Please try again.")
            return
        print("Wrong course ID, Please try again.")
        return


def list_cr_marks():
    cid = input("Enter course id: ")
    for i in marks1:
        if i[1] == cid:
            for index, item in enumerate(students1):
                print(index, item)
                print("Student's mark:", i[2])


while True:
    print(
        "Chose: \n 1. To input numbers of students.\n 2. To input numbers of course.\n 3. To input student "
        "information: id, name, DoB.\n 4. To input course information: id, name.\n 5. To select a course, input marks "
        "for student in this course.\n 6. To print list of student.\n 7. To list course.\n 8. Show student marks for "
        "a given course.")

    option = int(input())
    if option == 1:
        n1 = input_number_student(int(input("Input number of students in a class: ")))

    if option == 2:
        n4 = input_number_course(int(input("Input number of course: ")))

    if option == 3:
        n1 = int(input("Input number of students to input:"))
        for n in range(n1):
            Id = input('enter student id:')
            name = input('enter student name:')
            dob = input('enter student dob:')
            p1 = input_students(Id, name, dob)
            p1.add_student()
            print(p1)

    if option == 4:
        n5 = int(input("Input number of course to input:"))
        for n in range(n5):
            Id_course = input('enter course id:')
            name = input('enter course name:')
            p2 = input_courses(Id_course, name)
            p2.add_course()
            print(p2)

    if option == 5:
        n6 = int(input("Input number of mark to input:"))
        for n in range(n6):
            course_id = input("Enter course ID: ")
            student_id = input("Enter student ID: ")
            mark = input("Enter mark: ")


    if option == 6:
        print_student_list()

    if option == 7:
        print_course_list()
    if option == 8:
        list_cr_marks()
    else:
        print("Please enter a number from 1 to 8!")
