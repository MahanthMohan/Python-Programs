def censor_string():
    censor_text = str(input("Enter the text: "))
    censor_word = str(input("Enter the censor: "))
    censor_character = str(input("Enter a censor character: "))
    censor_string = (censor_text , [str(censor_word)," "], censor_character)
    print("This is the text you entered: " + "{}".format("\n") + censor_string[0])
    censor_length = len(censor_string[1][0])
    final_trim = censor_length * censor_string[2]
    censored_string = censor_string[0].replace(censor_word, final_trim)
    print("This is the censored string: " + "{}".format("\n") + censored_string)

censor_string()
