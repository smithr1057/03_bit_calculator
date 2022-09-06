<<<<<<< HEAD
from time import sleep


def num_check(question):
    # Check that users enter a number that is more than zero
    valid = False
    while not valid:

        error = "please enter a integer that is more than zero"

        try:
        
            # Ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print(error)
            print()
keep_going = ""
while keep_going == "":

    integer = num_check("Integer: ")
    print()

    # Slow it down a bit
    sleep(1.25)

    keep_going = input("Press <enter> to keep going or any other key to quit ")
=======
from time import sleep


def num_check(question):
    # Check that users enter a number that is more than zero
    valid = False
    while not valid:

        error = "please enter a integer that is more than zero"

        try:
        
            # Ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
                return response

            # outputs error if input is invalid
            else: 
                print(error)
                print()

        except ValueError:
            print(error)
            print()
keep_going = ""
while keep_going == "":

    integer = num_check("Ineger: ")
    print()

    # Slow it down a bit
    sleep(1.25)

    keep_going = input("Press <enter> to keep going or any other key to quit ")
>>>>>>> 6354200279cd545add6dac43f214f8465e999ba6
    print()