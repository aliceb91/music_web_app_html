from lib.artist import Artist

def test_creates_new_artist():
    # Given artist data
    # It creates an artist object.
    artist = Artist(1, "Hello", "Goodbye")
    assert artist.id == 1
    assert artist.name == "Hello"
    assert artist.genre == "Goodbye"

def test_compares_two_artists():
    # Given two Artist objects
    # It compares their instance variables.
    artist_1 = Artist(1, "Hello", "Goodbye")
    artist_2 = Artist(1, "Hello", "Goodbye")
    assert artist_1 == artist_2

def test_returns_string_when_called():
    # Given an Artist object
    # It returns a given string when called.
    artist = Artist(1, "Hello", "Goodbye")
    assert str(artist) == "Hello"
