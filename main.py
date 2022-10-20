import random
import test

def clearLine():
    print ("\033[A\033[A")

def drawFigure(lives):
    test.drawFigure(lives)

def displayWord(word, guesses):
    print("\n")
    for letter in word:
        if letter in guesses:
            print(f"{letter}", end="")
        else:
            print("_", end="")
    print("\n")


listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]
word = random.choice(listOfWords)

print("🌟Hangman🌟\n")
lives = 8
guesses = []
won = False

while won == False and lives > 0:
    
    displayWord(word, guesses)

    choice = input("Letter or word: ")
    if choice.lower() in ["letter", "l"]:
        
        guess = input("Guess a letter: ")
        guesses.append(guess)
        if guess not in word:
            print("Nope, worng!")
            lives-=1
            print(f"You have {lives} lives left")
            drawFigure(lives)
            continue
        elif guess in word:
            count = word.count(guess)
            if count == 1:
                print("Great! There's one")
            else:
                print(f"Amazing! There are {count} {guess}'s!!")
            continue
    elif choice.lower() in ["word", "w"]:
        guess = input("Guess the whole word: ")
        if guess == word:
            if lives > len(word):
                print("Amazing!!! How did you do it??")
            else:
                print("Great! You got it!")
            won = True
        else:
            print("Tough luck, you got greedy...")
            lives-=3
            print(f"You have {lives} lives left")
            drawFigure(lives)

if won == True:
    print(f"Congratulations!! You won with {lives} lives left.")
else:
    print(f"Too bad, you lost... The word was {word}.")