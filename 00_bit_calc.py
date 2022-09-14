from time import sleep
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


# displays instructions / information
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("Please choose a data type (image / text / integer)")
    print()
    print("This program asumes that images are being represented in 24 bit colour (ie: 24 bits per pixel). For text, we asume that ascii encoding is being used (8 bits per character).")
    print()
    print("Complete as many calculaations as necessary, pressing <enter> at the end of each calculation or any key to quit.")
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
    print("We need {} bits to represent {}".format(num_bits, text))
    print()

    return ""


# finds # of bits for 24 bit colour 
def image_bits():
    
    # ask user for image width and height
    print()
    image_width = num_check("Image width: ", 1)
    image_height = num_check("Image height: ", 1)
    print()

    # calculate # pixels and # bits
    num_pixels = (image_width * image_height)
    num_bits = (num_pixels * 24)


    # output # pixels and # bits
    print("# of pixels = {} x {} = {}".format(image_height, image_width, num_pixels))
    sleep(.5)
    print()
    print("# bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()

    return ""


# converts decimal to binary and state how 
# many bits are needed to represent the original integer
def int_bits():

    # Get integer (must be >= 0)
    var_integer = num_check("Please enter an integer: ", 0)

    # Source for code below is
    # https://stackoverflow.com/questions/699866/python-int-to-binary-string

    var_binary = "{0:b}".format(var_integer)

    # calculate # of bits (length of string above)
    num_bits = len(var_binary)

    # output answer with working
    print()
    print("{} in binary is {}".format(var_integer, var_binary))
    print("# of bits is {}".format(num_bits))
    print()

    return ""


# Main Routine goes here

# Heading
statement_generator("Bit Calculator for Integers, Text & Images", "-")

# Display instructions if user has not used the progra before
first_time = input("Press <enter> to see the instructions or any key to continue ")

if first_time == "":
    instructions()
# Loop to allow multiple calulations per session
keep_going = ""
while keep_going == "":

    # Ask the user for the file type
    data_type = user_choice()
    print("You chose", data_type)
    
    # For integers, ask for integer
        # (must be an integer more than / equal to 0)
    if data_type =="integer":
        int_bits()
    
    # For images, ask for width and height
    # (must be integers more than / equal to 1)
    elif data_type =="image":
        image_bits()

    # For text, ask for a string
    else:
        text_bits()

    print()
    keep_going = input("Press <enter> to continue or any key to quit ")
    print()