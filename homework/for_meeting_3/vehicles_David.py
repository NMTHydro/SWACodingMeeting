class Vehicle(object):

    def __init__(self, make, model, year, kind):

        self.make = make
        self.model = model
        self.year = year
        self.kind = kind


class Car(Vehicle):

    def __init__(self, doors):

        Vehicle.__init__(self, self.make, self.model, self.year, kind='Car')
        self.doors = doors


class Boat(Vehicle):

    def __init__(self, power):

        Vehicle.__init__(self, self.make, self.model, self.year, kind='Boat')
        self.power = power
        ## ## ##


class Airplane(Vehicle):

    def __init__(self):
        pass


# ============================ EOF =============================
