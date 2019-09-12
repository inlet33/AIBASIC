
# y = 1**2+3*1+2

# def f(x,z=0):
#      y = x**2+3*x+z
#      print(y)
     
# def add(x,y):
#     total = x + y
#     return total
# def even_odd():
#     n = int(input("Enter A number:"))
#     if n%2 == 0 :
#         print("n is even number")
#     else:
#         print("n is an odd number")
# #add(2,4)

# even_odd()

# number = [1,2,4,5,6,7,8]

# print(min(number))
# x= 12

# def f():
#     global x
#     x =15
#     y = 3

#     return x+y
# def g():
#     global x
#     x =20
#     return x


# print(g())
# print(f())
# print(x)

class MyCar:

    def __init__(self,brand,color,code):
        self.brand = brand
        self.color = color
        self.code = code
        self.speed = 0

        print("Car Brand {} , color {} ,code {}".format(self.brand,self.color,self.code))
    
    def speedup(self):
        self.speed +=10
        return self.speed
    def speeddown(self):
        self.speed -=10
        return self.speed

Toyota = MyCar('Toyota','Red','x009')
Isuzu =  MyCar('Isuzu','Black','x010')

while True:
    speed = input("enter s to speedup")
    if speed == "st":
        print("Your Car",Toyota.brand," speed is ",Toyota.speedup())
        continue
    elif speed == "si":
        print("Your Car",Isuzu.brand," speed is ",Isuzu.speedup())
        continue
    else:
        break
