from .model import Model


class Hotel(Model):
    _id = None
    name = None

    @classmethod
    def create(cls, record):

        instance = cls()
        # fill this up with the create logic
        return instance
