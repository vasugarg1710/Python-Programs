class Library:
    books_for_lending = {}

    def __init__(self, library_name, list_of_books):
        self.name = library_name
        self.list_of_books = list_of_books

    def addBook(self):  # adds or donate a book
        name_book = input("Enter the book name you want to add:")
        self.list_of_books.append(name_book)
        print(f"Added book {name_book}")

    def deleteBook(self):  # deletes a book from the database
        # used try exception handling so that if the book is not in the database then the program will continue to run
        try:
            delete_book = input("Enter the book you want to delete:")
            self.list_of_books.remove(delete_book)
            print(f"Deleted book {delete_book}")
        except Exception as e:
            print(e)

    def returnBook(self):  # returns a book
        returnBook = input("Enter the book you want to return")
        for key, value in list(self.books_for_lending.items()):
            if returnBook == key:
                print(f"Boook is issued by {self.books_for_lending[returnBook]}")
                print("Returning book....")
                del self.books_for_lending[returnBook]
                print("Book successfully returned")
            else:
                print("Book is not issued yet")

    def issue_book(self):  # issues a book
        name_student = input("Enter your name:\n")
        issue_book = input("Enter the book name you want to issue:\n")

        def isExist():
            for item in self.list_of_books:
                if item == issue_book:
                    return True

        def isIssued():
            for key, value in list(self.books_for_lending.items()):
                # key is the name of book and value is the name of student
                if key == issue_book:
                    print(f"Book is already issued by {value}")
                    return True

        if isExist():
            if isIssued():
                print("You cannot issue this book")

            else:
                self.books_for_lending[issue_book] = name_student
                print(f"Issued book {issue_book} to {name_student}")

                # print(self.books_for_lending)
        else:
            print("Book is not in the database")

    def displayBook(self):  # displays the book
        print("What do you want to display:\n Press 1 for books in the database\n Press 2 for issued books")
        dis = input()
        if dis == "1":
            print(self.list_of_books)
        elif dis == "2":
            print(self.books_for_lending)
        else:
            print("Invalid input")

    def main(self):
        do = input("What do you want to do\n Press 1 to issue a book \n Press 2 to return a book \n Press 3 to delete "
                   "a book from the database \n Press 4 to donate or add a book in the database \n Press 5 to display "
                   "the book\n")
        if do == "1":
            self.issue_book()
        elif do == "2":
            self.returnBook()
        elif do == "3":
            self.deleteBook()
        elif do == "4":
            self.addBook()
        elif do == "5":
            self.displayBook()
        else:
            print("Invalid input")


VasuLibrary = Library("VasuLibrary", ['rd sharma', 'rs aggarwal'])
while True:
    VasuLibrary.main()
