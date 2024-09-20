import random

def append_random_numbers(numbers_list, quantity=1):
    """Has two parameters: a list named numbers_list and an integer named 
    quantity. The parameter quantity has a default value of 1"""
    
    for i in range(quantity):
        # Compute quantity pseudo random numbers by
        # calling the random.uniform function.
        random_number = random.uniform(0, 100)

        # Round the quantity pseudo random numbers
        # to one digit after the decimal.
        rounded = round(random_number, 1)

        # Append the quantity pseudo random numbers 
        # onto the end of the numbers_list.
        numbers_list.append(rounded)


def append_random_words(words_list, quantity=1):
    """Has two parameters: a list named words_list and an integer named
    quantity. The parameter quantity has a default value of 1"""
    
    # A list of words to randomly choose from.
    words = ["back", "car", "bow", "writer", "waiting", "happy", "heaven", "love", "authority",
        "different", "interesting", "pizza", "poison", "medicine", "doctor", "protect",
        "suggestion", "decision", "phone", "dogs", "rabbit", "hero"]
    
    for i in range(quantity):
    # Randomly select quantity words from a list of words and
    # appends the selected words at the end of words_list.
        random_word = random.choice(words)
        words_list.append(random_word)


def main():

    # Create a list named numbers and add float numbers
    numbers = [16.2, 75.1, 52.3]
    
    # Print the number list
    print(f"Numbers: {numbers}")

    # Call the append_random_numbers function with only
    # one argument to add one number to numbers
    append_random_numbers(numbers)

    # Print the number list
    print(f"Numbers: {numbers}")

    # Call the append_random_numbers function again with
    # two arguments to add three numbers to numbers
    append_random_numbers(numbers, 3)

    # Print the number list
    print(f"Numbers: {numbers}")

    # Create a list to store random words
    words = []

        # Call the append_random_words function
    # to add one random word to the list.
    append_random_words(words)
    print(f"words {words}")

    # Call the append_random_words function
    # to add five random words to the list.
    append_random_words(words, 5)
    print(f"words {words}")
    
        
if __name__ == "__main__":
    main()