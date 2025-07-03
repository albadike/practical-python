import time


class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        # Notice how the class is passed as an argument
        tm = time.localtime()
        # And used to create a new instance
        return cls(tm.tm_year, tm.tm_mon, tm.tm_mday)
    
class NewDate(Date):
    pass

d = Date.today()
print(f"Today's date is: {d.year}-{d.month:02}-{d.day:02}")  

new_date = NewDate.today()
print(f"Today's date in NewDate is: {new_date.year}-{new_date.month:02}-{new_date.day:02}")