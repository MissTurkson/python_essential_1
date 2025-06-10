#As you surely know, due to some astronomical reasons, years may be leap or common. The former are 366 days long, while the latter are 365 days long.
#Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:

#if the year number isn't divisible by four, it's a common year;
#otherwise, if the year number isn't divisible by 100, it's a leap year;
#otherwise, if the year number isn't divisible by 400, it's a common year;
#otherwise, it's a leap year.
#Look at the code in the editor – it only reads a year number, and needs to be completed with the instructions implementing the test we've just described.
#The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
#It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: Not within the Gregorian calendar period. Tip: use the != and % operators.

number_year = int(input("Type a year of your choice here: "))
if number_year < 1582:
    print("Type a year which is within the Georgian Calender Period")

if number_year >= 1582:
    if number_year % 4 != 0:
        print(number_year, "is a common year")

    elif number_year % 100 != 0:
        print(number_year , "is a leap year")

    elif number_year % 400 != 0:
        print(number_year , "is a common year")

    else: print("It's a leap year")





