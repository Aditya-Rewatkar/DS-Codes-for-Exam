class Node:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.next = None

class StudentList:
    def __init__(self):
        self.head = None

    def insert_student(self, roll, name):
        new_node = Node(roll, name)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
        print("Student added.")

    def display(self):
        if self.head is None:
            print("No records.")
            return
        
        temp = self.head
        print("Student Records:")
        while temp is not None:
            print(f"Roll: {temp.roll}, Name: {temp.name}")
            temp = temp.next

    def delete_student(self, roll):
        if self.head is None:
            print("List is empty.")
            return
        
        if self.head.roll == roll:
            self.head = self.head.next
            print("Student deleted.")
            return

        prev = None
        temp = self.head

        while temp is not None and temp.roll != roll:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Student not found.")
        else:
            prev.next = temp.next
            print("Student deleted.")

# -------- Menu --------
s = StudentList()

while True:
    print("\n1. Insert Student")
    print("2. Display Students")
    print("3. Delete Student")
    print("4. Exit")

    ch = input("Enter choice: ")
    
    if ch == "1":
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        s.insert_student(roll, name)

    elif ch == "2":
        s.display()

    elif ch == "3":
        roll = int(input("Enter Roll No to delete: "))
        s.delete_student(roll)

    elif ch == "4":
        break
    
    else:
        print("Invalid choice.")