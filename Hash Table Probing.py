# Hash Table Implementation using Division Method and Linear Probing

SIZE = 10
hash_table = [-1] * SIZE    # -1 represents an empty slot

def hash_function(key):
    return key % SIZE        # Division method

def insert(key):
    index = hash_function(key)

    # If collision occurs, find next empty slot
    while hash_table[index] != -1:
        index = (index + 1) % SIZE   # Linear probing (wrap around)
    hash_table[index] = key
    print(f"Inserted {key} at index {index}")

def search(key):
    index = hash_function(key)
    start = index

    # Probe until we find the key or reach an empty slot
    while hash_table[index] != -1:
        if hash_table[index] == key:
            print(f"{key} found at index {index}")
            return
        index = (index + 1) % SIZE
        if index == start:
            break
    print(f"{key} not found in hash table")

def display():
    print("\nCurrent Hash Table:")
    for i in range(SIZE):
        print(f"Index {i}: {hash_table[i]}")

# ------------------- Main Menu -------------------
while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        key = int(input("Enter key to insert: "))
        insert(key)

    elif choice == "2":
        key = int(input("Enter key to search: "))
        search(key)

    elif choice == "3":
        display()

    elif choice == "4":
        break

    else:
        print("Invalid choice! Try again.")