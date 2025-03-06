import book_data
import add_book
import view_books
import remove_book
import search_book

def main():
    while True:
        print("\n Book Store Management System")
        print("- Add Book")
        print("- View Books")
        print("- Remove Book")
        print("- Search Book")
        print("- Exit")

        choice = input("Enter your choice: ").strip().lower()

        if choice in ["add book", "add"]:
            add_book.add_book()
        elif choice in ["view books", "view"]:
            view_books.view_books()
        elif choice in ["remove book", "remove"]:
            remove_book.remove_book()
        elif choice in ["search book", "search"]:
            search_book.search_book()
        elif choice in ["exit", "quit"]:
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
