from .model import Model
from .hotel import Hotel


class Room(Model):
    _id = None
    hotel_id = None
    price = None
    capacity = None

    @classmethod
    def create(cls, record):

        instance = cls()
        # fill this up with the create logic
        return instance

    def hotel(self, db):
        pass # Fill this up with the hotel logic