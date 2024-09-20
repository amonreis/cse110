# Import the math module so I can use the math.pi and math.sqrt.
import math

# Import the datatime module so that it can be used in this program.
from datetime import datetime

# Print a description of this program for the user to see.

print("\nThis program computes and outputs the volume of space inside a car tire and") 
print("calculates the price of the tire according to your wheel size and type of tire.\n")

# Get the width, aspect ratio and the diameter from the user.
width = float(input("Enter the width of the tire in mm (ex 205): "))
a_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

# Compute the volume of space inside a tire
volume = math.pi * (width **2) * a_ratio * ((width * a_ratio) + (2540 * diameter)) / 10000000000

# Round the volume to one digit after the decimal point.
volume = round(volume, 2)

# Print the volume of space in the tire
print(F"The approximate volume inside the tire is {volume} liters")
print()


# Call the now() method to get the current date and time from 
# the computer's operating system and store it in a variable
current_date_and_time = datetime.now()

user_answer = "yes"


with open("volumes.txt", "at") as volumes:

    print(f"\n{current_date_and_time:%Y-%m-%d}\n", file=volumes)
    print(f"Width of the tire: {round(width)} mm", file=volumes)
    print(f"Aspect ratio of the tire: {round(a_ratio)}", file=volumes)
    print(f"Diameter of the wheel: {round(diameter)} in", file=volumes)
    print(f"Volume of the tire: {volume} liters", file=volumes)


    print("--- Welcome to the ARO13 Online Tire Store ---")
    

    while user_answer.lower() != "no":
        user_answer = input("\nWould you like to take a look for the price of\na tire corresponding to its measurements? (yes/no): ")
    
        if user_answer.lower() == "yes":
            print("\nWhat is the diameter of the wheel?")
            print("13    AVAILABLE      14 (coming soon)")
            print("15 (out of stock)    16 (out of stock")
            print("17 (out of stock)    18 (out of stock)")    
            print("19 (out of stock)    20 (out of stock")
            aro = input("Select one of the above: ")
            
            if aro == "13":
                print("\nWhat is the width of the tire?")
                print("145    155    165    175")
                print("    185    205    235")
                width = input("Select one of the above: ")
            
                if width == "145":
                    ratio = input("\nWhat is the aspect ratio of the tire (70 or 80)? ")

                    if ratio == "70":
                        print("\nThe price of a tire (145/70R13) is $36,37.")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 36.37 * 4 * 0.3 
                            price = (36.37 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 36.37
                            print(f"The total is: ${price:.2f}.")
                        
                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("145/70R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")

                    elif ratio == "80":
                        print("\nThe price of a tire (145/80R13) is $61,64.")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 61.64 * 4 * 0.3 
                            price = (61.64 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 61.64
                            print(f"The total is: ${price:.2f}.")
                        
                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("145/80R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")

                if width == "155":
                    ratio = input("What is the aspect ratio of the tire (65, 70 or 80)? ")
                
                    if ratio == "65":
                        print("\nThe price of a tire (155/65R13) is $68,61.")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 68.61 * 4 * 0.3 
                            price = (68.61 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 68.61
                            print(f"The total is: ${price:.2f}.")
                        
                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("155/65R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")

                    elif ratio == "70":
                        print("\nThe price of a tire (155/70R13) is $54,65")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 54.65 * 4 * 0.3 
                            price = (54.65 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 54.65
                            print(f"The total is: ${price:.2f}.")
                        
                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("155/70R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")

                    elif ratio == "80":
                        print("\nThe price of a tire (155/80R13) is $63,75.")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 63.75 * 4 * 0.3 
                            price = (63.75 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 63.75
                            print(f"The total is: ${price:.2f}.")
                        
                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("155/80R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")
                
                if width == "165":
                    print("What is the aspect ratio of the tire?")
                    print("60    65")
                    print("70    80")
                    ratio = input("Select one of the above: ")

                    if ratio == "60":
                        print("\nThe price of a tire (165/60R13) is $54,89")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 54.89 * 4 * 0.3 
                            price = (54.89 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 54.89
                            print(f"The total is: ${price:.2f}.")
                        
                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("165/60R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")

                    elif ratio == "65":
                        print("\nThe price of a tire (165/65R13) is $61,99")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 61.99 * 4 * 0.3 
                            price = (61.99 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 61.99
                            print(f"The total is: ${price:.2f}.")

                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("165/65R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")   

                    elif ratio == "70":
                        print("\nThe price of a tire (165/70R13) is $59.99")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 59.99 * 4 * 0.3 
                            price = (59.99 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 59.99
                            print(f"The total is: ${price:.2f}.")

                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("165/70R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")

                    elif ratio == "80":
                        print("\nThe price of a tire (165/80R13) is $64,74")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 64.74 * 4 * 0.3 
                            price = (64.74 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 64.74
                            print(f"The total is: ${price:.2f}.")

                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("165/80R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")
                    
                if width == "175":
                    print("What is the aspect ratio of the tire?")
                    print("50    60    65")
                    print("   70    80")
                    ratio = input("Select one of the above: ")

                    if ratio == "50":
                        print("\nThe price of a tire (175/50R13) is $52,03")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 52.03 * 4 * 0.3 
                            price = (52.03 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 52.03
                            print(f"The total is: ${price:.2f}.")

                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("175/50R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")

                    elif ratio == "60":
                        print("\nThe price of a tire (175/60R13) is $65,65")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 65.65 * 4 * 0.3 
                            price = (65.65 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 65.65
                            print(f"The total is: ${price:.2f}.")

                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("175/60R13", file=volume)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")

                    elif ratio == "65":
                        print("\nThe price of a tire (175/65R13) is $69.68")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 69.68 * 4 * 0.3 
                            price = (69.68 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 69.68
                            print(f"The total is: ${price:.2f}.")

                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("175/65R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")  

                    elif ratio == "70":
                        print("\nThe price of a tire (175/70R13) is $64,99")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 64.99 * 4 * 0.3 
                            price = (64.99 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 64.99
                            print(f"The total is: ${price:.2f}.")

                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("175/70R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")

                    elif ratio == "80":
                        print("\nThe price of a tire (175/80R13) is $106,99")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 106.99 * 4 * 0.3 
                            price = (106.99 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 106.99
                            print(f"The total is: ${price:.2f}.")

                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("175/80R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!") 

                if width == "185":
                    print("What is the aspect ratio of the tire?")
                    print("60    70    80")
                    ratio = input("Select one of the above: ")

                    if ratio == "60":
                        print("\nThe price of a tire (185/60R13) is $78,61")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 78.61 * 4 * 0.3 
                            price = (78.61 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 78.61
                            print(f"The total is: ${price:.2f}.")

                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("185/60R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")

                    elif ratio == "70":
                        print("\nThe price of a tire (185/70R13) is $77,99")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 77.99 * 4 * 0.3 
                            price = (77.99 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 77.99
                            print(f"The total is: ${price:.2f}.")

                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("185/70R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")   

                    elif ratio == "80":
                        print("\nThe price of a tire (185/80R13) is $124,74")
                        n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                        if n_tires == 4:
                            disc = 124.74 * 4 * 0.3 
                            price = (124.74 * 4) - (disc)
                            print(f"The total with discount is ${price:.2f}")
                        else:
                            price = n_tires * 124.74
                            print(f"The total is: ${price:.2f}.")

                        purchase = input("\nContinue purchase (y/n)? ")
                        if purchase.lower() == "y":
                            name = input("Enter your name: ")
                            print(f"Name: {name}", file=volumes)
                            p_number = input("Enter your phone number: ")
                            print(f"Phone Number: {p_number}", file=volumes)
                            print("185/80R13", file=volumes)
                            print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                            print("Thank you!")
                        else:
                            print("Thank you!")    

                if width == "205":
                    print("\nThe price of a tire (205/60 R13) is $88,99")
                    n_tires = int(input("\nHow many tires would you like to order 1, 2, 3 or 4(full pack)?\nBuying a pack with 4 you get a discount of 30%: "))
                    if n_tires == 4:
                        disc = 88.99 * 4 * 0.3 
                        price = (88.99 * 4) - (disc)
                        print(f"The total with discount is ${price:.2f}")
                    else:
                        price = n_tires * 88.99
                        print(f"The total is: ${price:.2f}.")

                    purchase = input("\nContinue purchase (y/n)? ")
                    if purchase.lower() == "y":
                        name = input("Enter your name: ")
                        print(f"Name: {name}", file=volumes)
                        p_number = input("Enter your phone number: ")
                        print(f"Phone Number: {p_number}", file=volumes)
                        print("205/60 R13", file=volumes)
                        print(f"N° Tires: {n_tires} - Total: {price:.2f}", file=volumes)
                        print("Thank you!")
                    else:
                        print("Thank you!")

                if width == "235":
                    print("This product is out of stock :( Try selecting a different option.")

            else:
                print("\nThis is not a valid option. Please try selecting a different option.\n")

        elif user_answer.lower() != "no":
            print("\nThis is not a valid option. Please try selecting a different option.\n")

print("\nThe prices were based on the model, brand and type of tire.\n")
print("Src: Itaro / Firelli / Firestone / Continental / Atlas Tires / Rinaldi / Michelin / Bridgestone / Goodyear etc..")
print("\nGoodbye!")



