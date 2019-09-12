import csv
class Database:
    def __init__(self,data=[], file_name=""):
        self.data = data
        self.header = []
        self.scv_file = file_name
        self.last_id = 0
    def savedata(self):
        self.readdata()
        with open(self.scv_file,'w',newline='') as wf:
            writer = csv.writer(wf)
            writer.writerow(self.header)
            writer.writerows(self.data)

    def readdata(self):
        with open(self.scv_file,'r') as rf:
            reader = csv.reader(rf)
            self.header = next(reader)
            for row in reader:
                self.data.append(row)
        return self.data

    def printdata(self):
        with open(self.scv_file,'r') as rf:
            reader = csv.reader(rf)
            for row in reader:
                print(row)

    def id_ai(self):
        with open(self.scv_file,'r') as rf:
            reader = csv.reader(rf)
            self.header = next(reader)
            if reader:  #print(type(reader)) -> <class '_csv.reader'>
                self.last_id = len(list(reader))
        return self.last_id

