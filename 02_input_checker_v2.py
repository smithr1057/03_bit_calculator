# Checks user coice is 'integer', 'text' or 'image'
def user_choice():

    valid = False
    while not valid:
        
        # ask user for choice and change response to lowercase
        response = input("File type (integer / text / image): ").lower()

        # if they choose "t" or "text", return "text"
        text_ok = ["text", "t", "txt"]
        if response in text_ok:
            return "text"

        else: 
            print("Please choose a valid file type!")
            print()



# Main routine goes here 
keep_going = ""
while keep_going == "":
    data_type = user_choice()
    print("you chose", data_type)

    print()