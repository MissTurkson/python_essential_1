dictionary = {"cat" : "chat" , "dog" : "chien" , "horse" : "cheval"}
phone_number = {"boss" : "55566677788" , "suzzy": "5678953345"}
empty_dictionary = {}
print(dictionary)
print(phone_number)
print(empty_dictionary)

print(dictionary['cat'])
print(phone_number['Suzy'])

dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
words = ['cat', 'lion', 'horse']

for word in words:
    if word in dictionary:
        print(word, "->", dictionary[word])
    else:
        print(word, "is not in dictionary")