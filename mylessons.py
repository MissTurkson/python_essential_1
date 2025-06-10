print("Hello World")
print("The itsy bitsy spider climbed the sprout again")
print()
print("Down came the rain and washed the spider out \n up came the sun and dried the rain away and the ity bitsy spider went up the sprout again")

#the sep=" "  keyword is used to seperate the string depending on the kind of seperation that you would like to do.
print("My name" , "is" , "Kwansema", "Sekyi" , sep="-")

print("orange" , "banana" , "pineapple" , "watermelon" , sep="," , end="mango " )

n = 40
print(n < 100)
print(n >=100)

#if_else_statement
#if weather_is_good:
  #  go_for_walk()
    #buy_sweets()
#else:
    #go_to_theatre()
    #eat_pringles()
#go_for_lunch()

#Analysing Code Samples
#declaration of variables
number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))

#determines the larger number
if number_1 > number_2:
    larger_number = number_1
else:
    larger_number = number_2
#print the result
print("The larger number is: ", larger_number)

# find the largest of three numbers.
number1 = int(input("Type the first number: "))
number2 = int(input("Type the second number: "))
number3 = int(input("Type the third number: "))

largest_number = number1
if number2 > largest_number:
    largest_number = number2
if number3 > largest_number:
    largest_number = number3
else:
    largest_number = number1
print("The largest Number of all the three values inputed is: ",  largest_number)

