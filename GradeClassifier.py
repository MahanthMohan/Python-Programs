def gradeClassifier(Score,Total):
    if not(Total == 0):
        Percentage = Score/Total*100
        if Percentage>=90:
            return("You have an A and your percentage is {}".format(Percentage))
        elif Percentage>=80:
            return("You have a B and your percentage is {}".format(Percentage))    
        elif Percentage>=70:
            return("You have a C and your percentage is {}".format(Percentage))
        elif Percentage>=60:
            return("You have a D and your percentage is {}".format(Percentage))
        elif Percentage<60:
            return("You have a F and your percentage is ", Percentage, " Failure is the stepping stone to success")
    else:
        return("Invalid inputs")

Score = int(input("Enter your score: "))
Total = int(input("Enter the total: "))
print (gradeClassifier(Score,Total))