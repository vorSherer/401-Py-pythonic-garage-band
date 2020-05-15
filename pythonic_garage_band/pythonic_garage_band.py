class Band():

    bands = []

    def __init__ (self, name, members):
        self.name = name
        self.members = members
        Band.bands.append(self)

    # def play_solos(self):
    #     pass

    # @classmethod
    # def to_list(cls):
    #     return cls.band_members # list of all members



class Musician():
    def __init__ (self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Musician, {self.name}"
         

class Guitarist(Musician):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def __repr__(self):
        return f"Guitarist, {self.name}"

    # def get_instrument(self):
    #     return "guitar"

    # def play_solo(self):
    #     return "power riff"


class Bassist(Musician):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    def __repr__(self):
        return f"Bassist, {self.name}"

    # def get_instrument(self):
    #     return "bass"

    # def play_solo(self):
    #     return "bottom riff"


class Drummer(Musician):
    def __init__ (self, name, kit):
        super().__init__(name)
        self.kit = kit

    # def __repr__(self):
    #     return f"Drummer, {self.name}"

    # def get_instrument(self):
    #     return "drums"

    # def play_solo(self):
    #     return "percuusion madness"


class Keyboardist(Musician):
    def __init__(self, name, model):
        super().__init__(name)
        self.model = model

    # def __repr__(self):
    #     return f"Keyboardist, {self.name}"

    # def get_instrument(self):
    #     return "Keys"

    # def play_solo(self):
    #     return "electro jam"


