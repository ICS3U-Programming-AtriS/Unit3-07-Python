#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: March 31, 2025
# Grandparents will only approve of a person dating their grandchild
# if they are older than 25 AND younger than 40.
# This program takes an age from the user
# and then tells the user whether they can date the grandchild or not.

import constants


def main():
    # Get the user's age as a string
    age_as_string = input("Enter your age: ")

    try:
        # Convert the user's age to an integer
        age = int(age_as_string)

        # Check if user is older than 25 AND younger than 40
        if (age > constants.MIN_APPROVED_AGE) and (age < constants.MAX_APPROVED_AGE):
            # Tell the user that they are approved
            print("You are approved of dating our grandchild.")
        # Check if user has a negative age OR an age that's too much for a human
        elif (age < constants.MIN_VALID_AGE) or (age > constants.MAX_VALID_AGE):
            # Tell the user that their age was invalid
            print("Please enter a valid age.")
        else:
            # Tell the user that they are denied
            print("You cannot date our grandchild!")
            print("You must be older than 25 and younger than 40.")
    except ValueError:
        # Tell the user that their input wasn't an integer
        print(f"{age_as_string} is not an integer.")
    finally:
        # Program completion message
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
