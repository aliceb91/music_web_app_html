from lib.artist_repository import ArtistRepository
from unittest.mock import Mock

def test_returns_list_of_artist_names(db_connection):
    # Given calling the all method
    # It returns a list of artist names as a string.
    db_connection.seed('seeds/artists_table.sql')
    repository = ArtistRepository(db_connection)
    result = repository.all()
    assert result == 'Pixies, ABBA, Taylor Swift, Nina Simone'

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
    assert result == 'Pixies, ABBA, Taylor Swift, Nina Simone, Test name'
