numbers = [10,5,7,2,1]
print("Original list content: " , numbers) #Printing original list contents

numbers[0] = 111
print("\n Previous list contents: " , numbers)  #printing previous list cntents

numbers[1] = numbers[4] # Copying value of the fifth element to the second.
print("New List contents: ", numbers)  #printing current list contents

print("\n List length is: " , len(numbers))

#Accessing List CONTENTS
print(numbers[0])


#Removing list contents
del numbers[1]  # the number 5 will be deleted
print(len(numbers))
print(numbers)

#you can't access an element which doesnot exist


#Negative indexing
#negative indices are legal and can be very useful
numbers = [111, 7, 2, 1]
print(numbers[-1])


#Adding elements to a list
#we can use the insert() or the append()

#.append() function
numbers.append(4)
print(len(numbers))
print(numbers)


#.insert() function
numbers.insert(0 , 222)
print(len(numbers))
print(numbers)

numbers.insert(1, 333)
print(numbers)
