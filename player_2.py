# This is the file for 2 player mode

import dealer
import logic

def main(): # I needed a main function 
    player1 = input("Please input a name for player 1: ")
    player2 = input("Please input a name for player 2: ")

    player_points = 0
    player2_points = 0 

    play_again = "Y"
    while play_again == "Y": # Five Card Draw game loop
        dealer.build_new_hands()
        print("\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n        Welcome to Five Card Draw! \n")
        print("-------------- Scoreboard: --------------\n")
        print(f"              {player1}:     {player_points}")
        print(f"              {player2}:     {player2_points}")
        print(f"\n----------------------------------------\n")

        decision = input(f"\n{player1} are you ready to see your cards? (Y/N): ").strip().upper()
        if decision != "Y":
            print("Too bad, here are your cards anyway:")
        dealer.print_player_hand()
        print("\n")
        input(f"Okay {player1}, now you have a chance to discard some of your cards. Press enter to continue: ")
        dealer.get_new_player_cards()
        dealer.print_player_hand()

        input(f"\nOkay, slide the screen to {player2}. {player2}, it's your turn now. Press enter to continue: ")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        decision = input(f"\n{player2} are you ready to see your cards? (Y/N): ").strip().upper()
        if decision != "Y":
            print("Unlucky, here are your cards anyway:")
        dealer.print_player2_hand()
        print()
        dealer.get_new_player2_cards()
        dealer.print_player2_hand()

        input(f"\nOkay {player1} & {player2}, it's time to figure out who wins. Press enter to continue: ")
        print()

        print("\n-------------- Showdown! --------------")
        dealer.print_player_hand()
        dealer.print_player2_hand()

        # Scoring
        player_score = logic.evaluate_hand(dealer.player_hand)
        player2_score = logic.evaluate_hand(dealer.player2_hand)

        if player_score > player2_score: 
            input(f"\nCongratulations, {player1} wins! {player2} had a {logic.hand_names[player2_score[0]]}.")
            player_points += 1
        elif player_score == player2_score:
            input("\n Oh, it's a tie!")
        else:
            input(f"\nCongratulations, {player2} wins! {player1} had a {logic.hand_names[player_score[0]]}.")
            player2_points += 1

        play_again = input("\nThat was a short game! Do you want to play again? (Y/N): ").strip().upper()