import string

def remove_punctuation():
    user_input = input("Enter a string: ")
    no_punctuation = user_input.translate(str.maketrans('', '', string.punctuation))
    print("String without punctuation:", no_punctuation)

remove_punctuation()