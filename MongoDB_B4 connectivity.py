pip install pymongo


# Import pymongo
from pymongo import MongoClient

# Step 1: Connect to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Step 2: Create or connect to database
db = client["studentDB"]

# Step 3: Create or connect to collection
collection = db["students"]

# ---------------- MENU OPERATIONS ----------------

def add_student():
    name = input("Enter Student Name: ")
    roll = int(input("Enter Roll Number: "))
    branch = input("Enter Branch: ")
    record = {"name": name, "roll": roll, "branch": branch}
    collection.insert_one(record)
    print("Student added successfully!\n")

def display_students():
    print("\n--- Student Records ---")
    for s in collection.find():
        print(s)

def update_student():
    roll = int(input("Enter Roll Number to Update: "))
    new_branch = input("Enter New Branch: ")
    collection.update_one({"roll": roll}, {"$set": {"branch": new_branch}})
    print("Record updated successfully!\n")

def delete_student():
    roll = int(input("Enter Roll Number to Delete: "))
    collection.delete_one({"roll": roll})
    print("Record deleted successfully!\n")

# ---------------- MAIN MENU ----------------

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        update_student()
    elif choice == 4:
        delete_student()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.")
