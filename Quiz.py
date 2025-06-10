#write a program that prints the sum of all numbers from 1 to a number provided by the user that is divisble by
# a) 3 and 5  b) 3 or 5  c) 2 and 5 or 5 d) 2 and 3 or 3 and 5


# Program to compute specific sums based on divisibility
# retrieving user input
usernumber = int(input("Enter any number: "))

suma = 0
sumb = 0
sumc = 0
sumd = 0



for i in range(1, usernumber+1):
    if (i % 3 == 0 and i % 5 == 0):
        suma = suma + i

    if (i % 3 == 0 or i % 5 == 0):
        sumb = sumb + i

    if ((i % 2 == 0 and i % 5 == 0) or i % 5 == 0):
        sumc = sumc + i

    if (i % 2 == 0 and i % 3 == 0) or (i % 3 == 0 and i % 5 == 0):
        sumd = sumd + i

print("Sum of numbers divisible by both 3 and 5:" , suma)
print("Sum of numbers divisible by both 3 or 5:" , sumb)
print("Sum of numbers divisible by both 2 and 5 or 5:" , sumc)
print("Sum of numbers divisible by both 2 and 5 or 3 and 5:" , sumd)









# Get user input
n = int(input("Enter a number: "))

# Initialize sums
sum_a = 0  # divisible by 3 and 5
sum_b = 0  # divisible by 3 or 5
sum_c = 0  # divisible by (2 and 5) or 5
sum_d = 0  # divisible by (2 and 3) or (3 and 5)

# Loop through all numbers from 1 to n
for i in range(1, n + 1):
    if i % 3 == 0 and i % 5 == 0:
        sum_a += i
    if i % 3 == 0 or i % 5 == 0:
        sum_b += i
    if (i % 2 == 0 and i % 5 == 0) or i % 5 == 0:
        sum_c += i
    if (i % 2 == 0 and i % 3 == 0) or (i % 3 == 0 and i % 5 == 0):
        sum_d += i

# Print results
print("Sum of numbers divisible by both 3 and 5:", sum_a)
print("Sum of numbers divisible by 3 or 5:", sum_b)
print("Sum of numbers divisible by (2 and 5) or 5:", sum_c)
print("Sum of numbers divisible by (2 and 3) or (3 and 5):", sum_d)
