import random
lst = ["s", "p", "sci"]
total_chances = 0
computer_score = 0
player_score = 0
while total_chances<=10:
    user_choice = input("Enter s,p or sci\n")
    total_chances = total_chances + 1
    computer_choice = random.choice(lst)
    if user_choice=="s" and computer_choice=="p":
        print(f"Computer Won. You entered {user_choice} and computer entered {computer_choice}")
        computer_score = computer_score + 1
    elif user_choice=="s" and computer_choice=="sci":
        print(f"You won. You entered {user_choice} and computer entered {computer_choice}")
        player_score = player_score + 1
    elif user_choice=="p" and computer_choice=="s":
        print(f"You won. You entered {user_choice} and computer entered {computer_choice}")
        computer_score = computer_score + 1
    elif user_choice=="p" and computer_choice=="sci":
        print(f"Computer won. You entered {user_choice} and computer entered {computer_choice}")
        player_score = player_score + 1
    elif user_choice=="sci" and computer_choice=="s":
        print(f"Computer won. You entered {user_choice} and computer entered {computer_choice}")
        computer_score = computer_score + 1
    elif user_choice=="sci" and computer_choice=="p":
        print(f"You won. You entered {user_choice} and computer entered {computer_choice}")
        player_score = player_score + 1
    else:
        print(f"Nobody won. You entered {user_choice} and computer entered {computer_choice}. No score is added")

if player_score>computer_score:
    print(f"Congrats you won. Your score is {player_score} and computer score is {computer_score}")
elif player_score<computer_score:
    print(f"Computer won. Your score is {player_score} and computer score is {computer_score}")
else:
    print("Match is tied. The score is same")