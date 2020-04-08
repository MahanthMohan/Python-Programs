def censor_string():
    censor_text = str(input("Enter the text: "))
    censor_word = str(input("Enter the censor(s), spaced out using comma(s): "))
    censor_character = str(input("Enter a censor character: "))
    splitted_censor = censor_word.split(",")
    censor_list_length = len(splitted_censor)
    print("This is the text you entered: " , "\n" , censor_text)
    for i in range (0,censor_list_length):
        i = i
        censor_string = (censor_text , splitted_censor[i] , censor_character)
        trim = 0
        trim = len(censor_string[i]) * censor_string[2]
        censored_string = censor_string[0].replace(splitted_censor[i],trim)
        print("This is the censored string: " , "\n" , censored_string)

censor_string()
