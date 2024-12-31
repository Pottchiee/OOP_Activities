roster = [["Alice", 85],
          ["Bob", 92],
          ["Charlie", 78]]

def display_menu():
    print("\nClass Roster Management")
    print("========================")
    print("1. View Roster")
    print("2. Access a Student's Record")
    print("3. Update a Student's Grade")
    print("4. Add a New Student")
    print("5. Remove a Student")
    print("6. Exit")

def view_roster():
    print("\nCurrent Roster:")
    for i in range(len(roster)):
        student = roster[i]
        print(f"{i}. Name: {student[0]}, Grade: {student[1]}")

def access_student_record():
    index = int(input("Enter the student's index to access: "))
    if 0 <= index < len(roster):
        print(f"Student Record: Name: {roster[index][0]}, Grade: {roster[index][1]}")
    else:
        print("Invalid index.")

def update_student_grade():
    index = int(input("Enter the student's index to update: "))
    if 0 <= index < len(roster):
        new_grade = int(input("Enter the new grade: "))
        roster[index][1] = new_grade
        print("Updated Roster:", roster)
    else:
        print("Invalid index.")

def add_new_student():
    name = input("Enter the new student's name: ")
    grade = int(input("Enter the new student's grade: "))
    roster.append([name, grade])
    print("Updated Roster:", roster)

def remove_student():
    index = int(input("Enter the student's index to remove: "))
    if 0 <= index < len(roster):
        removed_student = roster.pop(index)
        print(f"{removed_student[0]} has been removed from the roster.")
        print("Updated Roster:", roster)
    else:
        print("Invalid index.")

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == '1':
        view_roster()
    elif choice == '2':
        access_student_record()
    elif choice == '3':
        update_student_grade()
    elif choice == '4':
        add_new_student()
    elif choice == '5':
        remove_student()
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")