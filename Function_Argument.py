def myFunction(n):
    print("I got" , n)
    n += 1
    print("I have" , n)
var = 1
myFunction(var)
print(var)

def my_function(my_list_1):
    print("Print #1: ", my_list_1)
    print("Print #2: ", my_list_2)
    my_list_1 = [0, 1]
    print("Print #3: ", my_list_1)
    print("Print #4: " , my_list_2)
my_list_2 = [2,3]
my_function(my_list_2)
print("Print #5: ", my_list_2)

def bmi(weight, height):
    return weight/height ** 2
print(bmi (52.5 , 1.65))

def bmi(weight, height):
    if height < 1.0 or height > 2.5 or\
    weight <20 or weight > 200:
        return None
    return weight/height ** 2
print(bmi(352.5 , 1.65))

def lb_to_kg(lb):
    return lb * 0.45359237
print(lb_to_kg(1))

def ft_and_inch_to_m(ft, inch):
    return ft *0.3048 + inch * 0.0254
print(ft_and_inch_to_m(1,1))
print(ft_and_inch_to_m(6,0))


def ft_and_inch_to_m(ft, inch=0.0):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(6))


