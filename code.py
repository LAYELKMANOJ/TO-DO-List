import json
database = "database.json"


def load_database():
    try:
        with open(database, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []




def save_database(data):
    with open(database, "w") as file:
        json.dump(data, file, indent=4)

user_input = "random"
data = load_database()  


def show_menu():
    print("Hai.... Welcome to DO-TO List")
    print('MENU....')
    print("1. Add items to the list")
    print("2. Mark completed items")
    print("3. View items in the to-do list")
    print("4. Exit")



while user_input != "4":
    show_menu()
    user_input = input("Enter your choice from the menu: ")



    if user_input == "1":
        item = input("What do you need to do today? ")
        data.append(item)
        save_database(data)  # Save changes to the file
        print("Item added:", item)



    elif user_input == "2":
        item = input("What items have you completed? ")
        if item in data:
            data.remove(item)
            save_database(data)  # Save changes to the file
            print("Item marked as completed and removed from the list.")
        else:
            print("Oops, you forgot to add it to the to-do list.")

    elif user_input == "3":
        print("Things pending to do today:")
        print(data)

    elif user_input == "4":
        print("Goodbye! You did a Great job.")
    else:
        print("Please Ensure you entered a valid Menu Option.")
