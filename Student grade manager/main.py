classX = []
def add_student():
    while True:
        name = input("name of student: ").lower()
        marks = int(input("enter marks of student: "))
        student = {"name":name, "marks":marks}

        classX.append(student)
        print("student is added")

        ask = input("do you want to add details of another student?(yes/no): ").lower()
        if ask == "no":
            break
            
def view_grades():
    for student in classX:
        print(student["marks"])


def view_average():
    total = 0
    for student in classX:
        total = total + student["marks"]
    print(total/2)


print("welcome to the student grade tracker!")
add_student()

while True:
    print("1. view grades")
    print("2. view average") 
    print("3. Exit")

    choice = int(input("What do you wanna view first?: "))

    if choice == 1: 
        view_grades()

    if choice == 2:
        view_average()

    if choice == 3:
        break





        
    