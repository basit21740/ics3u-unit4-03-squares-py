#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Dec 2021
# this progra do For Loops


def main():
    # this is a function for creating for loop program

    # asking for input
    num = input("Please enter a number: ")
    num = int(num)

    # process/output
    for i in range(num + 1):
        print(f"{i}² = {i*i}")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
