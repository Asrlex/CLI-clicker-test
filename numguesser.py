import random

print("Guess the number!!")
min = int(input("Minimum: "))
max = int(input("Maximum: "))
number = random.randint(min, max)
close_range = int((max-min)/100*20)
closest_range = int((max-min)/100*5)
guesses = 0

while True:
    print("\nGuess")
    guess = int(input(" > "))
    guesses+=1
    if guess > max or guess < min:
        print("Dude can you read?")
        continue
    elif guess == number:
        print("Correct!!!")
        break
    elif guess < number:
        if guess < (number - close_range):
            print("That's waaaay too low")
        elif guess > (number + close_range):
            print("Almost! Just a little higher.")
        else:
            print("Too low...")
    elif guess > number:
        if guess > (number + close_range):
            print("That's waaaay too high")
        elif guess < (number + close_range):
            print("Almost! Just a little lower.")
        else:
            print("Too high...")

print(f"Congratulations!! You guessed it in {guesses} guesses.")
