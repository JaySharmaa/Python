import random

game = True

def play_again():
    play = input("do u want to play again ?").lower()
    if play == "Yes" or "Y":
        game
    else:
        print("Thank you for playing!")

while game:

    my_ans = input("Choose rock , paper or scissors: ")
    my_ans = my_ans.lower()

    if my_ans == "quit":
        break

    comp_ans = random.choice(["rock" , "paper" , "scissors"])

    if my_ans != "rock" and my_ans != "paper" and my_ans != "scissors":
        print("Please enter a valid option")
        continue

    print(f"Your choice {my_ans}")
    print(f"Computer chose {comp_ans}")

    if my_ans == comp_ans:
        print("It is a Tie!")
        continue
    elif my_ans == "paper" and comp_ans == "rock":
        print("You Won!")
        break
    elif my_ans == "rock" and comp_ans == "scissors":
        print("You Won!")
        break
    elif my_ans == "scissors" and comp_ans == "paper":
        print("You Won!")
        break
    else:
        print("You Lose!")
        play_again()


