import datetime
import hashlib
from time import strftime
from typing import Type

class Queen:
    def __init__(self, name, birthmonth, mother = None):
        self.name = name
        if isinstance(birthmonth, datetime.datetime):
            self.birthmonth = birthmonth
        else:
            raise TypeError("Birthmonth should be a datetime object")    
        
        # Set color based on year born
        self.color = self.color_from_year(self.birthmonth)
        # Register time, mostly to generate a unique ID
        self.register_time = datetime.datetime.now()
        # ID specified from birthmonth, name, first registered time, sha1 ?
        self.id = str(self.name) + str(self.birthmonth.strftime(r'%m%d%Y%H%M%S')) + str(self.register_time.strftime(r'%m%d%Y%H%M%S'))
        self.id = hashlib.sha1(self.id.encode('utf-8')).hexdigest()
        # Another registered queen might be the mother of the current queen...
        self.mother = mother
    
    @staticmethod
    def color_from_year(date: datetime.datetime):
        year_remainder = int(date.year) % 5
        if year_remainder == 0:
            color = "blue"
        elif year_remainder == 1:
            color = "white"
        elif year_remainder == 2:
            color = "yellow"
        elif year_remainder == 3:
            color = "red"
        else:
            color = "blue"
        return color


if __name__ == "__main__":
    temp_queen = Queen("Queen2", datetime.datetime.now())

    # Should be this years color
    print('Color:', temp_queen.color)
    print('Id:', temp_queen.id)