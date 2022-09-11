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

# Main routine goes here
text_bits()