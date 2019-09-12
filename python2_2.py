from information.information import Information
from information.student import Student
from information.teacher import Teacher
from information.database import Database
from information.subject import Subject
from information.schedule import Schedule
from information.course import Course
import os 
import csv


# class View:
#     @staticmethod
#     def showinfo():
#         print("Name      |     Age     |      Address      |     Type")
#         for info in info_list:
#             print("{}      | {}         | {}              | {} \n".format(info["name"],info["age"],info["address"],info["type"]))

while True:
    print("Welcome to Enrollment System")
    print("[1]Student")
    print("[2]Teacher")
    print("[3]Subject")
    print("[4]Course")
    print("[5]Schedule")
    print("[6]Show Info")
    print("[0]Exit")
    choice = input("Your Choice")
    if choice == '1':
        os.system('cls')
        name = input("Student Name:")
        age = input("Student Age:")
        address = input("Student Address:")
        yearlvl = input("Student Year Level:")
        student = Student(name,age,address,yearlvl)
        student.addstudent()
        continue

    elif choice =='2':
        os.system('cls')
        name = input("Teacher Name:")
        age = input("Teacher Age:")
        address = input("Teacher Address:")
        teacher = Teacher(name,age,address)
        teacher.saveinformation('teacher')
        continue

    elif choice == '3':
        os.system('cls')
        name = input("Subject Name:")
        code = input("Subject Code:")
        subject = Subject(name,code)
        subject.add_subject()
        continue
        #subject.add_subject([Name','Code'])

    elif choice == '4':
        os.system('cls')
        name = input("Course Name:")
        code = input("Course Code:")
        course = Course(name,code)
        course.add_course()
        continue

    elif choice == '5':
        os.system('cls')
        name = input("Schedule Name:")
        code = input("Schedule Code:")
        schedule = Schedule(name,code)
        schedule.add_schedule()
        continue

    elif choice == '6':
        os.system('cls')
        print("Select Type")
        print("[1]Student")
        print("[2]Teacher")
        print("[3]Subject")
        print("[4]Course")
        print("[5]Schedule")
        choice_info = input("Your Choice")
        os.system('cls')
        
        if choice_info == '1':
            print(Database([],'data/information.csv').printdata())
        elif choice_info == '2':
            print(Database([],'data/information.csv').printdata())
        elif choice_info == '3':
            print(Database([],'data/subject.csv').printdata())
        elif choice_info == '4':
            print(Database([],'data/course.csv').printdata())
        elif choice_info == '5':
            print(Database([],'data/schedule.csv').printdata())
     
    
    elif choice == '0':
        break
