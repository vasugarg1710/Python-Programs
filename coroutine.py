import time
def name_search():
    time.sleep(3)
    names = "harry larry rohan skillf tanay vasu maary "
    while True:
        text = (yield)
        if text in names:
            print("Your name is in the list")
        else:
            print("Your name is not in the list.")


search = name_search()
print("Search started")
print("Running the next method....")
next(search)
search.send("vasu")
search.send("carry")
search.close()

