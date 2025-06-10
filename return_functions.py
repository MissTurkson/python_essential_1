#return without expression

def happy_new_year(wishes = True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return
    print("Happy new year!")
happy_new_year()

#return with an expression
def boringFunction():
    return 123
x = boringFunction()
print("The boring function has returned its result. It is" , x)


def boring_function():
    print("'Boredom mode', ON.")
    return 123
print("This lesson is interesting!")
boring_function()
print("This lesson is boring")

#A few word on None
#None is a keyowrd. Let us take a look at this 
value =  None 
if value is None:
    print("Sorry, you donot carry any value")

def strange_function(n):
    if(n%2 == 0):
        return True
print(strange_function(2))
print(strange_function(1))