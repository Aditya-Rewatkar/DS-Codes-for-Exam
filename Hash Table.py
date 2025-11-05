SIZE = 10
hash_table = [-1] * SIZE   # -1 means empty slot

def hash_function(key):
    return key % SIZE

def insert(key):
    index = hash_function(key)

    # Linear probing
    while hash_table[index] != -1:
        index = (index + 1) % SIZE
    
    hash_table[index] = key
    print("Inserted", key)

def search(key):
    index = hash_function(key)
    start = index

    # Linear probing search
    while hash_table[index] != -1:
        if hash_table[index] == key:
            print(key, "found at index", index)
            return
        index = (index + 1) % SIZE
        if index == start:
            break

    print(key, "not found")

def display():
    for i in range(SIZE):
        print(i, ":", hash_table[i])

# Menu
while True:
    print("\n1. Insert")
    print("2. Search")
    print("3. Display")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        key = int(input("Enter number: "))
        insert(key)
    
    elif ch == "2":
        key = int(input("Enter number to search: "))
        search(key)

    elif ch == "3":
        display()
    
    elif ch == "4":
        break
    
    else:
        print("Invalid choice")