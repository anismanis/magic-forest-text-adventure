import time
import random
item = []
villain = random.choice(["slenderman", "joker", "clown", "vampire", "zombie"])
spell = random.choice(["protection", "luck", "invincible", "powerful"])


def print_pause(text_to_print):
    print(text_to_print)
    time.sleep(2)


def intro():
    print_pause("\n\nYou find yourself standing in honey "
                "in the middle of the food forest.")
    print_pause("\nUnbothered, you turn around and see a shadow "
                "from the corner of your eye.")
    print_pause("\n?????")
    print_pause("\nA {} is staring at you.".format(villain))
    print_pause("\nYou choose to ignore the {}.".format(villain))
    print_pause("\nYou keep walking to enjoy the cotton candy sky.")
    print_pause("\nYou feel pretty hungry.")


def forest():
    print_pause("\nWould you like to:")
    forest_choice = input("1. Cast a spell\n"
                          "2. Explore forest for food\n")
    if forest_choice == "1":
        print_pause("\nYou start casting {} spell.".format(spell))
        print_pause("\n!!!!!")
        print_pause("\nYou have summoned {} wand.".format(spell))
        item.append("wand")
    elif forest_choice == "2":
        print_pause("\nYou start exploring the forest.")
        print_pause("\nYou hear rustling behind the trees.")
        print_pause("\nYou turn around.")
        print_pause("\n!!!!!")
        print_pause("\nIt's the {}, grinning at you!".format(villain))
        print_pause("\nDarn it!He robs you off your crystals.")
        print_pause("\nIf only you have casted a spell to protect yourself.")
        print_pause("\nTry again?")
        forest()
    else:
        print_pause("Choose 1 or 2.")
        forest()


def garden():
    if "wand" in item:
        print_pause("\nYou keep walking.")
        print_pause("\nYou see a bountiful garden and a pizza park.")
        print_pause("\nThere is an ogre guarding each one of the places.")
        garden_choice = input("\nWhere would you go?:\n"
                              "1. Bountiful garden\n"
                              "2. Pizza park\n")
        if garden_choice == "1":
            print_pause("\nYou start dancing fortnite.")
            print_pause("\nThe ogre laughs.")
            print_pause("\nYou are granted access to the bountiful garden.")
            print_pause("\nYou start gathering food.")
            garden()
        elif garden_choice == "2":
            print_pause("\nThe ogre asks to show a magic wand.")
            print_pause("\nYou unveil the wand.")
            print_pause("\n\nZaaaapppppp!!!")
            print_pause("\nSome biznatch grabs your {} wand "
                        "from your sackle!".format(spell))
            print_pause("\n\nIt's the {}! Should have seen that "
                        "coming.\n".format(villain))
            item.append(spell)
        else:
            print_pause("Choose 1 or 2")
            garden()


def fight():
    fight_choice = input("\nInfuriated, you:\n"
                         "1. Curse and chase him\n"
                         "2. Throw a big rock candy at him\n")
    if fight_choice == "1":
        print_pause("\nYou blaspheme and start chasing "
                    "the {}.".format(villain))
        print_pause("\n...but he is much faster than you!")
        print_pause("\nAs you are chasing the {}, he uses the wand "
                    "against you!".format(villain))
        print_pause("\n\nZiiingggggg!")
        print_pause("\n\n.....you lose consciousness.")
        print_pause("\nYou lose the game.")
        play_again()
    elif fight_choice == "2":
        print_pause("\nYou pick up a big rock candy from the ground.")
        print_pause("\nYou throw the rock candy at the {}.".format(villain))
        print_pause("\nIt struck the {} right on his head and "
                    "he fell unconsciouss.".format(villain))
        print_pause("\nYou drag him to the nearest forest nymph "
                    "station for justice.")
        print_pause("\nYou have reacquired the wand of {}.".format(spell))
        print_pause("\nYou win the game!")
        play_again()
    else:
        print_pause("Choose 1 or 2.")


def play_again():
    replay = input("\nWould you like to play again? (y/n)")
    if replay == "y":
        print_pause("Awesome! Wait a moment..")
        play_game()
    elif replay == "n":
        print_pause("It has been an adventure. Until next time!")
    else:
        play_again()


def play_game():
    intro()
    forest()
    garden()
    fight()
    play_again()


play_game()
