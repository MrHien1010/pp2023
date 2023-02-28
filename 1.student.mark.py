def input_numbers_students():
    numbers_students = int(input("Input number of students in a class: "))
    if numbers_students < 0:
        print('invalid numbers, input again')
        input_numbers_students()
    return numbers_students


def input_numbers_courses():
    numbers_of_courses = int(input("input numbers of courses: "))
    if numbers_of_courses < 0:
        print("invalid numbers, input again")
        numbers_of_courses()
    return numbers_of_courses


marks = []
input_student_infor = {}
course = []
students = []


def input_student_in4():
    # student = []
    numbers_of_students_to_enter = int(input("Input number of students in the list: "))
    print(numbers_of_students_to_enter)
    for i in range(numbers_of_students_to_enter):
        Id, name, Dob = input(f"Enter #{i + 1} student's id, name,  Dob: ").split()
        students_d = {'id': Id, 'Name': name, 'Dob': Dob}
        students.append(students_d)

        print(students_d['id'])


def print_student_list():
    print("List of students:")
    for i in range(len(students)):
        print(f"{i + 1}")
        print(students[i])


def input_marks():
    print("enter E to exit function")
    while True:
        b = input("course id: ")
        a = input("student id:")
        c = input(" input marks:")
        marks.append((a, b, c))
        E = input("")



def list_cr_marks():
    cid = input("Enter course id: ")
    for i in marks:
        if i[1] == cid:
            for index, item in enumerate(students):
                print(index, item)
                print("Student's mark:", i[2])


def input_cousrse_in4():
    # student = []
    numbers_of_cousrse_to_enter = int(input("Input number of course in the list: "))
    print(numbers_of_cousrse_to_enter)
    for i in range(numbers_of_cousrse_to_enter):
        cousrse_d = {}
        Id, name = input(f"Enter #{i + 1} course's id, name: ").split()
        cousrse_d['id'] = Id
        cousrse_d['name'] = name
        course.append(cousrse_d)
        print(cousrse_d['id'])


def print_cousrse_list():
    print("List of courses:")
    for i in range(len(course)):
        print(course[i])


while True:
    print(
        "Chose: \n 1. To input numbers of students.\n 2. To input numbers of crourse.\n 3. To input student "
        "information: id, name, DoB.\n 4. To input course information: id, name.\n 5. To select a course, input marks "
        "for student in this course.\n 6. To print list of student.\n 7. To list course.\n 8. Show student marks for "
        "a given course.")
    option = int(input())
    if option == 1:
        input_numbers_students()
    if option == 2:
        input_numbers_courses()
    if option == 3:
        input_student_in4()
        print(students)
    if option == 4:
        input_cousrse_in4()
    if option == 5:
        input_marks()
    if option == 6:
        print_student_list()
    if option == 7:
        print_cousrse_list()
    if option == 8:
        list_cr_marks()
    else:
        print("Please enter a number from 1 to 8!")
