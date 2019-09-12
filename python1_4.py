
class Robot:
    def __init__(self,name="Lorem"):
        self.name = name
        self.color= "Red"
        self.energy = 100
    
    def introduce_yourself(self):
        print("My name is " + self.name)
    def jump(self,speed):
        
        if self.energy <= 50 and self.energy != 0:
            print("low energy")
            self.energy -= 10
        elif self.energy >=50:
            self.energy -= 10
        elif self.energy == 0:
            print("Empty Energy")
        return self.energy
    @staticmethod
    def newfunc():
        return True


robot1 = Robot("TOM")
robot1.jump("0.5")

