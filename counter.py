import datetime

class Counter:
    def __init__(self):
        self.count = 0
        self.time_last_update = None

    def check_query(self):
        if(self.time_last_update == None):
            self.count += 1
            self.time_last_update = datetime.date.today()
        elif(self.time_last_update != datetime.date.today()):
            self.count = 1
            self.time_last_update = datetime.date.today()
        elif(self.time_last_update == datetime.date.today() and self.count<100):
            self.count+=1
        elif(self.time_last_update == datetime.date.today() and self.count>=100):
            return False
        return True
