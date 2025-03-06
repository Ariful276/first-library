import json 
import os

Books_File = "book.json"

def load_books(): 
    if not os.path.exists(Books_File): 
        return []
    try:
        with open(Books_File, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: books.json is corrupted. Resetting file.")
        return []


def save_books(books): 
    with open(Books_File, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)

