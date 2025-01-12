import datetime
from datetime import timedelta

# Global variable for the current date
current_date = None

def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS
    """
    global current_date
    current_date = datetime.datetime.now()  # Get the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")  # Format it
    print(f"Current date and time: {formatted_date}")

def calculate_future_date(days_to_add):
    """
    Calculates and displays the future date after adding the specified number of days.
    """
    # Calculate the future date
    future_date = (current_date + timedelta(days=days_to_add)).date()
   formatted_future_date = future_date.strftime("%Y-%m-%d")  # Format the date
    print(f"Future date: {formatted_future_date}")

# Part 1: Display the current date and time
display_current_datetime()

# Part 2: Prompt the user for the number of days and calculate the future date
try:
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days_to_add)  # Pass days_to_add to the function
except ValueError:
    print("Error: Please enter a valid integer for the number of days.")
