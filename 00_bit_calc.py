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
            return "interger"

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

    # For images, ask for width and height 