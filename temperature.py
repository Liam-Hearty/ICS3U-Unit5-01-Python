#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: October 2019
# This program changes degrees celcius to farenheit.


def calculate_f():
    try:
        temp_c = int(input("Enter a temperature in degrees celcius: "))
        temp_f = (9/5) * temp_c + 32
        print("The temperature of {0}c is equal to {1}f".format(temp_c,
              temp_f))
    except ValueError:
        print("That was not a valid number.")


def main():
    # This function calls other functions
    calculate_f()


if __name__ == "__main__":
    main()
