#Hangman by Tavian Taylor
import random
words = ["unpopular","gargantuan", "dragon","saline","serendipity","aglet","nauseant","kidding","mississippi"]
gameOver = False
def chooseWord():
    randomWord = random.randint(0,len(words) - 1)
    return words[randomWord]
def toUnderscores(word):
    wordLength = len(word)
    hangString = ""
    # for x in range (wordLength):
    hangString = '_' * wordLength
    return hangString
def getInput():
    guess = input("Enter a guess: ")
    if checkGuessValid(guess):
        return guess
def checkGuessValid(guess):
    if len(guess) > 1:
        print("invalid input")
        return False
    else:
        return True
def checkForAnswer(word,guess,emptyWord):
    newEmptyWord = ""
    for i in range(len(word)):
        if guess == word[i]:
            newEmptyWord = emptyWord[:i] + guess + emptyWord[i+1:]
            
    print(newEmptyWord) #CONVERT STRING TO LIST         
                    
word = chooseWord()
emptyWord = toUnderscores(word)
print("Welcome to hangman!")
while not gameOver:
    guess = getInput()
    checkForAnswer(word,guess,emptyWord)

