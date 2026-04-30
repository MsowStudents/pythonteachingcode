def words_after_g():
    sentence = input("Welcome, Moussa Sow. Enter a 1 sentence quote, non-alpha separate words: ")
    word = ""
    for char in sentence:
        if char.isalpha():
            word += char
        else:
            if word != "":
                if word[0].lower() >= "h":
                    print(word.upper())
                word = ""
    # handle last word
    if word != "":
        if word[0].lower() >= "h":
            print(word.upper())
# call the function
words_after_g()