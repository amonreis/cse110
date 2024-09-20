# Import the datetime class from the datetime module
from datetime import datetime
# Import the csv module
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


def main():
    try:
        PRODUCT_INDEX = 1
        PRICE_INDEX = 2
        QUANTITY_INDEX = 1
        PRODUCT_NUM_INDEX = 0

        # Create a list to store the quantities of products ordered by a client
        quantity_list = []
        # Create a list to store the subtotal of the products ordered by a client
        subtotal_list = []

        # Call the read_dictionary function and store the compound dictionary in a variable
        products_dict = read_dictionary("products.csv", 0)

        # Call the now() method to get the current date and time as a  
        # datetime object from the computer's operating system.
        current_date_and_time = datetime.now()

        # Print the store name at the top of the receipt.
        print("KingMart")

        # Print the products_dict.
        # print(f"All Products\n{products_dict}")

        print("\nResqueted Items:\n")

        # Open the request.csv file for reading.
        with open("request.csv", "rt") as csv_file:

            reader = csv.reader(csv_file)
            
            # Skip the  first line of the request.csv file because the first line contains column headings
            next(reader)

            # Use a loop that reads and processes each row from the request.csv file
            for row_list in reader:
                
                # Save the product number in a variable
                product_num = row_list[PRODUCT_NUM_INDEX]
                # Save the quantity of products in a variable
                quantity = int(row_list[QUANTITY_INDEX])

                quantity_list.append(quantity)

                # Use the requested product number to find the corresponding item in the products_dict
                if product_num in products_dict:
                    
                    value = products_dict[product_num]
                    product = value[PRODUCT_INDEX]
                    price = float(value[PRICE_INDEX])
                    
                    i_subtotal = price * quantity
                    
                    subtotal_list.append(i_subtotal)

                    # Print the product name, requested quantity, and product price.
                    print(f"{product}: {quantity} @ {price}")

        # Compute the subtotal
        subtotal = sum(subtotal_list)
        # Compute the sales tax amount. Use 6% as the sales tax rate.
        tax_amount = subtotal * 0.06
        # Compute the total amount due
        total = subtotal + tax_amount

        # Exceeding the requirements
        # Write code to discount the product prices by 10% if today is Tuesday or Wednesday.
        weekday = current_date_and_time.weekday()

        if weekday == 1 or weekday == 2:
            discount = subtotal * .1
            total = subtotal + tax_amount - discount


        # Sum and print the number of ordered items
        print(f"\nNumber of Items: {sum(quantity_list)}")
        # Sum and print the subtotal due rounded
        print(f"Subtotal: {round(subtotal, 2)}")
        # Print the sales tax amount rounded.
        print(f"Sales Tax: {round(tax_amount, 2)}")
        # Print the total amount due rounded.
        print(f"Total: {round(total, 2)}")

        # Display a thank you message.
        print("\nThank you for shopping at the KingMart.")
        # Display the current day of the week and the current time
        print(f"{current_date_and_time:%A %b %d %X %Y}")


    except FileNotFoundError as error:
        print("Error: cannot open file because it doesn't exist. Try selecting a different one.")
        print(error)
    except PermissionError as perm_err:
        print("Error: cannot access this file because you don't have permission to read it.")
        print(perm_err)
    except KeyError as key_err:
        print("Error: unknown product ID in the request.csv file")
        print(key_err)

# If this file was executed like this:
# > python receipt.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__=="__main__":
    main()