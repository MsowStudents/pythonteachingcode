def str_analysis(text):

    if text.isdigit():
        num = int(text)

        if num > 99:
            return text + " is a pretty big number"
        else:
            return text + " is a smaller number than expected"

    elif text.isalpha():
        return '"' + text + '"' + " is all alphabetical characters!"

    else:
        return "multiple character types"


#  input until not empty
user_input = ""

while user_input == "":
    user_input = input("Moussa Sow, enter word or integer: ")

# call function
result = str_analysis(user_input)

print(result)