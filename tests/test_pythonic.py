from pythonic_garage_band/pythonic_garage_band import Musician

def test_Musician():
    actual = Musician.name("Bob")
    expected = "Bob"
    assert actual == expected


def test_band_members():
    assert Band.to_list


