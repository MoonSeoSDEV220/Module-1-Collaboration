#Moon Seo
#Module 2 Lab
#This programm will calculate the student's gpa to determine the eligibility 
# of making it into the Dean's list.

count: int = 0
deansGPA: float = 3.5
honorRoll: float = 3.25

while count != 5:
    
    studentLname: str = input("Enter the last name. Enter ZZZ to quit: ")
    if studentLname == "ZZZ":
        break
    
    studentFname: str = input("Enter the First name. Enter ZZZ to quit: ")
    if studentFname == "ZZZ":
        break
    
    student_gpa: float = float(input("Enter the GPA: "))
    if student_gpa >= deansGPA:
        print("Congratulation", studentFname, studentLname, "!. You have made it into Dean's list!")
    
    elif student_gpa >= honorRoll:
        print("Congratulation", studentFname,studentLname, "!. You have made it into Honor Roll!")

    count += 1
    