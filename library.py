import main


def mainMenu():
    library=main.Library()
    star = "*******************************************************************************************************************"
    print(star)
    print('Welcome Ajish Library'.center(115, ' '))
    print(star)
    while True:
        userInput=input("1 List All Book\n2 Borrowing Book\n3 Returning Book\n4 Add Book\n5 Delete Book\n6 Quit\n")
        if userInput not in ["1", "2", "3", "4", "5", "6"]:
            print("\nPlease enter Valid Entry 1-6")
            continue
        else:
            if userInput=="1":
                print('\n')
                library.listBook()
            elif userInput=="2":
                print('\n')
                bookName=input("Enter the Book Name to you want: ")
                library.borrowingBook(bookName)
            elif userInput=="2":
                print('\n')
                library.returningBook()
            elif userInput=="2":
                print('\n')
                library.addBook()
            elif userInput=="2":
                print('\n')
                library.deleteBook()
            if userInput=="6":
                print("Thanks for Visiting Library")
                break



mainMenu()