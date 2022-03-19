from multiprocessing.sharedctypes import Value


class Hive:
    def __init__(self, id, strength):
        # If ID not specified, autogenerate?
        self.id = id
        self.strength = strength
        self.layers = 1
    
    def layer_increase(self):
        self.layers += 1

    def layer_decrease(self):
        if self.layers > 1:
            self.layers -= 1
        else:
            raise ValueError("Cant decrease under 1 level.")
    