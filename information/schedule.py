from . import Database

class Schedule:
    def __init__(self,s_name,c_name):
        self.s_name = s_name
        self.c_name = c_name
        self.csv_file = 'data/schedule.csv'

    def schedule_info(self):
        print("Subject: {} \n Course: {} \n".format(self.s_name,self.c_name))

    def add_schedule(self):
        last_id = Database([], self.csv_file).id_ai()
        schedule = [last_id +1,self.s_name,self.c_name]
        Database([schedule],self.csv_file).savedata()
    
    def all_schedule(self):
        Database([], self.csv_file).printdata()
