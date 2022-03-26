import hashlib, _hashlib
import datetime

class Calendar:
    instances = []

    def __init__(self):
        Calendar.instances.append(self)

    def delete(self):
        Calendar.instances.remove(self)
        del self