import random

wordList = [
    'juniper',
    'cow',
    'horse',
    'pig',
    'rat',
    'zero',
    'rooster'
]

word = random.choice(wordList)
lettersGuessed = []
wrongGuessesLeft = 10

def guessedAllLettersInWord():
    # Look at each letter in the word and see if we haven't guessed it yet.
    for letter in word:
        if letter not in lettersGuessed:
            return False
    # We checked all the letters in word, and they were all in lettersGuessed
    return True

def printWordSoFar():
    charactersToPrint = []
    for letter in word:
        if letter in lettersGuessed:
            charactersToPrint.append(letter)
        else:
            charactersToPrint.append("_")
    combinedWord = " ".join(charactersToPrint)
    print(combinedWord)

print("Hangman!!")
while not guessedAllLettersInWord() and wrongGuessesLeft > 0:
    printWordSoFar()
    newGuess = input("Guess a letter: ")
    if newGuess in lettersGuessed:
        print("You already guessed that!")
    else:
        lettersGuessed.append(newGuess)
        if newGuess in word:
            print("That's right!")
        else:
            print("That letter isn't in the word.")
            wrongGuessesLeft =  wrongGuessesLeft - 1

if wrongGuessesLeft == 0:
    print("Sorry, you ran out of tries!")
else:
    print(f"Congratulations! You had {wrongGuessesLeft} wrong guesses left!")
