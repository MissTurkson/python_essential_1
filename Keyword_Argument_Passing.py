def introduction(firstName , lastName):
    print("My name is " , firstName, lastName)

introduction(firstName="Esi" , lastName="Kuma")
introduction(lastName="Mbroh" , firstName="Jovita")

#In the passing of argument the parameter name should be the same as the arguement name

#Mixing positional argument and Keyword Arguement
#The rule is that postional arguement must come before keyword argument

def adding(a , b, c):
    print(a, "+" , b , "+" , c, "=" , a+b+c)
adding(1,2,3)

#this here is a pure positional argument oriented code
adding(c = 2, a= 1 , b=3)
adding(3 , b=1, c=2)