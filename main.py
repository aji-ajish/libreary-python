import json

class Library:

    def listBook(self):
        try:
            with open("./book.json") as f:
                data = json.load(f)
                star = "-------------------------------------------------------------------------------------------------------------------"
                print(star)
                print("S.No".ljust(5) + "Book Name".center(50, ' ') + "Author".center(30, ' ') + "Genre".center(20, ' ') + "Year".ljust(5))
                print(star)
                # Initialize a counter for serial numbers
                serial_number = 1
                
                for book in data["books"]:
                    # Print each book's details with serial number
                    print('| '+str(serial_number).ljust(7) +
                          book["title"].ljust(50) +
                          book["author"].ljust(30) +
                          book["genre"].ljust(20) +
                          str(book["year"]).ljust(5)+'|')

                    # Increment serial number for the next book
                    serial_number += 1
                print(star+"\n")      
        except Exception as e:
            print(f"Error: {e}")

    def borrowingBook(self,bookName):
        self.bookExisting(bookName)
    def returningBook(self):
        pass
    def addBook(self):
        pass
    def deleteBook(self):
        pass
    def bookExisting(self,bookName):
        try:
            with open("./book.json") as f:
                data = json.load(f)
                for book in data["books"]:
                    if book["title"].lower()==bookName.lower():
                        print("Take the book")
                else:
                    print("No Book Found")
        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    library = Library()
    library.listBook()
