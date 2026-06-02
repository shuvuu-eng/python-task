students = []

n = int(input("Enter number of students: "))

for i in range(n):
    student = {}

    student["Name"] = input("Enter Name: ")
    student["Roll No"] = input("Enter Roll No: ")
    student["Branch"] = input("Enter Branch: ")
    student["Marks"] = int(input("Enter Marks: "))
    student["Grade"] = input("Enter Grade: ")

    students.append(student)

print("\nStudent Records")

for student in students:
    print(student)