import hashlib, _hashlib
import datetime

class Entry:
    instances = []

    def __init__(self):
        Entry.instances.append(self)

    def delete(self):
        Entry.instances.remove(self)
        del self