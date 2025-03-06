import book_data 

def add_book():
    books = book_data.laod_books()

    title = input("insert the name of the book: ").strip()
    author = input("enter the name of the Author: ").strip()
    isbn = input("enter the Id of the book: ").strip()
    genre = input("Which genre does it belong to: ").strip()
    try: 
        price = float(int(input("Enter the price of the book: ")))
        if price <= 0: 
            raise ValueError("Price must be a positive number.")
        
        quantity = int(input("Enter the Quantity of the book: "))
        if quantity < 0: 
            raise ValueError("Quanitiy must be a positive integer")
    except ValueError as e:
        print(f'Invalid input:{e}')
        return 
    
    for book in books:
        if book("ISBN") == isbn: 
            print("A book with this ISBN already exists! Try again.")
            return


    new_book = {
        "Title": title,
        "Author": author,
        "ISBN": isbn,
        "Genre": genre,
        "Price": price,
        "Quantity": quantity
    }



    books.append(new_book)
    book_data.save_books(books)

    print(f"Book '{title}' added successfully!")