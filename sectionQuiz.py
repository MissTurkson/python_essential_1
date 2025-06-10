#finding odd numbers

for i in range(1, 11):
    if i % 2 == 1:
       print(i)
print("These are the odd numbers following the parameters")

#Create a while loop that counts from 0 to 10, and prints odd numbers to the screen. Use the skeleton below:


x = 1
while x < 11:
    if x % 2 == 1:
        print(x)
    x+=1

#Create a program with a for loop and a break statement. The program should iterate over characters in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line. Use the skeleton below:

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print (ch , end = "")

#Create a program with a for loop and a continue statement. The program should iterate over a string of digits, replace each 0 with x, and print the modified string to the screen. Use the skeleton below:

for digit in "0165031806510":
    if digit == "0":
        print ("x", end="")
        continue
    print(digit , end= "")