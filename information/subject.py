from . import Database

class Subject:
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.csv_file = 'data/subject.csv'

    def subject_info(self):
        print("Name: {} \n Code: {} \n".format(self.name,self.code))

    def add_subject(self):   
        last_id = Database([], self.csv_file).id_ai()
        subject = [last_id +1,self.name,self.code]
        Database([subject],self.csv_file).savedata()
    
    def all_subject(self):
        Database([], self.csv_file).printdata()


