print("hello World") 


lax = 2 + 2
print("this shows addition")
print(lax)
print("\n")

bball = 4 - 2
print("this shows subtraction")
print(bball)
print("\n")

soccer = 4 * 2
print(soccer)
football = 4 / 2
print(football)
hockey = 4 // 2
print(hockey)

tennis = 4 % 2
print(tennis)

def print_lyrics():
    print("She said do you love me")
    print("I said only partly I only love my bed and my momma I'm sorry")

print_lyrics()

def return_lyrics():
    lyrics = "She said do you love me"
    lyrics += """ I said only partly I
               only love my bed and my momma I'm sorry."""
    return lyrics
godsplanSong = return_lyrics()

numb = 1
if numb == 1:
    print("one")
elif numb == 2:
    print("two")
else:
    print("bigger number")

i = 0
while i < 5:
    print('hello')
    i += 1

i = 0
j = 0
while i < 5:
    while j < 5:
        print(j, end='')
        j += 1
    print('\n###############')
    j = 0
    i += 1
fruits = ['apple', 'orange', 'banana', 'grape']
firstFruits = fruits[0]
twoFruits = fruits[1:3]
favFoods = {'cheese': 'camembert', 'meat':
            'beef', 'vegetables': 'carrot',
            'desert': 'pie',
            'meat product': 'spam'}
# str.find()

string = "catch my catatonic cat."
subString = "cat"
stringIndex = string.find(subString)
print(stringIndex)

# str.lower()
crazyString = "I will be easy to catch my catatonic cat"
stringIndex = crazyString.find(subString)
print(stringIndex)

stringIndex = crazyString.lower().find(subString)
print(stringIndex)

 # str.split()

someValues = "Laconia Gilford Belmont"
listOfValues = someValues.split()
print(listOfValues[1])
#here is a more complex example
keyValuePairs = "Bill: Laconia, Jane: Gilford, Tom: Belmont"
listOfPairs = keyValuePairs.split(", ")
count = 0
while count < len(listOfPairs):
    fname, town = listOfPairs[count].split(": ")
    print("first name is: " + fname + "\n town is: " + town)
    count += 1
