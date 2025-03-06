import book_data

def remove_book():
    books = book_data.load_books()

    if not books:
        print("No books available to remove!")
        return 


    isbn_to_remove = input("Enter the ISBN of the book to remove: ").strip()

    for book in books:
        if book["ISBN"] == isbn_to_remove:
            books.remove(book)
            book_data.save_books(books)
            print(f"Book '{book['Title']}' removed successfully!")
            return
        
print("No book found with that ISBN! Please try again.")