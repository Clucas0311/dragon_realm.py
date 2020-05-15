import random
import time  # Contains time related functions


def display_intro():
    print("""  You are in a land full of dragons. In front of you, you see two
caves. In one cave, the dragon is friendly and will share his treasure with
you. The other dragon is greedy and hungry, and will eat you on sight.""")


print()


def choose_cave():  # Ask the player which cave they want to go in
    cave = ''
    while cave != '1' and cave != '2':
        print("Which cave will you go into? (1 or 2)")
        cave = input()

    return cave


def check_cave(chosen_cave):
    print("You approach the cave...")
    time.sleep(2)  # pauses the program for 2 secs
    print("It's dark and spooky...")
    time.sleep(2)  # pauses for another 2 secs.
    print(
        "A large dragon jumps out in front of you! He opens his jaws roar... \
            and...")
    print()
    time.sleep(2)
    friendly_cave = random.randint(1, 2)  # indicates cave with friendly dragon
    if chosen_cave == str(
            friendly_cave):  # checks to see if player cave chosen
        # similar to friendly dragons cave randomly chosen if true:
        print("Gives you his treasure!")
    else:
        print("He gobbles you up in one bite! - YUM!!")


play_again = 'yes'  # Loop that intiates the start of the game
while play_again == "yes".lower() or play_again == 'y'.lower():
    display_intro()  # displays intro
    cave_number = choose_cave()  # allows the player to choose the cave they want
    check_cave(cave_number)  # stores the cave the player chose and compares it
    # to the cpu random number.
    print("Do you want to play again? (yes or no)")  # Ask the user
    play_again = input()  # If they would like to play again or not
