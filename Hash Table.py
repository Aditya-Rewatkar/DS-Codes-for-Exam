# Hash Table implementation using division method and chaining

# Hash table size = 10
SIZE = 10

# Initialize hash table with empty lists (chains)
hash_table = [[] for _ in range(SIZE)]

def hash_function(key):
    return key % SIZE   # Division method

def insert(key):
    index = hash_function(key)
    hash_table[index].append(key)
    print(f"Inserted {key} at index {index}")

def search(key):
    index = hash_function(key)
    if key in hash_table[index]:
        print(f"{key} found at index {index}")
    else:
        print(f"{key} NOT found")

def display():
    for i in range(SIZE):
        print(f"Index {i}:", hash_table[i])

# Main Program
while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Display Hash Table")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        key = int(input("Enter key to insert: "))
        insert(key)

    elif ch == 2:
        key = int(input("Enter key to search: "))
        search(key)

    elif ch == 3:
        display()

    elif ch == 4:
        break

    else:
        print("Invalid choice")