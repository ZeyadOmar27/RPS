import random
import time

def main():
    while True:
        winner()
        play_again = input("Again?? - Yes or No: ").lower()
        if play_again == "yes":
            continue
        else:
            print("Thanks for playing!")
            break
                
RPS = ["rock","paper","scissor"]

def gameplay():
    # prints rock, paper, scissor and gets user input
    while True:
        print("Rock...")
        time.sleep(0.4)
        print("Paper...")
        time.sleep(0.4)
        print("Scissor...")
        time.sleep(0.4)
        print("SHOOT!")
    
        user_play = input("").lower()
        if user_play not in RPS:
            print("Don't break the rules xD")
            continue
        else:
            return user_play

def machine():
    # computer's play 
    return random.choice(RPS)  
    
def winner():
    # score counters
    player_score = 0
    machine_score = 0
    
    # The whole gameloop
    while (player_score < 3) and (machine_score < 3):
        # updates user_play and machine_play with every round
        user_play = gameplay()
        machine_play = machine()

        if user_play == machine_play:
            print("It's a Tie")
        elif (user_play == "paper" and machine_play == "rock") or (user_play == "scissor" and machine_play == "paper") or (user_play == "rock" and machine_play == "scissor"):
            print("You Win!")
            player_score += 1
        else:
            print("Computer Wins!")   
            machine_score += 1

        print(f"Your play: {user_play} | Computer's play: {machine_play} ")
        print(f"{player_score} to {machine_score}")    

    if player_score == 3:
        print("Congratulations! You won the game!")
    else:
        print("Computer wins the game! Better luck next time.")
          
if __name__ == "__main__":
    main()

