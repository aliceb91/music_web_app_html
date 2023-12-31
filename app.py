import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.artist import Artist
from lib.artist_repository import ArtistRepository
from lib.album import Album
from lib.album_repository import AlbumRepository

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/albums', methods=['GET'])
def get_albums():
    # Given a GET request
    # It returns all current albums in the databse.
    #connection = get_flask_database_connection(app)
    #repository = AlbumRepository(connection)
    #all_albums = repository.all()
    #return all_albums
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template('albums.html', albums=albums)

@app.route('/albums/<id>')
def get_single_albums(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template("show.html", album=album)

@app.route('/artists/<id>', methods=['GET'])
# Pulls a single artist from the repository and diaplays it's page.
def get_single_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template("show_artist.html", artist=artist)

@app.route('/artists', methods=['GET'])
# Pulls all artists and displays them on a page.
def get_all_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artists = repository.all()
    return render_template("artists.html", artists=artists)

# == Example Code Below ==

# GET /emoji
# Returns a smiley face in HTML
# Try it:
#   ; open http://localhost:5000/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    # We use `render_template` to send the user the file `emoji.html`
    # But first, it gets processed to look for placeholders like {{ emoji }}
    # These placeholders are replaced with the values we pass in as arguments
    return render_template('emoji.html', emoji=':)')

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
