def message(number):
    print("Enter a number:" , number)
number = 1234
message(1)
print(number)
#note that this mechanism is called shadowing


#parameterised fuctions in details
def introduction(firstname , lastname = "Smith"):
    print("My name is" , firstname , lastname)
introduction("James" , "Brown")
introduction("Henry")
introduction(firstname="Esi")

def introduction(firstname = "John" , lastname = "Smith"):
    print("Hello, my name is" , firstname, lastname)
introduction()