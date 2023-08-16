from lib.album import Album

def test_creates_valid_album():
    album = Album(1, "Doolittle", 1989, 1)
    assert album.id == 1
    assert album.title == "Doolittle"
    assert album.release_year == 1989
    assert album.artist_id == 1

def test_outputs_album_data():
    album = Album(4, "Hello", 1991, 3)
    assert str(album) == "Album(4, Hello, 1991, 3)"

def test_class_comparison():
    album_1 = Album(2, "Goodbye", 1976, 5)
    album_2 = Album(2, "Goodbye", 1976, 5)
    assert album_1 == album_2
