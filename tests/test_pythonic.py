from pythonic_garage_band.pythonic_garage_band import (
    Band, 
    Musician, 
    Guitarist,
    Bassist,
    Drummer,
    Keyboardist,
)


def test_Band_exists():
    assert Band
    # assert Band.to_list

    # A Band instance should have appropriate __str__ and __repr__ methods.
    # A Band should have a class method to_list which returns a list of previously created Band instances

def test_Band_build():
    # arrange - gather all data needed to do test: name, members
    expected_name = "Flloyd"
    bob = Guitarist("Bob", "Fender")
    ralph = Guitarist("Ralph", "Yamaha")
    expected_members = [bob, ralph]
    # act - performing the function that you want to test
    actual = Band("Flloyd", [bob, ralph])
    # assert - assert actual == expected
    assert actual.name == expected_name
    # A Band instance should have a name attribute which is a string.
    assert type(actual.name) is str
    # A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
    assert actual.members == expected_members
    assert Band.bands[0] == actual
    # A Band instance should have a play_solos method that asks each member musician to play a solo, in the order they were added to band.


def test_Musician_exists():
    assert Musician

    # Musician Subclass Tests

def test_Musician():
    # Each kind of Musician instance should have appropriate __str__ and __repr__ methods.
    expected = "Bob"
    bob = Musician("Bob")
    assert bob.name == expected
    assert str(bob) == "Bob"
    assert repr(bob) == "Musician, Bob"
    # Each kind of Musician instance should have a get_instrument method that returns string.
    # Each kind of Musician instance should have a play_solo method that returns string.


def test_Guitarist_exists():
    assert Guitarist


def test_Guitarist():
    expected_name = "Al"
    expected_model = "Fender"
    al = Guitarist("Al", "Fender")
    assert al.name == expected_name
    assert al.model == expected_model
    assert repr(al)


def test_Bassist_exists():
    assert Bassist


def test_Bassist():
    expected_name = "Doug"
    expected_model = "Squier"
    doug = Bassist("Doug", "Squier")
    assert doug.name == expected_name
    assert doug.model == expected_model
    assert repr(doug)


def test_Drummer_exists():
    assert Drummer


def test_Drummer():
    expected_name = "Boog"
    expected_model = "Gretch"
    boog = Drummer("Boog", "Gretch")
    assert boog.name == expected_name
    assert boog.model == expected_model
    assert repr(boog)


def test_Keyboardist_exists():
    assert Keyboardist


def test_Keyboardist():
    expected_name = "Dieter"
    expected_model = "Yamaha"
    dieter = Drummer("Dieter", "Gretch")
    assert dieter.name == expected_name
    assert dieter.model == expected_model
    assert repr(dieter)


