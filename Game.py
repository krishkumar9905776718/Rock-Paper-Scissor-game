import random
import time
import os

options = ["rock", "paper", "scissor"]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def countdown():
    for i in ["Rock", "Paper", "Scissor"]:
        print(i)
        time.sleep(1)
        

def play_round():
    user = input("\nEnter rock/paper/scissor: ").lower()
    while user not in options:
        user = input("Invalid! Enter rock/paper/scissor: ").lower()

    countdown()
    comp = random.choice(options)
    print("Computer chose:", comp)

    if user == comp:
        print("Draw!")
        return 0
    elif (user == "rock" and comp == "scissor") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissor" and comp == "paper"):
        print("You win this round")
        return 1
    else:
        print("Computer wins this round")
        return -1

def game():
    clear_screen()
    print("Rock - Paper - Scissor")

    rounds = int(input("How many rounds? (Best of): "))
    user_score = 0
    comp_score = 0

    for r in range(1, rounds + 1):
        print(f"\n----- Round {r} -----")
        result = play_round()

        if result == 1:
            user_score += 1
        elif result == -1:
            comp_score += 1

        print(f"Score - You: {user_score}  Computer: {comp_score}")
        time.sleep(1)
        clear_screen()

    print("\n===== Final Result =====")
    if user_score > comp_score:
        print("You won the match.")
    elif comp_score > user_score:
        print("Computer won the match.")
    else:
        print("Match Draw.")

game()