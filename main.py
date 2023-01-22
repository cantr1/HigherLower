from art import logo, vs
from replit import clear
from game_data import data
import random


def higher_lower():
    game_over = False
    num_correct = 0
    while not game_over:

        option_1 = data[random.randint(0, 49)]
        option_2 = data[random.randint(0, 49)]
        if option_2 == option_1:
            option_2 = data[random.randint(0, 49)]

        print(logo)

        print(f"\n1: {option_1['name']} is a {option_1['description']} from the {option_1['country']}.\n")

        print(vs)

        print(f"\n2: {option_2['name']} is a {option_2['description']} from the {option_2['country']}.\n")

        user_choice = input("\nWho do you think has more followers? '1' or '2' ")

        if user_choice == "1" and option_1['follower_count'] > option_2['follower_count']:
            num_correct += 1
            print("You are correct! ")
            print(f"You have gotten {num_correct} correct!")
            should_continue = input("Would you like to continue? 'Y' or 'N' ")
            if should_continue == "Y":
                clear()
            elif should_continue == "N":
                print("Thanks for playing!")

        if user_choice == "1" and option_1['follower_count'] < option_2['follower_count']:
            print("You are incorrect! ")
            print(f"You have gotten {num_correct} correct!")
            print("Thanks for playing!")
            game_over = True

        if user_choice == "2" and option_2['follower_count'] > option_1['follower_count']:
            num_correct += 1
            print("You are correct! ")
            print(f"You have gotten {num_correct} correct!")
            should_continue = input("Would you like to continue? 'Y' or 'N' ")
            if should_continue == "Y":
                clear()
            elif should_continue == "N":
                print("Thanks for playing!")

        if user_choice == "2" and option_1['follower_count'] > option_2['follower_count']:
            print("You are incorrect! ")
            print(f"You have gotten {num_correct} correct!")
            print("Thanks for playing!")
            game_over = True


higher_lower()