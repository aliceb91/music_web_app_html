class Artist():
    def __init__(self, id, name, genre):
        # Sets artist data.
        #
        # Parameters:
        #   id: int
        #   name: string
        #   genre: string
        self.id = id
        self.name = name
        self.genre = genre

    def __eq__(self, other):
        # Compares two Artist objects together.
        return self.__dict__ == other.__dict__

    def __repr__(self):
        # Returns a string when the object is called.
        return f"Artist({self.id}, {self.name}, {self.genre})"
