import webbrowser
lock = input("Are you bored in lockdown? (Yes/No)\n")
if lock.lower()=="yes":
    lock2 = input("What would you like to do:\nPress 1 to listen songs\nPress 2 to watch comedy videos\nPress 3 to watch porn\n")
    if lock2=="1":
        song = input("Which song you want to listen.Please enter the song name:\n")
        print(f"Ok.Playing {song}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    elif lock2=="2":
        print("Opening BB ki Vines channel")
        webbrowser.open("https://www.youtube.com/channel/UCqwUrj10mAEsqezcItqvwEw")
    elif lock2=="3":
        print("Opening porn site")
        webbrowser.open("https://www.xvideos3.com/")
    else:
        print("Invalid Input")
elif lock.lower()=="no":
    print("Bhaad mein jaa")
else:
    print("Invalid input")

