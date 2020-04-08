def grade_classifier(score, total):
    if not (total == 0):
        percentage = score / total * 100
        if percentage >= 90:
            return "You have an A and your percentage is " + str(percentage)
        elif percentage >= 80:
            return "You have an B and your percentage is " + str(percentage)
        elif percentage >= 70:
            return "You have an C and your percentage is " + str(percentage)
        elif percentage >= 60:
            return "You have an D and your percentage is " + str(percentage)
        elif percentage < 60:
            return "You have a F and your percentage is " + str(percentage)
    else:
        return "Invalid inputs"

#look a edit with vscode

Score = int(input("Enter your score: "))
Total = int(input("Enter the total: "))
print(grade_classifier(Score, Total))
