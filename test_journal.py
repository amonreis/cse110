"""Verify if the functions in the Journal Program work properly"""

from journal import get_random_prompt, append_entry, prompt_list
from datetime import datetime
import csv
import pytest 

def test_get_random_prompt():

    test_prompt_list = [
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
    
    # Assert that the prompt_list contains each of the prompts above
    assert len(prompt_list) == len(test_prompt_list)
    assert prompt_list == test_prompt_list

    # Assert that all the prompts are strings
    for prompt in prompt_list:
        assert isinstance(prompt, str)

    # Assert that the get_random_prompt function sucessfuly returns a random prompt from the promt list    
    for _ in range(4):

        # Call the get_random_prompt function and store it's return in a variable
        random_prompt = get_random_prompt()

        assert random_prompt in prompt_list


def test_append_entry():

    # Create a empty list fot appending
    test_entries = []

    # Create an example list for asserting
    entries = [
        "My day was good",
        "I love Christmas and Christ",
        "I want to become the best developer ever"
    ]
    
    # Call the 'append_entry' function to test if it correctly appends 
    # the elements of the entries list in the 'journal.csv' file
    append_entry("journal.csv", entries)

    # Open the 'journal.csv' file for reading and assert that the entries are inside the file
    with open("journal.csv", "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # Skip the first line of the csv file
        next(reader)

        # Read the rows in the CSV file one row at a time and append each one to the 'test_entries' list
        for row_list in reader:
            test_entries.append(row_list)

        # Take the last element of that list 
        last_list = test_entries[-1]

        # Assert that those elements in the 'entries' list are the same in the 'test_entries' one
        assert "My day was good" in last_list[1]
        assert "I love Christmas and Christ" in last_list[2]
        assert "I want to become the best developer ever" in last_list[3]
        
        # Assert that the function correctly takes the date from the user's computer operating system
        current_date = datetime.now()
        assert last_list[0] == f"{current_date:%d/%m/%Y}"
    

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])