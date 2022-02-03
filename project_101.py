from ast import If
import random

game = True

while game:

    my_ans = input("Choose rock , paper or scissors: ")
    my_ans = my_ans.lower()

    # play_again = input("Do u want to play again ? Y Or N :").lower()

    if my_ans == "quit":
        break

    comp_ans = random.choice(["rock" , "paper" , "scissors"])

    if my_ans != "rock" and my_ans != "paper" and my_ans != "scissors":
        print("Please enter a valid option")
        continue

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

    # play_again = None

    # while play_again not in ["y" ,"yes","no","n"]:
    #     play_again = input("Do u want to play again ?").lower()
    # if play_again in ["y","yes"]:
    #     continue
    # else:
    #     print("You have finished game")
    #     game = False

    

# play_again = True

# while play_again:
#     choice = input("Do u want to play again ? Y or N").lower()
#     if choice == "y" or choice == "n":
#         play_again = False
#     else:
#         print("Wrong input!")
#         play_again = True


