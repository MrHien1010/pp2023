
numbersstudents = int(input("Input number of students: "))
numbersofcourses = int(input("input numbers of courses: "))

def inputstinfor():

    student = dict(
        input('Enter key and value separated by space: ').split()
        for _ in range(2))

    # 👇️ {'id': '1', 'name': 'Alice'}
    print(student)
    # studentinfor = input("input student id, name, DOB: ")
    # numbersofcourses = int(input("input numbers of courses: "))
    # coursesinfor = input("input courses information: Id , Name")
    #
    # # # number of student
    # n = int(input("Enter number of studnets: "))
    #
    # # Below line read inputs from user using map() function
    #
    # a = list(map(str, input("\nEnter the students name : ").strip().split()))[:n]
    #




    # For list of student
    lst1 = []

    # For list of courses
    # lst2 = []
    #
    # lst1 = [int(item) for item in input("Enter the student marks: ").split()]
    #
    # lst2 = [item for item in input("Enter the list courses : ").split()]
    #
    # print(lst1)
    # print(lst2)
    #




# def listcourses():
# print("\nStudent List is - ", a)


while True:
    print("Chose: \n 1. To input student information: id, name, DoB\n 2. To input course information: id, name\n 3. To select a course, input marks for student in this course")
    option = int(input())
    if option == 1:
         inputstinfor()
    #
    #
    if option == 2:
         break
