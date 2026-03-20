# Tire Volume Calculator
# This is a basic program that calculates the volume of a tire based on user input and logs the data to a text file.

#from datetime import datetime
#import math

# --- Step 1: Get user input ---
#width = int(input("Enter the width of the tire in mm (ex 205): "))
#aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
#diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

# --- Step 2: Calculate tire volume ---
# Formula: v = (π * w^2 * a * (w * a + 2540 * d)) / 10_000_000_000
#v = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

# Round the volume to 2 decimal places
#volume = round(v, 2)

# --- Step 3: Display the result ---
#print(f"The approximate volume is {volume} liters")

# --- Step 4: Get current date ---
#current_date = datetime.now()

# --- Step 5: Log the data to volumes.txt ---
#with open("volumes.txt", "at") as file:
#    print(f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume}", file=file)


# Tire Volume Calculator with Logging and Purchase Option
# Enhancement: Added tire pricing suggestion for select sizes and an option to record
# customer's phone number if they want to buy the tires.


#Tire Volume Project
from datetime import datetime
import math

# --- Prompt user for input and convert to numbers ---
width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

v = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
volume = round(v, 2)

print(f"The approximate volume is {volume} liters")

current_date = datetime.now()

with open("volumes.txt", "at") as file:
    print(f"{current_date:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume}", file=file)

price = None
if width == 185 and aspect_ratio == 50 and diameter == 14:
    price = 120
elif width == 205 and aspect_ratio == 60 and diameter == 15:
    price = 150
elif width == 225 and aspect_ratio == 55 and diameter == 16:
    price = 180
elif width == 245 and aspect_ratio == 45 and diameter == 17:
    price = 210

if price:
    print(f"Estimated price for this tire: ${price}")

buy = input("Do you want to buy tires with these dimensions? (yes/no): ").strip().lower()
if buy == "yes":
    phone = input("Enter your phone number: ").strip()
    # Append phone number to volumes.txt
    with open("volumes.txt", "at") as file:
        print(f"Customer phone number: {phone}", file=file)
    print("Thank you! Your order has been recorded.")