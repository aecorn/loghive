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
        self.mother = self.queen_finder(mother)
        # In some cases we know who the father is, he only has the DNA of his mother
        self.fathers_mother = self.queen_finder(fathers_mother)
    
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
    def queen_finder(mother):
        """
        Can recieve the name of mother as string or the sha1-ID,
        will then have to search among existing queens to find ID.
        If no match is found, keep the string as passed. But should probably warn the user...
        Dont warn if no mother is registered?
        """
        if isinstance(mother, _hashlib.HASH):
            print("mother is identified by ID")
            for queen in Queen.instances:
                if mother == queen.id:
                    return queen.id
            raise ValueError("Cant find Queen by ID")
        elif isinstance(mother, str):
            print("mother is identified by name")
            for queen in Queen.instances:
                if mother.lower() == queen.name.lower():
                    return queen.id
            return mother
        elif mother is None:
            print("mother is missing")
            return None
        else:
            raise TypeError("Dont understand the Queen I am looking for.")

if __name__ == "__main__":
    temp_queen = Queen("Queen", datetime.datetime.now())
    temp_queen2 = Queen("Queen", datetime.datetime.now(), mother="Queen", fathers_mother=temp_queen.id)

    # Should be this years color
    print('Color', temp_queen.color_id, ":", temp_queen.color, )
    print('Id:', temp_queen.id.hexdigest())
    print("Queen2's mother is", temp_queen2.mother.hexdigest())