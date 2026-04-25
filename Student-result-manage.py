Student = { }

while True:
    print("\n ----Student Manager App----")
    print(" 1. Add Student")
    print(" 2. View Student")
    print(" 3. Check Result")
    print(" 4. Exit")

    Choice = input("enter your choice: ")

    #Add student
    if Choice == "1":
        name = input("enter student name: ")
        marks = input(" enter student marks: ")
        Student[name] = marks
        print(f"{name} Successfully Added!")

    #View Student
    if Choice == "2":
        if not Student:
            print("NO student found")
        else:
            for name, marks in Student.items():
                print(name, ":", marks)

    #Check Result
    if Choice == "3":
        name = input("enter student name: ")
        if name in Student:
            marks = Student[name]

            if marks >= 40:
                print("PASS")
            else:
                print("FAIL")

        else:
            print("student not found")

    #Exit
    elif Choice == "4":
        print("Exiting...")
        break
    else:
        print("In-Valid input")