from .room import Room
from .model import Model


class Booking(Model):
    _id = None
    room_id = None
    name = None
    paid = None

    @classmethod
    def create(cls, record):

        instance = cls()
        # fill this up with the create logic
        return instance

    def room(self, db):
        pass # fill this up with the room logic
        