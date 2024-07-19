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
    def deleteBook(self,book_name):
        try:
            with open("./book.json", "r") as f:
                data = json.load(f)
            
            # Find the book by name and remove it
            original_length = len(data["books"])
            data["books"] = [book for book in data["books"] if book["title"] != book_name]
            new_length = len(data["books"])
            print(data["books"])
            if new_length < original_length:
                # Write the updated data back to the file
                with open("./book.json", "w") as f:
                    json.dump(data, f, indent=4)
                print(f"The book '{book_name}' has been deleted.")
            else:
                print(f"No book found with the name '{book_name}'.")
                    
        except Exception as e:
            print(f"Error: {e}")
    def bookExisting(self,bookName):
        try:
            with open("./book.json") as f:
                data = json.load(f)
                for book in data["books"]:
                    if book["title"].lower()==bookName.lower():
                        print("Please Take it. And carefully handle the book and ensure it is returned on time.")
                else:
                    print("The book is not in the library's inventory; it is currently borrowed.")
        except Exception as e:
            print(f"Error: {e}")
if __name__ == "__main__":
    library = Library()
    library.listBook()
