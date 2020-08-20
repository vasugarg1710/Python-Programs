# Notes adding and retrieving system - done
# Lectures Watching - done
# Test series - done
# Task reminder - done
import os
import webbrowser
import time
from plyer import notification


def surf(url):
    '''This function opens a url'''
    webbrowser.open(url)


class Study:
    def __init__(self, name, std_class):
        self.name = name
        self.std_class = std_class

    def notes(self):
        choice = input("What do you want to do: \nPress 1 for adding the notes\nPress 2 for retrieving the notes.")
        if choice == "1":
            choice_sub = input("Which subject: \n")
            chapter = input("Enter the chapter:\n")
            notes = input("Enter the notes: \n")
            working_path = os.path.join(os.getcwd(), choice_sub)
            if not os.path.isdir(working_path):
                os.mkdir(choice_sub)
                # print("folder created")

            os.chdir(working_path)
            with open(f"{chapter}.txt", "a") as f:
                f.write(f"{notes}\n")
        elif choice == "2":
            choice_sub = input("Which subject: \n")
            chapter = input("Enter the chapter:\n")
            working_path = os.path.join(os.getcwd(), choice_sub)
            os.chdir(working_path)
            with open(f"{chapter}.txt") as f:
                content = f.read()
                print(content)
        else:
            print("Invalid input")

    def lectures_watching(self):
        print("Enter the site:\nPress 1 for byjus\nPress 2 for toppr\nPress 3 for youtube\nPress 4 for cuemath")
        choice_site = input()
        if choice_site == "1":
            surf("https://learn.byjus.com/home/dashboard")
        elif choice_site == "2":
            surf("https://www.toppr.com/")
        elif choice_site == "3":
            surf("https://www.youtube.com/")
        elif choice_site == "4":
            surf("https://leap.cuemath.com/")
        else:
            print("Invalid input")

    def test(self):
        chapter = input("Enter the chapter name: \n")
        surf(f"https://www.bing.com/search?q=class {self.std_class} {chapter} mcq test")

    def task_reminder(self):
        task = input("Enter the task:\n")
        task_time = input("After how much time you want to get a reminder. Enter the time in seconds:\n")
        time.sleep(int(task_time))
        notification.notify(
            title=task,
            message="This is the task that you have to do",
            # displaying time
            timeout=20)
        print("Notification fired")



name = input("What is your name\n")
std_class = input("What is your class (eg. 9)\n")
name = Study(name, std_class)
print("What you want to do:\nPress 1 for notes\nPress 2 to watch lectures\nPress 3 for tests\nPress 4 for task "
      "reminder\n")
ch = input()
if ch == "1":
    name.notes()
elif ch == "2":
    name.lectures_watching()
elif ch == "3":
    name.test()
elif ch == "4":
    name.task_reminder()
else:
    print("Invalid input")
