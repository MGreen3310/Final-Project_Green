# This is the file for explaining how Five Card Draw works.

def tutorial(): # This looked messy so I made it a function. If I can't see it isn't not messy :D
    decision = input("\nBefore we begin, let's set some things straight. For this game you will need to make decisions, which you will indicate using Y for yes, N for no. These will be shown using (Y/N).\nLet's try that here -> Do you understand? (Y/N): ").strip().upper()
    while decision != "Y":
        decision = input("Your decison should only be the letter Y or N. You don't need to capitalize it or add any spaces. Do you understand? (Y/N): ").strip().upper()
    if decision == "Y":
        decision = input("\nGreat! Additionally, if you are prompted to continue, simply press enter. Try that here -> Press enter to continue: ").strip().upper()
    decision = input("\nAwesome! Before we begin, do you know the rules of Five Card Draw? (Y/N): ").strip().upper()
    if decision == "Y":
        decision = input("Are you sure? There is no harm in reviewing the rules before you play. Are you confident you know the rules? (Y/N): ").strip().upper()
    if decision != "Y":
        input("\nFive Card Draw is a short and simple poker variation that can be finished within 2 rounds. Press enter to continue: ")
        input("\n   1) Each player intially will be dealt 5 cards. Then, each player can choose to discard some cards. Press enter to continue: ")
        input("\n   2) For each card you will be given the chance to discard it. Press enter to continue: ")
        input("\n   3) After this phase, both players will reveal their cards. Whoever has a better hand of cards wins. Press enter to continue: ")
        input("\n   4) I recommend keeping a reference guide for poker hands up while you play. Press enter to continue: ")