# Write a class to hold item information.
# The item should have name and description attributes.


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}"

    def on_take(self):
        if self.name.lower() == "crown":
            print(
                """You pick up the rusty crown in disappointment only to reveal an ancient mechanism under it that opens a secret passage in the wall. You step inside and can't believe your eyes! Mountains of gold and precious gems stand before you!

            ===================================
            =            YOU WIN!             =
            ===================================
            """)
        else:
            print(f"\n{self.name.upper()} has been added to your inventory.\n")

    def on_drop(self):
        print(f"\n{self.name.upper()} was dropped from your inventory.\n")
