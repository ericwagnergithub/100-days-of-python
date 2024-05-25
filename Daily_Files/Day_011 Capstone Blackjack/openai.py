import random

# Define the card deck and their values
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4

def deal_card(deck):
    return random.choice(deck)

def calculate_hand_value(hand):
    value = sum(hand)
    # Adjust for aces if the total value is greater than 21
    aces = hand.count(11)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_hand(hand, hidden=False):
    if hidden:
        print(f"Dealer's hand: [{hand[0]}, *]")
    else:
        print(f"Hand: {hand}, Value: {calculate_hand_value(hand)}")

def game():
    print("Welcome to Blackjack!\n")
    
    # Shuffle the deck
    random.shuffle(deck)
    
    # Initial dealing
    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]
    
    # Display hands
    display_hand(player_hand)
    display_hand(dealer_hand, hidden=True)
    
    # Player turn
    while True:
        if calculate_hand_value(player_hand) == 21:
            print("Blackjack! You win!")
            return
        elif calculate_hand_value(player_hand) > 21:
            print("Bust! You lose!")
            return
        
        choice = input("Do you want to [H]it or [S]tand? ").lower()
        if choice == 'h':
            player_hand.append(deal_card(deck))
            display_hand(player_hand)
        elif choice == 's':
            break
    
    # Dealer turn
    display_hand(dealer_hand)
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deal_card(deck))
        display_hand(dealer_hand)
    
    # Final hands
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    print("\nFinal Results:")
    print(f"Your hand: {player_hand}, Value: {player_value}")
    print(f"Dealer's hand: {dealer_hand}, Value: {dealer_value}")
    
    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("You lose!")
    else:
        print("It's a tie!")

game()