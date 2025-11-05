borrowed_books = {}  # key: student name, value: book name

def issue_book():
    student = input("Enter student name: ").strip()
    book = input("Enter book name: ").strip()

    if student in borrowed_books:
        print("Error: This student already has a borrowed book.")
        return
    
    borrowed_books[student] = book
    print(f"Book '{book}' issued to {student}.")

def return_book():
    student = input("Enter student name: ").strip()

    if student not in borrowed_books:
        print("Error: No record found for this student.")
        return
    
    returned_book = borrowed_books.pop(student)
    print(f"Book '{returned_book}' returned by {student}.")

def display_records():
    if not borrowed_books:
        print("No borrowing records found.")
        return

    print("\nBorrowing Records:")
    for student, book in borrowed_books.items():
        print(f"Student: {student}  |  Book: {book}")
    print()

def main():
    while True:
        print("\n====== Library Menu ======")
        print("1. Issue Book")
        print("2. Return Book")
        print("3. Display Records")
        print("4. Exit")

        choice = input("Enter choice (1-4): ")

        if choice == '1':
            issue_book()
        elif choice == '2':
            return_book()
        elif choice == '3':
            display_records()
        elif choice == '4':
            print("Exiting Program.")
            break
        else:
            print("Invalid input, enter 1–4 only.")

main()