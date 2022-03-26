import datetime
import hashlib, _hashlib

class Queen:
    instances = []

    def __init__(self, name, birthmonth, mother = None, fathers_mother = None):
        # Set name if unique
        for queen in Queen.instances:
            if name == queen.name:
                print(Queen.instances)
                raise ValueError(f"Queen must have unique name, {name} matches {queen.name}")
        self.name = name
        # Check if birth is actual date
        if isinstance(birthmonth, datetime.datetime):
            self.birthmonth = birthmonth
        else:
            raise TypeError("Birthmonth should be a datetime object")    
        # Set color based on year born
        self.color_id, self.color = self.color_from_year(self.birthmonth)
        # Register time, mostly to generate a unique ID
        self.register_time = datetime.datetime.now()
        # ID specified from birthmonth, name, first registered time, as sha1
        self.id = str(self.name) + str(self.birthmonth.strftime(r'%m%d%Y%H%M%S')) + str(self.register_time.strftime(r'%m%d%Y%H%M%S'))
        self.id = hashlib.sha1(self.id.encode('utf-8'))
        # Another registered queen might be the mother of the current queen...
        if mother: self.mother = self.queen_finder(mother)
        # In some cases we know who the father is, he only has the DNA of his mother
        if fathers_mother: self.fathers_mother = self.queen_finder(fathers_mother)
    
        # End of init, if queen was created successfully add to list of Queens
        Queen.instances.append(self)

    @staticmethod
    def color_from_year(date: datetime.datetime) -> tuple:
        """Return the color the queen should be marked with, based on year of birth"""
        color_key = {
            0 : "blue",
            1 : "white",
            2 : "yellow",
            3 : "red",
            4 : "green"
        }
        year_remainder = int(date.year) % 5
        return (year_remainder, color_key[year_remainder])

    @staticmethod
    def queen_finder(needle_name_id = None):
        """
        Can recieve the name or the sha1-ID of a queen, returns the id, if the queen is registered.
        will then have to search among existing queens to find ID.
        If no match is found, keep the string as passed. But should probably warn the user...
        Dont warn if no mother is registered?
        """
        if isinstance(needle_name_id, _hashlib.HASH):
            #print("search is identified by ID")
            for queen in Queen.instances:
                if needle_name_id == queen.id:
                    return queen.id
            raise KeyError("Cant find Queen by ID")
        elif isinstance(needle_name_id, str):
            #print("search is identified by name")
            for queen in Queen.instances:
                if needle_name_id.lower() == queen.name.lower():
                    return queen.id
            raise KeyError("Cant find Queen by name")
        elif needle_name_id is None:
            raise KeyError("No identifier, name/id provided to find queen")
        else:
            raise TypeError("Dont understand the Queen I am looking for.")

    def delete(self):
        if self in Queen.instances:
            Queen.instances.remove(self)
        del self

    @classmethod
    def delete_queen(cls, name:str = None, id:_hashlib.HASH = None):
        if name:
            id = cls.queen_finder(name)
        if id:
            for queen in cls.instances:
                if queen.id == id:
                    cls.instances.remove(queen)
                    del queen


if __name__ == "__main__":
    temp_queen = Queen("Queen", datetime.datetime.now())
    temp_queen2 = Queen("Queen2", datetime.datetime.now(), mother="Queen", fathers_mother=temp_queen.id)

    # Should be this years color
    print('Color', temp_queen.color_id, ":", temp_queen.color, )
    print('Id:', temp_queen.id.hexdigest())
    print("Queen2's mother is", temp_queen2.mother.hexdigest())

    # Cleanup queen2 by instance method
    temp_queen2.delete()
    print(Queen.instances)
    # Cleanup queen with classmethod
    Queen.delete_queen("Queen")