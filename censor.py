def censor_string():
    censor_text = str(input("Enter the text: "))
    censor_word = str(input("Enter the censor word: "))
    censor_character = str(input("Enter the censor character: "))
    censor_list_length = len(censor_word)
    print("This is the text you entered: " , "\n" , censor_text)
    censor_string = (censor_text , censor_word , censor_character)
    trim = len(censor_string[1]) * censor_string[2]
    censored_string = censor_string[0].replace(censor_word,trim)
    print("This is the censored string: " , "\n" , censored_string)

censor_string()
