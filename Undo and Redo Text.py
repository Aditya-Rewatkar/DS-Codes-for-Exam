undo_stack = []
redo_stack = []
text = ""

def write(text_to_add):
    global text
    undo_stack.append(text)
    text += text_to_add
    redo_stack.clear()

def undo():
    global text
    if not undo_stack:
        print("Nothing to undo")
        return
    redo_stack.append(text)
    text = undo_stack.pop()

def redo():
    global text
    if not redo_stack:
        print("Nothing to redo")
        return
    undo_stack.append(text)
    text = redo_stack.pop()

while True:
    print("\n--- Text Editor ---")
    print("Current text: ", text)
    print("1. Write")
    print("2. Undo")
    print("3. Redo")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        data = input("Enter text to add: ")
        write(data)
    elif choice == "2":
        undo()
    elif choice == "3":
        redo()
    elif choice == "4":
        break
    else:
        print("Invalid choice")