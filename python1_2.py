
# x = [1,2,3,4,5]
# y = [6,7,8,9,10]
# z = 2 not in y
# print(z)
# name = "jan"
# age = 25;
# print("my name is {} ang i am {} year young".format(age,name))

"""
This is a comment
"""

# name = "Jan-Joven Jumao-as"
# print(name.split("-"))
# splitedname =name.split("-")
# print(' '.join(splitedname))

name = "          janjoven               "
print(name.strip())
"""
age = int(input("How young are you?"))

if age > 20 and age < 60:
    print("You are in legal age!")
elif age > 60 and age < 120:
    print("You are already great person")
else:
    print("You are under age")

"""
students = [{"name":"hiro"},{"name":"chika"},{"name":"asuka"}]

for student in students:
    print(student["name"])

while True:
    question = input("Do you want to quit? Y/N : ")
    if question == 'Y':
        break
    else:
        continue

