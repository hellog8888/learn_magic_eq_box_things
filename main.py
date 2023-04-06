class Box:
    def __init__(self):
        self.lst_box = []

    def add_thing(self, obj):
        self.lst_box.append(obj)

    def get_things(self):
        return self.lst_box

    def __eq__(self, other):
        return all(i in other.get_things() for i in self.get_things())

class Thing:
    def __init__(self, name, mass):
        self.name = name
        self.mass = mass

    def __eq__(self, other):
        if isinstance(other, Thing):
            return self.name == other.name.lower() and self.mass == other.mass