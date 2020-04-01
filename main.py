import random

attempts = 6
counter = 0
win = False
letterChose = ""
guessedLetters = []
location = []
spacesList = []

########################### Def Functions ##############################

def newGame(newword):
    print("Lets give you a hint, the word contains " + str(len(newword)) + " letters")
    
    for i in newword:
        print("_ ", sep="", end="")
    
    print("""
--------
|      |
|
|
|
|
|
----------
""")

def printMistakes(count, attempt = 6):
    if count == 1:
        print("""
--------
|      |
|      O
|
|
|
|
----------
""")
        print("You still have" + str(attempt - count) + "tries")
    elif count == 2:
        print("""
--------
|      |
|      O
|     |
|
|
|
----------
""")
        print("You still have" + str(attempt - count) + "tries")
    elif count == 3:
        print("""
--------
|      |
|      O
|     | |
|
|
|
----------
""")
        print("You still have" + str(attempt - count) + "tries")
    elif count == 4:
        print("""
--------
|      |
|      O
|     | |
|      |
|
|
----------
""")
        print("You still have" + str(attempt - count) + "tries")
    elif count == 5:
        print("""
--------
|      |
|      O
|     | |
|      |
|     |
|
----------
""")
        print("You still have" + str(attempt - count) + "tries")
    elif count == 6:
        print("""
--------
|      |
|      O
|     | |
|      |
|     | |
|
----------
""")
        print("You lose!")

def letterLocation(word, char):
    pos = []
    for n in range(len(word)):
        if word[n] == char:
            pos.append(n)
    return pos

def guessed(spacesList, posletter, word):
    for i in range(len(posletter)):
        spacesList[posletter[i]] = word
    
    return spacesList

############################## Functions End ##########################
        
with open('sowpods.txt') as f:
    words = list(f)
    
the_word = random.choice(words).lower()
the_word = list(the_word)
del the_word[-1]
print("Welcome to ** HangMan Game **")
print()
print("Try to guess the word with 6 attempts you have!!")

# create the space list for total letters for the randomly word
for i in range(len(the_word)):
        spacesList.append("_ ")

newGame(the_word)

while counter != 6 and win == False:
    guess_word = input("Enter the letter.. ")
    letterChose += guess_word
    if guess_word.lower() in the_word:
        print()
        print("Correct! let's try to guess another letter\n")
        guessedLetters.append(guess_word)
        location = letterLocation(the_word, guess_word) # return list location letter
        
        print(guessed(spacesList, location, guess_word))

    elif guess_word not in the_word:
        counter += 1
        printMistakes(counter,)
        
        print("Letter chosen: ", end="")
        for i in letterChose:
            print(i + ",", end="")
