# Checks user coice is 'integer', 'text' or 'image'
def user_choice():

    valid = False
    while not valid:
        
        response = input("File type (integer / text / image): ").lower()

        if response == "text" or response == "t":
            return "text"

        else: 
            print("Please choose a valid file type!")
            print()



# Main routine goes here 
data_type = user_choice()
print("you chose", data_type)

print()