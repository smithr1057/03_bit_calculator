# checks input is a number more than a given value
def num_check(question, low):
    valid = False
    while not valid:

        error = "please enter a integer that is more than "
        "(or equal to) {}".format(low)

        try:
        
            # Ask user to enter a number
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
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

    keep_going = input("Press <enter> to keep going or any other key to quit ")