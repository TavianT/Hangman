#Hangman by Tavian Taylor
import random
import sys
words = ["unpopular","gargantuan", "dragon","saline","serendipity","aglet","nauseant","kidding","mississippi"]
gameOver = False
totalGuesses = 7
def chooseWord():
    randomWord = random.randint(0,len(words) - 1)
    word = words[randomWord]
    wordAsList = []
    for i in range (len(word)):
        wordAsList.append(word[i])
    return wordAsList

def toUnderscores(word):
    emptyWordList = []
    for i in range(len(word)):
        emptyWordList.append('_')
    return emptyWordList

def getInput():
    guess = input("Enter a guess: ")
    return guess
def printWord(emptyWord):
    print(*emptyWord)
def checkForAnswer(word,guess,emptyWord,totalGuesses):
    correctGuess = False
    if len(guess) == 1:
        for i in range(len(word)):
            if guess == word[i]:
                emptyWord[i] = guess
                correctGuess = True
        if correctGuess == False:
            totalGuesses = decrementGuesses(totalGuesses)
        
    else:
        wordAsString = convertToString(word)
        if guess == wordAsString:
            gameWon(totalGuesses)
        else:
            totalGuesses = decrementGuesses(totalGuesses)
    return emptyWord,totalGuesses
        
def convertToString(word):
    newWord = ""
    for i in range(len(word)):
        newWord = newWord + word[i]
    return newWord
def gameWon(totalGuesses):
    print("WINNER WINNER CHICKEN DINNER")
    print("You won with " + str(totalGuesses) + " guesses to spare")
    sys.exit()
def decrementGuesses(totalGuesses):
    totalGuesses = totalGuesses - 1
    return totalGuesses  
def gameOverCheck(totalGuesses):
    if totalGuesses == 0:
        return True
    else:
        return False
def gameLost():
    print("GAME OVER!!!")
    print("Better luck next time!")                    
word = chooseWord()
emptyWord = toUnderscores(word)
print(word)
print("Welcome to hangman!")
while not gameOver:
    printWord(emptyWord)
    print("Remaing guesses: " + str(totalGuesses))
    guess = getInput()
    emptyWord,totalGuesses = checkForAnswer(word,guess,emptyWord,totalGuesses)
    gameOver = gameOverCheck(totalGuesses)
gameLost()