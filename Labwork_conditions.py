#Spathiphyllum, more commonly known as a peace lily or white sail plant, is one of the most popular indoor houseplants that filters out harmful toxins from the air. Some of the toxins that it neutralizes include benzene, formaldehyde, and ammonia.

#Imagine that your computer program loves these plants. Whenever it receives an input in the form of the word Spathiphyllum, it involuntarily shouts to the console the following string: "Spathiphyllum is the best plant ever!"

#prints the sentence "Yes - Spathiphyllum is the best
#plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
#prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
#prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.
#Test your code using the data we've provided for you. And get yourself a Spathiphyllum, too!

inputflower = input("What is the name of your favorite flower: ")
flower_name = "Spathiphyllum"
if inputflower == flower_name:
    print("Yes - Spathiphyllum is the best plant ever")
elif inputflower == flower_name.upper():
    print("No, I want a big Spathiphyllum")
elif inputflower == flower_name.lower():
    print("Spathiphyllum! Not" , inputflower, end="!")
elif inputflower != flower_name:
    print("Spathiphyllum! Not", inputflower, end="!")












