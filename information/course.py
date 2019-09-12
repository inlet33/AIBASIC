from . import Database

class Course:
    def __init__(self,name,code):
        self.name = name
        self.code = code
        self.csv_file = 'data/course.csv'

    def course_info(self):
        print("Name: {} \n Code: {} \n".format(self.name,self.code))

    def add_course(self):
        last_id = Database([], self.csv_file).id_ai()
        course = [last_id +1,self.name,self.code]
        Database([course], self.csv_file).savedata()
    
    def all_course(self):
        Database([], self.csv_file).printdata()

