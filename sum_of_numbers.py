#!/usr/bin/env python3
# Created by: Xiaohan
# Created on: Apr 3, 2025
# This program adds all whole numbers from 0 up to the number entered by the user.


def main():
    # Ask the user to enter a number
    user_input = input("Enter a positive integer: ")

    try:
        # Try converting the user input into an integer
        number = int(user_input)

        # Check if the number is positive
        if number < 0:
            print("Please enter a positive number.")
        else:
            # Initialize variables for total and counter
            total = 0
            counter = 0

            # Use a while loop to calculate the sum
            while number >= counter:
                total = total + counter
                counter = counter + 1

            # Display the result
            print("The sum of all whole numbers from 0 to", number, "is", total)
    except Exception:
        # If the input can't be converted to int, show error
        print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    main()
