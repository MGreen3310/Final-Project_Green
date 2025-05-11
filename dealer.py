# This is the file for dealing the cards

import deck
import logic
import collections

max_cards_in_hand = 5

full_deck = deck.build_deck()
player_hand = full_deck[:5] # Initializes the player's hand 
player2_hand = full_deck[5:10] # Initializes player 2's hand
computer_hand = full_deck[5:10] # Initializes the computer's hand
next_card_index = 10 # Initializes the point from which new cards are drawn

def build_new_hands():
    global full_deck, player_hand, player2_hand, computer_hand, next_card_index
    full_deck = deck.build_deck()
    player_hand = full_deck[:5] # Initializes the player's hand 
    player2_hand = full_deck[5:10] # Initializes player 2's hand
    computer_hand = full_deck[5:10] # Initializes the computer's hand
    next_card_index = 10 # Initializes the point from which new cards are drawn

def print_player_hand():
    print("\nYour hand:") # Printing your hand
    for i, card in enumerate(player_hand):
        number = card[:-1]
        suit = card[-1]
        print(f"Card {i+1}: {number}{deck.suits[suit]}")

def print_computer_hand():
    print("\nComputer hand:") # Printing computer's hand
    for i, card in enumerate(computer_hand):
        number = card[:-1]
        suit = card[-1]
        print(f"Card {i+1}: {number}{deck.suits[suit]}")

def get_new_player_cards(): # Replace cards you don't want
    global next_card_index
    for i in range(max_cards_in_hand):
        card = player_hand[i]
        card_decision = (
            input(f"Do you want to keep the {card[:-1]}{deck.suits[card[-1]]}? (Y/N): ").strip().upper())
        if card_decision != "Y":
            player_hand[i] = full_deck[next_card_index]
            next_card_index += 1

def get_new_computer_cards(): # Computer logic made to be a bit fiesty & go for the win. Old version was too easy to beat.
    global next_card_index
    kept_cards = [] # 

    hand_rank, _ = logic.evaluate_hand(computer_hand)
    nums = [card.split("/")[0] for card in computer_hand]
    num_count = collections.Counter(nums)

    if hand_rank >= 5:  # Straight or better
        return
    elif hand_rank == 4:  # Three of a Kind
        matches = [n for n, count in num_count.items() if count == 3]
        if matches:
            matching_num = matches[0]
            kept_cards = [card for card in computer_hand if card.split("/")[0] == matching_num]
    elif hand_rank == 3:  # Two Pair
        matching_nums = [n for n, count in num_count.items() if count == 2]
        kept_cards = [card for card in computer_hand if card.split("/")[0] in matching_nums]
    elif hand_rank == 2:  # One Pair
        matches = [n for n, count in num_count.items() if count == 2]
        if matches:
            matching_num = matches[0]
            kept_cards = [card for card in computer_hand if card.split("/")[0] == matching_num]
    else:  # High card, keep faces
        face_cards = ["J", "Q", "K", "A"]
        kept_cards = [card for card in computer_hand if card.split("/")[0] in face_cards]

    for i in range(len(computer_hand)): # Replace all other cards
        if computer_hand[i] not in kept_cards:
            computer_hand[i] = full_deck[next_card_index]
            next_card_index += 1

def print_player2_hand():
    print("\nYour hand:") # Printing your hand
    for i, card in enumerate(player2_hand):
        number = card[:-1]
        suit = card[-1]
        print(f"Card {i+1}: {number}{deck.suits[suit]}")

def get_new_player2_cards(): # Replace cards you don't want
    global next_card_index
    for i in range(max_cards_in_hand):
        card = player2_hand[i]
        card_decision = (
            input(f"Do you want to keep the {card[:-1]}{deck.suits[card[-1]]}? (Y/N): ").strip().upper())
        if card_decision != "Y":
            player2_hand[i] = full_deck[next_card_index]
            next_card_index += 1


if __name__ == "__main__":
    print_player_hand()
    print_computer_hand()
    print_player2_hand()
    get_new_player_cards()
    get_new_player2_cards()
    get_new_computer_cards()
    build_new_hands()