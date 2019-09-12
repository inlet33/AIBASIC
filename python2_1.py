# class Car:
#     def __init__(self):
#         self.__secretkey = '123xxx22' 
#     def getter(self):
#         return self.__secretkey
#     def setter(self,seckey):
#         self.__secretkey = seckey

# Car().setter('asdasdww')
# car1 = Car()
# car1.setter('12344ssxxx')
# car2 = Car()
# print(car1.getter())
import os 





class View:
    @staticmethod
    def showinfo():
        print("Name      |     Age     |      Address      |     Type")
        for info in info_list:
            print("{}      | {}         | {}              | {} \n".format(info["name"],info["age"],info["address"],info["type"]))


while True:
    os.system('cls')
    print("Welcome to Enrollment System")
    print("[1]Student")
    print("[2]Teacher")
    print("[3]ShowInformations")
    print("[4]Exit")
    choice = input("Your Choice")
    if choice == '1':
        os.system('cls')
        name = input("Student Name:")
        age = input("Student Age:")
        address = input("Student Address:")
        yearlvl = input("Student Year Level:")
        student = Student(name,age,address,yearlvl)
        student.addstudent
        continue
    elif choice == '3':
        os.system('cls')
        View().showinfo()
    elif choice == '4':
        break
#