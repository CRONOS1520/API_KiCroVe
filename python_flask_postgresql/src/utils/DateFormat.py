import datetime

class DateFormat():

    @classmethod
    def convert_date(self, date):
        if(date == None):
            date = datetime.datetime.today()

        return datetime.datetime.strftime(date, '%d/%m/%Y')

    @classmethod
    def convert_date_hour(self, date):
        if(date == None):
            date = datetime.datetime.today()

        return datetime.datetime.strftime(date, '%d/%m/%Y %H:%M:%S')