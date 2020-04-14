# A program to group all 1's and 0's zeroes separately
# Also, calculates minimum number of 0's to be eliminated 

n = int(input("Enter the number of 100's to be printed: "))
input_values = "100" * n
print("These are the input values: " + input_values)
filtered_values = input_values.replace("0","*",-1)
print("These are the filtered values: " + str(filtered_values))
occurences = input_values.count("0",0,3)
print("The minimum number of zero(es) that need to be erased is " + str(occurences))