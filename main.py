# This is the main file for poker

import deck
import dealer
import logic
import intro
import player_2

# Header & Intro for the game

deck.cards_drawing() # Graphics

input("\nWelcome to Five Card Draw! Are you ready to play? Press enter if you are ready to begin! ")

intro.tutorial() # Tutorial

decision = input("\nDo you want to play Five Card Draw? (Y/N): ").strip().upper() # Options
if decision != "Y":
    print("Thank you for considering, come back any time!")
    play_again = "N"
decision = input("Do you want to play against another person? If not, you will play against the computer. (Y/N): ").strip().upper() # 2 player version
if decision == "Y":
    player_2.main()
    play_again = "N"
    pass
else:
    play_again = "Y"
    player_points = 0
    computer_points = 0
while play_again == "Y": # Five Card Draw game loop
    dealer.build_new_hands()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") # An ineffective way to clear the entire screen lol
    print(f"\n----------------------------------------\n")
    print("\n        Welcome to Five Card Draw! \n")
    print("-------------- Scoreboard: --------------\n")
    print(f"              Player:     {player_points}")
    print(f"              Computer:   {computer_points}")
    print(f"\n----------------------------------------\n")

    decision = input("\nAre you ready to see your cards? (Y/N): ").strip().upper()
    if decision != "Y":
        print("Too bad, here are your cards anyway:")
    dealer.print_player_hand()
    input("\nNow that you have your cards, let's play! Press enter to continue: ")
    print()

    dealer.get_new_player_cards()
    dealer.print_player_hand()
    dealer.get_new_computer_cards() # Change computer's cards

    decision = input("Are you happy with your cards? (Y/N): ").strip().upper()
    if decision == "Y":
        input("Good, now let the battle begin! (to see if you win or lose). Press enter to continue: ")
    else:
        input("Too bad, get ready (to lose)! Press enter to continue: ")

    print("\n-------------- Showdown! --------------")
    dealer.print_player_hand()
    dealer.print_computer_hand()

    # --- Scoring ---
    player_score = logic.evaluate_hand(dealer.player_hand)
    computer_score = logic.evaluate_hand(dealer.computer_hand)

    # --- Debugging ---
    # print(f"Player score: {player_score}")
    # print(f"Computer score: {computer_score}")

    if player_score > computer_score: 
        print(f"\nCongratulations, you win with {logic.hand_names[player_score[0]]}! The computer had {logic.hand_names[computer_score[0]]}.")
        player_points += 1
    elif player_score == computer_score:
        print("\nSo close, it's a tie!")
    else:
        print(f"\nSadly, you lose with {logic.hand_names[player_score[0]]}! The computer had {logic.hand_names[computer_score[0]]}.")
        computer_points += 1
    play_again = input("\nThat was a short game! Do you want to play again? (Y/N): ").strip().upper()
    print(f"\n----------------------------------------\n")
    print("\n\n")
print("Thank you for playing! Come back again any time.")