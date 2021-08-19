
# game over
def game_over(reason):
    print("\n" + reason)
    print("Game Over!")
    # ask player if they want to play again or not by activating play_again()
    play_again()
    
# play again
def play_again():
    print("\nDo you want to play again? Press y or n")

    #convert the player's input to lower_case
    answer = input(">").lower()

    if "y" in answer:
        # if player typed "yes" or "y" start game from the beginning
        start()
    else:
        # if user types anything besides "yes" or "y", exit() the program
        exit()

def start():
    # give some prompts
    print("\nYou are standing in a dark room.")
    print("There is a door to your left and right, which one do you choose?")
    print("\nPress 1 or 2 to choose")
    print("1). Go to the left.")
    print("2). Go to the right.")

    # take input()
    answer = input(">")

    if answer == "1":
        #the player is dead!
        print("\nYou found a monster room")
        monster_room()
    elif answer == "2":
        #lead player to bear room()
        print("\nYou found a bear room")
        bear_room()
    else:
        # else call invalid_choice() function with "reason" argument
        game_over("\nYou didn't listen")
    
# bear room
def bear_room():
    # give some prompts
    # '\n' is to print the line in a new line
    print("\nThere is a bear here.")
    print("Behind the bear is another door.")
    print("The bear is eating tasty honey!")
    print("\nPress 1 or 2 to choose")
    print("1). Take the honey.")
    print("2). Taunt the bear.")

    # take input()
    answer = input(">")

    if answer == "1":
        #the player is dead!
        game_over("\n=====You have died=====")
    elif answer == "2":
        #lead player to diamond_room()
        print("\nThe bear finds your faces disgusting and closes its eyes to hide from the hideousness. You go through the other door safely.")
        diamond_room()
    else:
        # else call invalid_choice() function with "reason" argument
        game_over("\nYou didn't listen")

# monster room
def monster_room():
    # give some prompts
    # '\n' is to print the line on a new line
    print("\nNow you've entered the room of a monster!")
    print("The monster is sleeping.")
    print("\nPress 1 or 2 to choose")
    print("1). Go through the door silently.")
    print("2). Try to kill it.")

    #take input()
    answer = input(">")

    if answer == "1":
        #lead player to diamond_room()
        print("\nAnd people said those ninja lessons would never pay off. You go to the next room.")
        diamond_room()
    elif answer == "2":
        #the player is dead!
        game_over("\n=====You have died=====")
    
# diamond room
def diamond_room():
    # give some prompts
    # '\n' is to print the line in a new line
    print("\nYou walk into a room full of dazzling light. Diamonds litter the walls and ceiling in a dance of illumination")
    print("You are tempted to take a diamond but you hear hissing sounds. Do you dare to take one?")
    print("\nPress 1 or 2 to choose")
    print("1) Everyone can use more diamonds!")
    print("2) Let's make a run for it. Can't spend diamonds if I'm snake food.")

    # take input()
    answer = input(">")

    if answer == "1":
        # the player is dead!
        game_over("\n=====You have died=====")
    elif answer == "2":
        # the player wins the game
        print("\nYou have seen Indiana Jones and aren't fond of snakes. You run as fast as your legs can carry you.")
        print("\nYou win!!!")
        # activate play_again() function
        play_again()
    else:
        # else call game_over() function with "reason" argument
        game_over("\nYou didn't listen.")    

# start the game
start()
