# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.room_name = self.current_room.get_name()

    def get_currentroom(self):
        return self.current_room

    def update_currentroom(self, room):
        self.current_room = room
        return self.get_currentroom()
