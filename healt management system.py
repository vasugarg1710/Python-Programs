def log(client_name,data,log_choice):
    if log_choice==1:
        f = open(f"{client_name}_exercise.txt","a");
        f.write(data)
        f.write("\n")
        f.close()
        print("Data has been successfully added to the file.")
    elif log_choice==2:
        f = open(f"{client_name}_diet.txt", "a");
        f.write(data)
        f.write("\n")
        f.close()
        print("Data has been successfully added to the file.")
    else:
        print("Invalid input")

def retrieve(client_name):
    if retrieve_choice==1:
        f = open(f"{client_name}_exercise.txt");
        content =  f.read()
        print(content)
        f.close()
    elif retrieve_choice==2:
        f = open(f"{client_name}_diet.txt");
        content = f.read()
        print(content)
        f.close()
    else:
        print("Invalid Input")

print("What do you want to do: \nPress 1 for log \nPress 2 for retrieve")
choice = int(input())
if choice==1:
    print("For whom you are logging:\nHarry\nRohan\nHamad\nMake sure you enter the name not the number")
    client_name = input()
    print("What do you want to log:  \nPress 1 for Exercise \nPress 2 for Diet")
    log_choice = int(input())
    print("Enter your data:")
    data = input()
    log(client_name,data,log_choice)
elif choice==2:
    print("For whom you are retrieving:\nHarry\nRohan\nHamad\nMake sure you enter the name not the number")
    client_name = input()
    print("What do you want to retrieve\nPress 1 for Exercise \nPress 2 for Diet")
    retrieve_choice = int(input())
    retrieve(client_name)
else:
    print("Invalid Input")



