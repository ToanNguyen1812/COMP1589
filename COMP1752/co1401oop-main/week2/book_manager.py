# from file_name import function_name, variable_name
from books import books, TITLE, AUTHOR, PRICE, curr_id

def main():
    running = True

    while running:
        print_menu()
        choice = input("Select an option: ")

        if choice == '1':
            display_books()
        elif choice == '2':
            search_book()
        elif choice == '3':
            add_book()
        elif choice == '4':
            edit_book()
        elif choice == '5':
            delete_book()
        elif choice == '6':
            running = False
            print("Exiting the program.")
        else:
            print('Invalid option. Please try again.')

def print_menu():
    print("\nBook Management Menu")
    print("1. Display all books")
    print("2. Search for a book by ID")
    print("3. Add a new book")
    print("4. Edit a book by ID")
    print("5. Delete a book by ID")
    print("6. Exit")

def display_books():
    print('All Books:')
    print(f'{"ID":<5} {"Title":<30} {"Author":<25} {"Price":<10}')
    for book_id, book_info in books.items():
        print(f'{book_id:<5}', end=' ')
        title = book_info[TITLE]
        author = book_info[AUTHOR]
        price = book_info[PRICE]
        print(f'{title:<30} {author:<25} ${price:<10.2f}')

def search_book():
    bid = int(input("Enter Book ID to search: "))
    if bid not in books:
        print("Book not found.\n\n")
        return
    
    title = books[bid][TITLE]
    author = books[bid][AUTHOR]
    price = books[bid][PRICE]
    print(f'Book Found - ID: {bid}, Title: {title}, Author: {author}, Price: ${price:.2f}\n\n')

def add_book():
    # enter title
    title = input("Enter Book Title: ")
    # enter author
    author = input("Enter Book Author: ")
    # enter price
    price = float(input("Enter Book Price: "))
    # create list for new book
    book_info = [title, author, price]

    # get new ide by incrementing curr_id
    global curr_id
    curr_id += 1
    new_id = curr_id

    # add new book (new_id, book_info) to books dictionary
    books[new_id] = book_info
    
    # print success message
    print(f"Book added successfully with ID: {new_id}")

def edit_book():
    # enter book id to edit
    bid = int(input("Enter Book ID to edit: "))
    # check if book id exists
    if bid not in books:
        print("Book not found.\n\n")
        return

    # if exists, enter new title, author, price
    new_title = input("Enter new Title: ")
    new_author = input("Enter new Author: ")
    new_price = float(input("Enter new Price: "))

    book_new_info = [new_title, new_author, new_price]

    # update book info in books dictionary
    books[bid] = book_new_info

    # print success message
    print(f"Book with ID: {bid} has been updated successfully.\n\n")

def delete_book():
    bid = int(input("Enter Book ID to delete: "))
    if bid not in books:
        print("Book not found.\n\n")
        return
    
    # delete book from books dictionary
    del books[bid]
    print(f"Book with ID: {bid} has been deleted successfully.\n\n")

if __name__ == "__main__":
    main()