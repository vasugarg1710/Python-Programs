import webbrowser
lock = input("Are you bored in lockdown? (Yes/No)\n")
if lock.lower()=="yes":
    lock2 = input("What would you like to do:\nPress 1 to listen songs\nPress 2 to watch comedy videos\nPress 3 to watch pº®n\nPress 4 to play games\nPress 5 to Binge watch\nPress 6 to learn language\nPress 7 to see Artworks\nPress 8 to chat online\nPress 9 to play chess\nPress 10 for others\n")
    if lock2=="1":
        song = input("Which song you want to listen.Please enter the song name:\n")
        print(f"Ok.Playing {song}")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
    elif lock2=="2":
         lock4=input("Which channel would u prefer:\n Press 1 for BB ki vines \n Press 2 for Carryminati \n Press 3 for other channel\n")
         if lock4=="1":
             print("Opening BB ki vine channel")
             webbrowser.open("https://www.youtube.com/channel/UCqwUrj10mAEsqezcItqvwEw")
         elif lock4=="2":
             print("Opening Carryminati channel")
             webbrowser.open("https://www.youtube.com/user/AddictedA1")
         elif lock4=="3":
             channel = input("enter the channel u want to watch:\n")
             print(f"Opening {channel}")
             webbrowser.open(f"https://www.youtube.com/results?search_query={channel}&sp=EgIQAg%253D%253D")
         else:
             print("Dhang se likh")
    elif lock2=="3":
        print("Opening pº®n site..Bahut shaukh hain dekhne ka..")
        webbrowser.open("https://www.xvideos3.com/")
    elif lock2=="4":
        print("Press 1 for roblox")
        print("Press 2 for friv")
        choice_game = input()
        if choice_game=="1":
            print("Opening roblox")
            webbrowser.open("https://www.roblox.com/")
        elif choice_game=="2":
            print("Opening friv")
            webbrowser.open("https://www.friv.com/")
        else:
            print("Abe dhank se likh")
    elif lock2=="5":
         lock3=input("Which streaming service would u prefer:\n Press 1 for Netflix \n Press 2 for primevideo\n")
         if lock3=="1":
            print("Opening netflix")
            webbrowser.open("https://www.netflix.com")
         elif lock3=="2":
            print("opening primevideo")
            webbrowser.open("https://www.primevideo.com")
         else:
           print("Bhai in dono mein se ek bata..")
    elif lock2=="6":
        print("opening leaning site")
        webbrowser.open("https://www.duolingo.com/")
    elif lock2=="7":
        print("Opening artworks")
        webbrowser.open("https://artsandculture.google.com/")
    elif lock2 == "8":
        print("Opening website")
        webbrowser.open("https://zoom.us")
    elif lock2 == "9":
        print("Opening Chess")
        webbrowser.open("https://www.chess.com/play/computer")
    elif lock2 == "10":
        print("Abey zyada others kar raha hain toh khud idea dede \nmail ur tharak idea to tharakidea@gmail.com")
    else:
        print("Abey Saale inn no.s mein se dekh..")
elif lock.lower()=="no":
    print("Bhaad mein jaa..puri duniya bore hori hain tu hi nahi hora..")
else:
    print("Abey Saale dhang se likh..")

