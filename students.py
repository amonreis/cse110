import csv

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

    dictionary = {}

    with open(filename, "rt") as csv_file:

        reader = csv.reader(csv_file)

        next(reader)

        for row_list in reader:

            key = row_list[key_column_index]
            
            dictionary[key] = row_list
    
    return dictionary

def main():

    I_NUMBER_INDEX = 0
    NAME_INDEX = 1
    
    dictionary = read_dictionary("students.csv", I_NUMBER_INDEX)

    i_number = input("Please enter an I-Number (xxxxxxxxx): ")

    i_number = i_number.replace("-", "")
    
    if len(i_number) < 9:
        print("You entered an I-Number with too few digits")
    elif len(i_number) > 9:
        print("You entered an I-Number with too many digits")

    
    if i_number in dictionary:

        name = dictionary[i_number]

        print(name[NAME_INDEX])

    else:
        print("No such student")


if __name__=="__main__":
    main()