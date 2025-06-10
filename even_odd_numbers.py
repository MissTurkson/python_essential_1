#creating the even and odd variables
even_numbers = 0
odd_numbers = 0

#taking inputs
number = int(input("Enter a number or type 0 to stop: "))

#checking if the number is even
while number != 0:
    if number % 2 == 0:
        even_numbers += 1

    else:
         odd_numbers +=1
    number = int(input("Enter a numbe or type 0 to stop: "))

print("Even numbers counted are: "  , even_numbers)
print("Odd numbers counted are: " , odd_numbers)






