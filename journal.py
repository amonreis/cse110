from random import choice
from datetime import datetime
import csv

'''Journal Program '''

# This program was invented with the purpose of helping you keep a journal
# writing on it everyday by answering to simple random prompts 

# Get the current date from the user's computer operating system
current_date = datetime.now()

# Creat a empty list to hold the user's entries
entries = []

# Creat a list to hold the prompts
prompt_list = [
    "What was the best part of my day?",
    "How did I see the hand of the Lord in my life today?",
    "What would you have done differently today?",
    "When/Where did you feel happiest today? Why?",
    "What are three things you're grateful for today?",
    "What steps did you take today towards a goal you're working on?",
    "What is something I can start doing today that my future self will thank me for in one year?",
    "What do you need the most right now? How can you meet that need?",
    "If I had one thing I could do over today, what would it be?",
    "Write a little bit of your day"
]


def main():
    
    DATE_INDEX = 0

    ''' User Interface'''

    # Display a welcoming message 
    print("\nWelcome to the Journal Program!")

    # Ask the user to start the program
    start = input("\nWould you like to start (yes/no)?\n\n>> ")

    while start.lower() != "no":

        ## MENU ##
        menu = ["\nPlease select one of the following choices: (1-5)",
                "1. Write",
                "2. Display",
                "3. Save",
                "4. Load",
                "5. Quit"
                ]

        # Display the Journal Menu
        for option_line in menu:
            print(option_line)

        # Allow the user to choose an option
        user_input = int(input("\n>> "))
        print()
 
        if user_input == 1:

            # Generate and print a random prompt
            random_prompt = get_random_prompt()
            print(f"\n{random_prompt}")

            # Allow the user to type in the answer to the prompt and append the entry to the "entries" list
            entry = input("\n>> ")
            entries.append(entry)

        elif user_input == 2:
                # Display the current date
                print(f"{current_date:%B %d %Y} ({current_date:%A})\n")
                
                # Display the entries on the screen
                for i in entries:
                    print(i)
                
        elif user_input == 3:

            # Call the "append_entry" function and append the entries in the journal.csv file
            append_entry("journal.csv", entries)

        elif user_input == 4:
            
            # Ask the user for a date to find the entries of that day
            user_key = input("Choose a date (DD/MM/YYYY)\n\n>>")

            # Call the "read_dictionary" function to read the csv file into a compound dictionary (use the date as the key)
            dictionary = read_dictionary("journal.csv", DATE_INDEX)

            # Find the entries according to the day in the dictionary and display them all
            if user_key in dictionary:

                value = dictionary[user_key]
                
                value.pop(0)
                # print a empty line
                print()

                for i in value:
                    
                    print(i)

            # Display "Not found if there's no entries in the day selected by the user"
            else:
                print("\nNot found")


        elif user_input == 5:
            print("ヘ( ^o^)/\(^_^ )")
            print("\nThanks for wrinting today!")
            break

        else:
            print("Invalid option, choose a valid one.")
                 

def get_random_prompt():
    """Randomly choose a prompt from the prompt list and return it
    Parameters: none
    Return: a randomly prompt
    """

    # Append prompts to the prompt list


    # Randomly choose a prompt from the list  
    random_prompt = choice(prompt_list)

    # Return a random prompt
    return random_prompt
    

def append_entry(filename, listname):
    """Append user's entries in a csv file.
    Parameters: a filename (in which the entries will be saved),
    and a list (where the entries are)
    Return: None"""

    # Open or create the file "journal.csv" for appending
    with open(filename, "at") as csv_file:

        # Print the current date and the list into the csv file
        print(f"{current_date:%d/%m/%Y},{listname}", file=csv_file)
        

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:
        
        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:
            
            # From the current row, retrieve the data
            # from the column that contains the key.
            key = row_list[key_column_index]

            # Store the data from the current
            # row into the dictionary.
            dictionary[key] = row_list

    # Return the dictionary.
    return dictionary


if __name__ == "__main__":
    main()