students = []
teachers = []
homeroom_teachers = []

def create_student():
    name_student = input("Enter the full name: ")
    class_student = input("Enter class name: ")

    student = {
        "Full name": name_student,
        "class": class_student
    }
    students.append(student)
    print(f"{name_student} has been added in the system")

def create_teacher():
    name_teacher = input("Enter the full name: ")
    subject_teacher = input("Enter subject name: ")
    classes_teacher = []

    while True:
        class_teacher = input("Enter class name: ")
        if class_teacher == "":
            break
        classes_teacher.append(class_teacher)

    teacher = {
        "Full name": name_teacher,
        "subject": subject_teacher,
        "class": classes_teacher
    }
    teachers.append(teacher)
    print(f"{name_teacher} has been added in the system")

def create_homeroom_teacher():
    name_homeroom = input("Enter the full name: ")
    class_lead = input("Enter the main class: ")
    homeroom_teacher = {
        "Full name": name_homeroom,
        "main class": class_lead
    }
    homeroom_teachers.append(homeroom_teacher)
    print(f"{name_homeroom} has been added in the system")

def manage_class():
    class_name = input("Enter class name: ").strip()
    print(f"{class_name} has the following students")

    found_students = False
    for student in students:
        if student["class"] == class_name:
            print(student["Full name"])
            found_students = True
    if not found_students:
        print("No students found")

    print ("Homeroom teacher:")
    found_homeroom_teacher = False
    for homeroom_teacher in homeroom_teachers:
        if homeroom_teacher["main class"] == class_name:
            print(homeroom_teacher["Full name"])
            found_homeroom_teacher = True
    if not found_homeroom_teacher:
        print("No homeroom teachers found")

def manage_student():
    student_name = input("Enter student name: ").strip()

    found_students = False
    student_class = None
    for student in students:
        if student["Full name"] == student_name:
            student_class = student["class"]
            print(f"{student_name} is in the following class {student_class}:")
            found_students = True
            break
    if not found_students:
        print("No classes found")
        return

    print("student's teachers")
    found_teachers = False
    for teacher in teachers:
        if student_class in teacher["class"]:
            print(teacher["Full name"])
            found_teachers = True
    if not found_teachers:
        print("No teachers found")

def manage_teacher ():
    teacher_name = input("Enter teacher name: ").strip()
    found_teachers = False
    for teacher in teachers:
        if teacher["Full name"] == teacher_name:
            print(f"{teacher_name} is in the following classes: ")
            for class_name in teacher["class"]:
                print(class_name)
            found_teachers = True
            break
    if not found_teachers:
        print("No class found")

def manage_homeroom_teacher ():
    homeroom_teacher_name = input("Enter homeroom teacher name: ").strip()
    found_homeroom_teacher = False
    found_homeroom_teacher_class = None

    for homeroom_teacher in homeroom_teachers:
        if homeroom_teacher["Full name"] == homeroom_teacher_name:
            found_homeroom_teacher_class = homeroom_teacher["main class"]
            found_homeroom_teacher = True
            break
    if not found_homeroom_teacher:
        print("Homeroom teacher not found")
        return

    print(f"{homeroom_teacher_name} leads class {found_homeroom_teacher_class}")
    print("Students in this class:")

    found_students = False

    for student in students:
        if student["class"] == found_homeroom_teacher_class:
            print(student["Full name"])
            found_students = True
    if not found_students:
        print("No students found")



while True:

    print("1. Create user")
    print("2. manage user")
    print("3. Show users")
    print("4. End")

    choice = input("Enter your choice: ")

    if choice == "1":
        user_type = input("Enter user type: student, teacher, homeroom teacher: ").strip()
        if user_type == "student":
            create_student()
        elif user_type == "teacher":
            create_teacher()
        elif user_type == "homeroom teacher":
            create_homeroom_teacher()

    elif choice == "2":
        manage_type = input("Enter search criteria: class, student, teacher, homeroom teacher, end: ").strip()

        if manage_type == "class":
            manage_class()
        elif manage_type == "student":
            manage_student()
        elif manage_type == "teacher":
            manage_teacher()
        elif manage_type == "homeroom teacher":
            manage_homeroom_teacher()
        else:
            print("Invalid input. Enter a valid choice")

    elif choice == "3":
        print("End")
        break

    else:
        print("Invalid input. Enter a valid choice")


