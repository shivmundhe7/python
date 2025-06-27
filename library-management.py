class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.lend_data = {}

    def display_books(self):
        if not self.books:
            print("📚 No books available in the library.")
        else:
            print(f"\n📘 Books in {self.name}:")
            for book in self.books:
                status = f" (Borrowed by {self.lend_data[book]})" if book in self.lend_data else " (Available)"
                print(f" - {book}{status}")

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"✅ '{book_name}' added to the library.")

    def lend_book(self, book_name, user_name):
        if book_name not in self.books:
            print("❌ Book not found in the library.")
        elif book_name in self.lend_data:
            print(f"❌ Book is currently borrowed by {self.lend_data[book_name]}.")
        else:
            self.lend_data[book_name] = user_name
            print(f"✅ '{book_name}' lent to {user_name}.")

    def return_book(self, book_name):
        if book_name in self.lend_data:
            del self.lend_data[book_name]
            print(f"✅ '{book_name}' returned successfully.")
        else:
            print("❌ This book was not borrowed.")

def main():
    lib = Library("Shiv's Library")

    while True:
        print("\n===== Library Menu =====")
        print("1. Display Books")
        print("2. Add Book")
        print("3. Lend Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            lib.display_books()
        elif choice == "2":
            book = input("Enter book name to add: ")
            lib.add_book(book)
        elif choice == "3":
            book = input("Enter book name to lend: ")
            user = input("Enter your name: ")
            lib.lend_book(book, user)
        elif choice == "4":
            book = input("Enter book name to return: ")
            lib.return_book(book)
        elif choice == "5":
            print("👋 Exiting the library system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
