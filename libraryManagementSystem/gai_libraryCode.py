class Library:
    def __init__(self, file_name="books.txt"):
        self.file_name = file_name
        self.file = open(self.file_name, "a+")

    def __del__(self):
        self.file.close()

    def addBook(self, book_data):
        with open(self.file_name, "a", encoding="utf-8") as file:
            file.write(",".join(book_data) + "\n")
        print("Book added successfully!")

    def removeBook(self, book_name):
        with open(self.file_name, "r") as file:
            lines = file.readlines()
        with open(self.file_name, "w") as file:
            for line in lines:
                if book_name not in line:
                    file.write(line)
        print("Book removed successfully!")

    def displayBook(self):
        print("\nThe Book that You Search: \n")
        with open(self.file_name, "r") as file:
            for line in file:
                book_data = line.strip().split(",")
                print("Book Name:", book_data[0])
                print("Author:", book_data[1])
                print("Release Year:", book_data[2])
                print("Number of Pages:", book_data[3])
                print()

    def searchBook(self, book_name):
        found = False
        with open(self.file_name, "r") as file:
            for line in file:
                book_data = line.strip().split(",")
                if book_name.lower() in book_data[0].lower():
                    print("Book found:")
                    print("Book Name:", book_data[0])
                    print("Author:", book_data[1])
                    print("Release Year:", book_data[2])
                    print("Number of Pages:", book_data[3])
                    print()
                    found = True
        if not found:
            print("Book not found.")

if __name__ == "__main__":
    library = Library()

    while True:
        print("\n1. Add Book")
        print("2. Remove Book")
        print("3. List Books")
        print("4. Search Book")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            book_data = [
                input("Enter Book Name: "),
                input("Enter Author Name: "),
                input("Enter Release Year of the Book: "),
                input("Enter Number of Pages: ")
            ]
            library.addBook(book_data)

        elif choice == "2":
            book_name = input("Enter Book Name to be removed: ")
            library.removeBook(book_name)

        elif choice == "3":
            library.displayBook()

        elif choice == "4":
            book_name = input("Enter Book Name to be searched: ")
            library.searchBook(book_name)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")
