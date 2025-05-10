import random
import os
import time



def main():
    last_mode = None
    game_mode = None
    first_time = True

    while True:
        if first_time:
            print(" ")
            print("The Game of Nimm")
            print(" ")
            print("To win, be the last player to remove a stone before they're all gone\n")
            game_option = input("Select either '2 player' or 'AI': ").strip().lower()

            if game_option == "2 player":
                last_mode = "2_player"
                clear()
                play_game_coop()

            elif game_option == "ai":
                game_mode = "ai"
                print("VS AI selected")
                msg = input("Which AI would you prefer to play against? (Beginner[B] / Intermediate[I]) ").strip().upper()
                if msg == "BEGINNER" or msg == "B":
                    last_mode = "beginner"
                    clear()
                    play_game(game_mode)
                elif msg == "INTERMEDIATE" or msg == "I":
                    last_mode = "intermediate"
                    clear()
                    play_game_intermediate(game_mode)
                else:
                    print("Maybe next time!")
                    break
            else:
                print("Invalid game mode selected. Exiting the script.")
                break

            first_time = False

        else:
            if last_mode == "2_player":
                play_game_coop()
            elif last_mode == "beginner":
                play_game(game_mode)
            elif last_mode == "intermediate":
                play_game_intermediate(game_mode)

        replay = input("Would you like to play again? (Y = same mode, M = main menu, N = quit): ").strip().upper()
        if replay == "Y":
            continue
        elif replay == "M":
            first_time = True
            continue
        elif replay == "N":
            print("Thank you for playing.")
            break
        else:
            print("Invalid input. Exiting.")
            break


def play_game_intermediate(game_mode):
    print("Good luck against the harder AI!")
    stones = 20
    current_player = 1

    while True:
        print(f"There are {stones} stones left")
        print(" ")

        if current_player == 1:
            while True:
                msg = input("Player 1, would you like to remove 1 or 2 stones? ")
                if msg in ["1", "2"]:
                    msg = int(msg)
                    print(" ")
                    if msg <= stones:
                        break
                print("Invalid input. Try again.")
            stones -= msg

        elif current_player == 2:
            for i in range(4):
                print("The Computer is calculating" + "." * i, end="\r")
                time.sleep(0.5)
            
            print()
            timer_delay()
            if stones >= 2:

                if stones == 2:
                    ai_num = 1

                elif stones == 4:
                    ai_num = 1
                elif (stones - 2) % 3 == 0:
                    ai_num = 2
                else:
                    ai_num = random.randint(1, 2)
            else:
                ai_num = 1
            print(f"The computer selected {ai_num}!")
            print(" ")
            stones -= ai_num

        if stones == 0:
            loser = current_player
            break

        current_player = 2 if current_player == 1 else 1

    winner = 2 if loser == 1 else 1

    if winner == 2 and game_mode == "ai":
        print("The AI wins! Better luck next time")
    else:
        print("You win! Good job.")

def play_game(game_mode):
    stones = 20
    current_player = 1

    while True:
        print(f"There are {stones} stones left")
        print(" ")

        if current_player == 1:
            while True:
                msg = input("Player 1, would you like to remove 1 or 2 stones? ")
                if msg in ["1", "2"]:
                    msg = int(msg)
                    print(" ")
                    if msg <= stones:
                        break
                print("Invalid input. Try again.")
            stones -= msg

        elif current_player == 2:
            for i in range(4):
                print("The Computer is guessing" + "." * i, end="\r")
                time.sleep(0.2)
            
            print()
            timer_delay()
            ai_num = 1 if stones == 1 else random.randint(1, 2)
            print(f"The computer selected {ai_num}!")
            print(" ")
            stones -= ai_num

        if stones == 0:
            loser = current_player
            break

        current_player = 2 if current_player == 1 else 1

    winner = 2 if loser == 1 else 1

    if winner == 2 and game_mode == "ai":
        print("The AI wins! Better luck next time")
    else:
        print("You win!")

def play_game_coop():
    stones = 20
    current_player = 1

    while True:
        print(f"There are {stones} stones left")
        print(" ")

        while True:
            msg = input(f"Player {current_player}, would you like to remove 1 or 2 stones? ")
            print(" ")
            if msg in ["1", "2"]:
                msg = int(msg)
                print(" ")
                if msg <= stones:
                    break
            print("Invalid input. Try again.")

        stones -= msg

        if stones == 0:
            break

        current_player = 2 if current_player == 1 else 1

    print(f"Player {2 if current_player == 1 else 1} wins!")


def timer_delay():
    time.sleep(0.2)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')



if __name__ == '__main__':
    main()
