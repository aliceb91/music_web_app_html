from lib.artist_repository import ArtistRepository
from unittest.mock import Mock

def test_returns_list_of_artist_names(db_connection):
    # Given calling the all method
    # It returns a list of artist names as a string.
    db_connection.seed('seeds/artists_table.sql')
    repository = ArtistRepository(db_connection)
    result = repository.all()
    name_list = []
    for artist in result:
        name_list.append(artist.name)
    assert name_list == ['Pixies', 'ABBA', 'Taylor Swift', 'Nina Simone']

def test_get_single_record(db_connection):
    db_connection.seed("seeds/artists_table.sql")
    repository = ArtistRepository(db_connection)
    mock_artist = Mock()
    mock_artist.id = 3
    mock_artist.name = "Taylor Swift"
    mock_artist.genre = "Pop"
    artist = repository.find(3)

    assert artist.id == mock_artist.id
    assert artist.name == mock_artist.name
    assert artist.genre == mock_artist.genre

def test_create_new_artist(db_connection):
    # Given an artist object
    # It creates a new artist entry in the database.
    db_connection.seed('seeds/artists_table.sql')
    repository = ArtistRepository(db_connection)
    test_artist = Mock()
    test_artist.name = "Test name"
    test_artist.genre = "Test genre"
    repository.create(test_artist)
    result = repository.all()
    name_list = []
    for artist in result:
        name_list.append(artist.name)
    assert name_list == ['Pixies', 'ABBA', 'Taylor Swift', 'Nina Simone', 'Test name']