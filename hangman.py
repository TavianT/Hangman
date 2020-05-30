#Hangman by Tavian Taylor
import random
words = ["unpopular","gargantuan", "dragon","saline","serendipity","aglet","nauseant","kidding","mississippi"]

def chooseWord():
    randomWord = random.randint(0,len(words) - 1)
    return words[randomWord]
def toUnderscores(word):
    wordLength = len(word)
    hangString = ""
    # for x in range (wordLength):
    hangString = '_' * wordLength
    return hangString


word = chooseWord()
emptyWord = toUnderscores(word)
print("Welcome to hangman!")
