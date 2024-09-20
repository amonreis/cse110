# Import the datetime library to use the datetime function
from datetime import datetime

# Store the current date and time, and the day of the week in variables
current_date = datetime.now()
weekday = current_date.weekday()

# Ask the user for a subtotal
subtotal = float(input("Please enter the subtotal: "))

if subtotal >= 50 and (weekday == 0 or weekday == 2):
    discount = subtotal * 0.1
    sales_tax = (subtotal - discount) * .06
    total = subtotal - discount + sales_tax

    print(f"Discount amount: {discount:.2f}")
    print(f"Sales tax amount: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")

elif subtotal < 50 and (weekday == 0 or weekday== 2):
    additional_amount = 50 - subtotal
    sales_tax = subtotal * .06
    total = subtotal + sales_tax
    print(f"Sales tax amount: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    print(f"If you make an additional purchase of ${additional_amount:.2f} you can get a 10% discount.")

else:
    sales_tax = subtotal * .06
    total = subtotal + sales_tax

    print(f"Sales tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")

print(weekday)



