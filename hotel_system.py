from models import Room, Hotel, Booking



# fill up all empty functions with the correct logic
class HotelSystem:
    def __init__(self, db):
        self.db = db

    def register_hotel(self, name):
        pass

    def add_room(self, hotel_id, **params):
        pass

    def get_room(self, room_id):
        pass

    def book_room(self, room_id, **params):
        pass
