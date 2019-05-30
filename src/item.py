# Write a class to hold item information.
# The item should have name and description attributes.


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}"

    def on_take(self):
        print(f"{self.name.upper()} has been added to your inventory.")

    def on_drop(self):
        print(f"{self.name} was dropped from your inventory.")
