students = []

while True:
    print("STUDENT MANAGEMENT SYSTEM")
    print("1. Add student")
    print("2. View all students")
    print("3. Search student by name")
    print("4. Search student by roll number")
    print("5. Update student details")
    print("6. Delete student")
    print("7. Exit")

    choice = int(input('Enter your choice (1-7): '))

    if choice == 1:
        name = input('Enter student name: ')
        rollno = input('Enter roll number: ')
        marks = input('Enter student marks: ')
        students.append([name, rollno, marks])
        print('Student added successfully!\n')

    elif choice == 2:
        if len(students) == 0:
            print('No students found!\n')
        else:
            print('List of students:')
            print('Name\t\tRoll no\t\tMarks')
            for student in students:
                print(f'{student[0]}\t\t{student[1]}\t\t{student[2]}')
            print('')

    elif choice == 3:
        name = input('Enter student name: ')
        found = False
        for student in students:
            if student[0].lower() == name.lower():
                found = True
                print('Name:', student[0])
                print('Roll no:', student[1])
                print('Marks:', student[2])
                print('')
                break
        if not found:
            print(f'No student found with name {name}\n')

    elif choice == 4:
        roll_no = input('Enter the roll number: ')
        found = False
        for student in students:
            if student[1] == roll_no:
                found = True
                print('Name:', student[0])
                print('Roll no:', student[1])
                print('Marks:', student[2])
                print('')
                break
        if not found:
            print(f'No student found with roll number {roll_no}\n')

    elif choice == 5:
        rollno = input('Enter student roll number: ')
        found = False
        for student in students:
            if student[1] == rollno:
                found = True
                print('1. Update name')
                print('2. Update roll no')
                print('3. Update marks')
                subchoice = int(input('Enter your choice (1-3): '))
                if subchoice == 1:
                    name = input('Enter new name: ')
                    student[0] = name
                elif subchoice == 2:
                    rollno = input('Enter new roll no: ')
                    student[1] = rollno
                elif subchoice == 3:
                    marks = input('Enter new marks: ')
                    student[2] = marks
                else:
                    print('Invalid Choice!')
                break
        if not found:
            print(f'No student found with roll number {rollno}\n')

    elif choice == 6:
        rollno = input('Enter student roll number: ')
        found = False
        for student in students:
            if student[1] == rollno:
                found = True
                students.remove(student)
                print('Student deleted successfully!\n')
                break
        if not found:
            print(f'No student found with roll number {rollno}\n')

    elif choice == 7:
        print('Thank you for using the Student Management System!')
        break

    else:
        print('Invalid choice! Please choose between 1 and 7.\n')