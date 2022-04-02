class Yard:
    instances = []

    def __init__(self, name, latitude=None, longitude=None, address=None):
        self.name = name

        Yard.instances.append(self)

    def delete(self):
        if self in Yard.instances:
            Yard.instances.remove(self)
        del self