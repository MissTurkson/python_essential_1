# Store the current largest number here.
#largest_number = -999999999

# Input the first value.
#number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
#while number != -1:
    # Is number larger than largest_number?
    #if number > largest_number:
        # Yes, update largest_number.
       # largest_number = number
    # Input the next number.
    #number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
#print("The largest number is:", largest_number)





largest_number = -999999999
number = int(input("Enter a number or key in -1  to exit:  "))
# if number is not equal to -1 continue
while number != -1:
    #creating the condition
    if number > largest_number:
        #giving it a new largest number depending on the value inputed
        largest_number = number
    number = int(input("Enter a number: "))
print("The largest number is " , number)