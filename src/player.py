# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f"The player is in {self.current_room}"

    def display_inventory(self):
        if len(self.inventory) > 0:
            print(f"\nYour inventory contains: ")
            for item in self.inventory:
                print(f"- {item.name}")
        else:
            print("\nYour inventory doesn't contain any items yet.\n")