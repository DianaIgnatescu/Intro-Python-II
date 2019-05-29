from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])


def move(direction, current_room):
    attribute = direction + "_to"

    # Check if the selected direction is possible
    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)

    # Print an error message if the movement isn't allowed.
    else:
        print("There is nothing for you there!")
        return current_room


# Write a loop that:

while True:
    # Prints the current room name
    print(player.current_room.name)

    # Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)

    # Waits for user input and decides what to do.
    print("You can move in a specific direction or you can type 'quit' to end your journey.")
    choice = input("\n>").lower()[0].split()

    if len(choice) == 1:
        # Set the user input as the direction command
        choice = choice[0]

        # If the user enters "quit", quit the game.
        if choice == "quit":
            print("Your journey has come to an end. See you next time!")
            break

        # If the user enters a cardinal direction, attempt to move to the room there.
        player.current_room = move(choice, player.current_room)

    elif len(choice) == 2:
        # If the user input contains two words, set the first as the direction command
        first_word = choice[0]
        second_word = choice[1]

    # Print an error message if the command is invalid.
    else:
        print("Please choose a valid command.")
        continue

