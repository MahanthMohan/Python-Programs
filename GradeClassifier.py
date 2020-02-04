def gradeClassifier(Score,Total):
    Percentage = Score/Total*100
    if Percentage>=90:
        print("You have an A and your percentage is {}".format(Percentage))
    elif Percentage>=80:
        print("You have a B and your percentage is {}".format(Percentage))    
    elif Percentage>=70:
        print("You have a C and your percentage is {}".format(Percentage))
    elif Percentage>=60:
        print("You have a D and your percentage is {}".format(Percentage))
    elif Percentage<60:
        print("You have a F and your percentage is {}".format(Percentage))            
        print("Failure is the stepping stone to success")

Score = int(input("Enter your score: "))
Total = int(input("Enter the total: "))
gradeClassifier(Score,Total)