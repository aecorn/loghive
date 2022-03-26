import hashlib, _hashlib

class Keeper:
    instances = []

    def __init__(self, name):
        self.name = name

        Keeper.instances.append(self)