value = int(input("Enter a natural number: "))
print("The reciprocal of value is: " , value , " is" ,  1/value)


try:
    value = int(input("Key in a natural value: "))
    print("The reciprocal value is: " , value, "is" , 1/value)
except:
    print("I donot know what to do")

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except ValueError:
    print('I do not know what to do.')
except ZeroDivisionError:
    print('Division by zero is not allowed in our Universe.')


try:
    value = int(input("Enter any number of your choice: "))
    print(" The reciprocal of the" ,  value,  "is" , 1/value)
except ValueError:
    print(" I donot know what to do")
except ZeroDivisionError:
    print("Our universe does not accept this division.")
except:
    print("Something strange is about ot happen here .....  sorry")


temperature = float(input('Enter current temperature:'))

if temperature > 0:
    print("Above zero")
elif temperature < 0:
    print("Below zero")
else:
    print("Zero")