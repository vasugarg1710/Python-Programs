guesses = 0
number = 18
while True:
    if (guesses == 9): # Limiting the guesses
        print("Your game is over as your guesses are over")
        break
    num = int(input("Enter the number\n"))
    guesses = guesses+1
    if (num<number):
        print("Try a larger number")
    elif (num==number):
        print("Congrats you guessed the correct number. The correct number is",number)
        print("Number of guesses you took to finish are",guesses)
        break
    else:
        print("Try a smaller number")



