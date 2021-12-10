#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Dec 2021
# this program tells about sqaures


def main():
    # this is a function for finding sqaures

    # Input
    enter_num = input("Enter an integer >= 0 : ")

    # Process & Output
    try:
        enter_num = int(enter_num)
        if (enter_num < 0):
            print("Number must be positive")
        else:
            for counter in range(enter_num+ 1):
                print("{}² = {}".format(counter, counter ** 2))

    except ValueError:
        print("You did not not an integer")
        
    print("\nDone.")

if __name__ == "__main__":
    main()