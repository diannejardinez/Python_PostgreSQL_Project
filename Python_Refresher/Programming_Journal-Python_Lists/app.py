# Objective: Creating programming journal

# Importing database.py to connect it to app.py
from database import add_entry, get_entries


# User Menu 
menu = """Please select one of the following options:
1. Add new entry for today
2. View entries
3. Exit

Your selection: """

# Welcome message
welcome = "Welcome to the Programming Journal!"
print(welcome)

# Function for adding new entry
def prompt_new_entry():
    # user input questions
    entry_content = input("What have you learned today? " )
    entry_date = input("Enter the date: " )
    # Using add_entry function in database.py
    add_entry(entry_content, entry_date)

# Funtion for getting all entries
def prompt_view_entry(entries):
    # Printing out all entries currently in the programming journal
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


# # Using Python ists as an in-memory database
# entries = [
#     {"content": "Today I started learning programming.", "date": "02-11-2020"},
#     {"content": "I created my first SQLite database!", "date": "04-16-2020"},
#     {"content": "Today I'm going to continue learning programming", "date": "08-13-2020"},
#     {"content": "I finished writing my programming journal application", "date": "08-13-2020"}
# ]


# User input for menu option
user_input = input(menu)

# Menu option conditions
while user_input != "3":
    if user_input == "1":
        prompt_new_entry()

    elif user_input == "2":
        # Using get_entries function in database.py
        prompt_view_entry(get_entries())

    else:
        print("Invalid option, please try again")

    user_input = input(menu)

