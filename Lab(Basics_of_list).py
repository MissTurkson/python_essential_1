#There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.

#Your task is to:

#write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (Step 1)
#write a line of code that removes the last element from the list (Step 2)
#write a line of code that prints the length of the existing list (Step 3).
#Ready for this challenge?  -Yes, Let us get started

hat_list = [1,2,3,4,5]  #existing numbers in the hat
print("The list in the hat is: ", hat_list)

promptUser = int(input("Replace the middle number with an integer of your choice: "))
hat_list[2] = promptUser
print("The new list with the replaced integer: " , hat_list)

#remvoing last element from list
del hat_list[-1]
print(hat_list)

print("The length of the new list is:" , len(hat_list))