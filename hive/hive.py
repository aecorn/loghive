from multiprocessing.sharedctypes import Value
from yard.yard import Yard

class Hive:
    instances = []

    def __init__(self, id, strength, yard: Yard):
        # If ID not specified, autogenerate?
        self.id = id
        self.strength = strength
        self.layers = 1

        # Hive should be in a Yard
        if isinstance(yard, Yard): 
            self.yard = yard
        else:
            self.yard = None

        Hive.instances.append(self)
    
    def layer_increase(self):
        self.layers += 1

    def layer_decrease(self):
        if self.layers > 1:
            self.layers -= 1
        else:
            raise ValueError("Cant decrease under 1 level.")
    
    def delete(self):
        if self in Hive.instances:
            Hive.instances.remove(self)
        del self