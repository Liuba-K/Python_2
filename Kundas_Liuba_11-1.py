class Date:

    def __init__(self, d):
        #self.date = d
        self.number, self.month, self.year = d.split("-")
        self.change_date(d.split("-"))

    @classmethod
    def change_date(cls, data):
        #number, month, year = data.split("-")
        return cls.validation_number(data)
        #print(int(number))
             #, int(month), int(year)

    @staticmethod
    def validation_number(obj):
        print("Hi", obj)
        """
        if obj.month < 12:
            print("hi")
        else:
            print("no", obj)
"""
#date_list = ["23", "12", "1988"]
d_1 = Date("20-10-1988")
#d_2 = Date.change_date("20-10-1988")
print(Date.change_date("20-10-1988"))
print(d_1.number)
#print(Date.validation_number(d_1))
#print(date_1.date)