# Functions go here

# Puts series of symbols at star and end of text (for emphasis)
def statement_generator(text, decoration):

    # Make string with five characters 
    ends = decoration * 5

    # add decoration to start and end of statement 
    statement = "{} {} {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# checks user choice is 'integer', 'text' or 'image'
def user_choice():

    valid = False
    while not valid:
        
        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()

        # if they choose "t" or "text" or "txt", return "text"
        text_ok = ["text", "t", "txt"]
        if response in text_ok:
            return "text"

         # if they choose "int" or "interger", return "interger"
        int_ok = ["int", "integer"]
        if response in int_ok:
            return "integer"

         # if they choose "image" or "p" or "img", return "image"
        img_ok = ["image", "p", "img"]
        if response in img_ok:
            return "image"

        # if they choose "i" ask whether they want interger or image
        elif response == "i":
            want_integer = input("Press <enter> for integer or any other key for image: ")
            if want_integer == "":
                return "integer"
            else:
                return "image"

        else: 
            print("Please choose a valid file type!")

            print()


# checks input is a number more than a given value
def num_check(question, low):
    valid = False
    while not valid:

        error = "please enter a integer that is more than (or equal to) {}".format(low)

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


# calculates the # of bits for text (# of characters x 8)
def text_bits():

    print()
    # ask user for a string...
    text = input("Enter some text: ")

    # calculate # of bits (length of string x 8)
    var_length = len(text)
    num_bits = 8 * var_length

    # output answer with working 
    print()
    print("\'{}\' has {} characters ...".format(text, var_length))
    print("# of bits is {} x 8...".format(var_length))
    print("We need {} bits to represent {}".format(num_bits, var_length))
    print()

    return ""



# Main Routine goes here

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Display instructions if user has not used the progra before

# Loop to allow multiple calulations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)
    
    # For integers, ask for integer
        # (must be an integer more than / equal to 0)
    if data_type =="integer":
        integer = num_check("Enter an integer: ", 0)
    
    # For images, ask for width and height
    # (must be integers more than / equal to 1)
    elif data_type =="image":
        image_width = num_check("Image width? ", 1)
        print()
        image_height = num_check("Image height? ", 1)

    # For text, ask for a string
    else:
        text = input("Enter some text: ")
