#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# this program prints all the numbers from 1000 - 2000 ending the line every 5 numbers


def main():
    loop_counter = 1000

    # process
    for loop_counter in range(1000, 2000 + 1):
        if loop_counter % 5 == 4:
            print("{0} ".format(loop_counter))
        else:
            print("{0} ".format(loop_counter), end ="")
    print("\nDone.")


if __name__ == "__main__":
    main()
