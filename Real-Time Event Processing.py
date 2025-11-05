from collections import deque

queue = deque() #Because a normal Python list is trash for queue operations — popping from the front of a list is O(n) (slow).

def add_event():
    event = input("Enter event description: ")
    queue.append(event)
    print("Event added.")

def process_event():
    if not queue:
        print("No events to process.")
        return
    event = queue.popleft()
    print(f"Processing event: {event}")

def view_events():
    if not queue:
        print("No pending events.")
        return
    print("Pending events:")
    for e in queue:
        print("→", e)

while True:
    print("\n--- Real-Time Event Queue ---")
    print("1. Add Event")
    print("2. Process Event")
    print("3. View Pending Events")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        add_event()
    elif ch == "2":
        process_event()
    elif ch == "3":
        view_events()
    elif ch == "4":
        break
    else:
        print("Invalid choice.")