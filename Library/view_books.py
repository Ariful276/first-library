import book_data 

def view_books():
    books = book_data.laod_books()

    print(f"DEBUG: books = {books}")

    if not books: 
        print("No book was added")
        return
    

    print(" \n Available books ")
    print("=" * 50 )

    for book in books:
        print(f"Title: {book["Title"]}")
        print(f"Author: {book["Author"]}")
        print(f"ISBN: {book["IDBN"]}")
        print(f"Price: ${book["Price: .2f"]}")
        print(f"Quantity in stock: {book["Quantity"]}")
        print("-" * 50)