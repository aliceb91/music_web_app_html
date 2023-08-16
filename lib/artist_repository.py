from lib.artist import Artist

class ArtistRepository():
    def __init__(self, connection):
        # Stores connection information.
        #
        # Parameters:
        #   connection: a connection object.
        self._connection = connection

    def all(self):
        # Pulls all artists from database and returns their names as a list.
        rows = self._connection.execute('SELECT * FROM artists')
        artists = []
        for row in rows:
            item = Artist(row["id"], row["name"], row['genre'])
            artists.append(item)
        return str(artists)[1:-1]

    def create(self, artist):
        # Adds a new artist entry to the database.
        self._connection.execute('INSERT INTO artists (name, genre) VALUES (%s, %s)', [artist.name, artist.genre])
