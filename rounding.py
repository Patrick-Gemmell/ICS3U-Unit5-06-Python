#!/usr/bin/env python3

# Created by: Patrick Gemmell
# Created on: november 2019
# This show two functions

import math


def round_decimal(some_variable, place_user_int):
    # process
    some_variable[0] = (some_variable[0]*(10**place_user_int))+0.5
    some_variable[0] = int(some_variable[0])
    some_variable[0] = float(some_variable[0])
    some_variable[0] = some_variable[0]/(10**place_user_int)


def main():
    # calling functions and inputs
    while True:
        some_variable = []

        float_user_string = input("Enter a decimal: (float) ")
        place_user_string = input("Enter the decimal place: ")

        try:
            float_user_float = float(float_user_string)
            place_user_int = int(place_user_string)

            some_variable.append(float_user_float)

            round_decimal(some_variable, place_user_int)

            print("The decimal rounded {0}".format(some_variable[0]))
            break
        except Exception:
            print("that is an invalid integer")


if __name__ == "__main__":
    main()
