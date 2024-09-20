import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2

def main():
    try:
        # Call the read_compound_list function to read 
        # the pupils.csv and store it in a variale
        students_list = read_compound_list("pupils.csv")

        # Write a lambda function that will extract the birthdate from a student.
        birthdate = lambda students_list: students_list[BIRTHDATE_INDEX]

        # Write a lambda function that will extract the given name from a student.
        given_name = lambda students_list: students_list[GIVEN_NAME_INDEX]

        # Write a call to the Python built-in sorted function that will sort the
        # students_list by birthdate from oldest to youngest.
        sorted_list_by_birthdate = sorted(students_list, key=birthdate)

        # Write a call to the Python built-in sorted function that will sort the
        # students_list by given name in alphabetical order
        sorted_list_by_given_name = sorted(students_list, key=given_name)

        print("\nOrdered from Oldest to Youngest")
        print(print_list(sorted_list_by_birthdate))

        print("\nOrdered by given name")
        print(print_list(sorted_list_by_given_name))


    except (FileNotFoundError, PermissionError ) as error:
        print(type(error).__name__, error, sep=": ")


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            clean_row = row.strip()
            # Append the current row at the end of the compound list.
            compound_list.append(clean_row)

    return compound_list


def print_list(_list):
    '''Prints each element of a list on a separate line
    
    Parameter
        compound_list: a compound list
    Return: a list 
    '''
    for line in _list:
        print(line)


if __name__ == "__main__":
    main()
    