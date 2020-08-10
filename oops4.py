# electronic device
# pocket gadget
# phone

class ElectronicDevice():
    def __init__(self, name):
        self.name = name

    life_of_use = 10


class PocketGadget(ElectronicDevice):
    storage = 10
    size = 20


class Phone(PocketGadget):
    size = 5


Redmi = Phone("redmi")
print(Redmi.storage)
print(Redmi.size)
