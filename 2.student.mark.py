class input_students:

    def __init__(self, id_student, name_student, dob_student):
        self.id_students = id_student
        self.name = name_student
        self.dob = dob_student

    def __str__(self):
        return f"{self.id_students} {self.name} {self.dob}"

    def add_student(self):
        students_2 = {'Student Id': self.id_students, 'Student Name': self.name, 'Student Dob': self.dob}
        student_id_list.append(students_2['Student Id'])

        students1.append(students_2)
        print(students1)
        print(student_id_list)


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
        print(f"{i + 1} ")
        print(students1[i])


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
        course_2 = {'Course id': self.id_course, 'Course Name': self.name}
        course_id_list.append(course_2['Course id'])
        course1.append(course_2)
        print(course1)
        print(course_id_list)


def print_course_list():
    print("List of course:")
    for i in range(len(course1)):
        print(f"{i + 1} ")
        print(course1[i])


class input_number_course:
    def __init__(self, n2):
        self.n3 = n2


def input_marks(course_id_1, student_id_1, marks):
    for course in course_id_list:

        if course_id_1 == course:
            for student in student_id_list:
                if student_id_1 == student:
                    marks_2 = {'Course Id': course_id_1, 'Student Id': student_id_1, 'Mark': marks}
                    mark_course.append(marks_2['Course Id'])
                    marks1.append(marks_2)
                    print(marks1)
                    print(mark_course)
                    print("Mark added successfully!")
                    return
        #         else:
        #             print("Wrong student ID, Please try again.")
        #             return
        # else:
        #     print("Wrong course ID, Please try again.")
        #     return


def list_cr_marks(course_id_2):
    for course in mark_course:
        if course_id_2 == course:
            print(f"Marks for course {course_id_2}:")
            print(marks1)

            return
    #     else:
    #         print("Wrong ID, Please try again.")
    #         return
    # else:
    #     print("Wrong ID, Please try again.")
    #     return


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
        n3 = int(input("Input number of students to input:"))
        for n in range(n3):
            Id = input('enter student id:')
            name = input('enter student name:')
            dob = input('enter student dob:')
            p1 = input_students(Id, name, dob)
            p1.add_student()
            print(p1)
    if option == 4:
        n4 = int(input("Input number of course to input:"))
        for n in range(n4):
            Id_course = input('enter course id:')
            name = input('enter course name:')
            p2 = input_courses(Id_course, name)
            p2.add_course()
            print(p2)
    if option == 5:
        n5 = int(input("Input number of mark to input:"))
        for n in range(n5):
            course_id = input("Enter course ID: ")
            student_id = input("Enter student ID: ")
            mark = input("Enter mark: ")
            input_marks(course_id, student_id, mark)

    if option == 6:
        print_student_list()
    if option == 7:
        print_course_list()
    if option == 8:
        course_id2 = input("Input Course you want to show students mark: ")
        list_cr_marks(course_id2)
    else:
        print("Please enter a number from 1 to 8!")
