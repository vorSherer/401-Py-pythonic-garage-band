class Band():

    band_members = []

    def __init__ (self, name="unknown", members):
        self.name = name
        Band.band_members.append(self)
        # self.members = members

    def play_solos(self):
        pass

    @classmethod
    def to_list(cls):
        return cls.band_members # list of all members



class Musician():
    def __init__ (self, name):
        # super().__init__(name)
        self.name = name


class Guitarist(Musician):
    def __init__(self, name):
        self.name = name

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "shred"


class Bassist(Musician):
    def __init__(self, name):
        pass


class Drummer(Musician):
    def __init__ (self, name):
        pass


