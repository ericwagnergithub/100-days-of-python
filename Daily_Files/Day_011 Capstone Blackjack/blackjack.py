import os
clear = lambda: os.system('cls')

import random

from blackjack_art import logo


def deal_card():
    """"Return a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(card_list):
    """Take a list of cards and return the score."""
    score = sum(card_list)
    if len(card_list) ==2 and score == 21:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return score


def compare(user_score, computer_score):
    if user_score == computer_score:
        print("It's a draw. 🙃")
    elif computer_score == 0:
        print("The computer wins with a blackjack.")
    elif user_score == 0:
        print("You win with a blackjack. 😊")
    elif user_score > 21:
        print("You Busted! You Lose.")
    elif computer_score > 21:
        print("The computer busted! You Win!")
    elif computer_score > user_score:
        print("You lose")
    elif user_score > computer_score:
        print("You win!")
    else:
        print("Not defined.")


def play_game():
    print(logo)

    game_over = False

    #Deal Original Cards
    user_cards = [deal_card(),deal_card()]
    computer_cards = [deal_card(), deal_card()]

    while not game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
        print(f"    Comptuer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand {user_cards}, final score: {user_score}")
    print(f"Computer's final hand {computer_cards}, final score: {computer_score}")
    compare(user_score,computer_score)

while input("Do you want to play a game of Blackjack? Type 'y' or 'n'") == "y":
    clear
    play_game()




