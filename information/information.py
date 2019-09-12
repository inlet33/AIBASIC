from .database import Database

class Information:
    def __init__(self,name,age,address):
        self.name = name
        self.age = age
        self.address = address
        self.csv_file = 'data/information.csv'
    def information(self):
        print("Name : {} \n Age: {} \n Address: {} \n".format(self.name,self.age,self.address))
    def saveinformation(self,wtype):
        last_id = Database([], self.csv_file).id_ai()
        student = [last_id +1,self.name,self.age,self.address,wtype]
        Database([student],self.csv_file).savedata()
        