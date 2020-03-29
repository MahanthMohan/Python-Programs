
n = int(input("Enter the number of sides, (n>=3): "))

command = input("What do you want to calculate - interior/exterior angle or interior/exterior angle sum?: ")

if(command == "interior angle"):
    int_angle_measure = str((180*(n-2))/n)
    print("Each interior angle of the " + str(n) + " sided polygon is " + int_angle_measure)

elif(command == "interior angle sum"):
    int_angle_sum_measure = str(180*(n-2))
    print("The sum of all interior angles of the " + str(n) + " sided polygon is " + int_angle_sum_measure)

elif(command == "exterior angle"):
    ext_angle_measure = str(360-(180*(n-2)/n))
    print("Each exterior angle of the " + str(n) + " sided polygon is " + ext_angle_measure)

elif(command == "exterior angle sum"):
    ext_angle_measure = str(n * (360-(180*(n-2)/n)))
    print("The sum of all interior angles of the " + str(n) + " sided polygon is " + ext_angle_measure)
