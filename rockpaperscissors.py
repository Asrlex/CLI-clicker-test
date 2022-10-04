from getpass import getpass as inputg
msg = " rock, paper or scissors: "
name1 = "\033[32m" + input("\033[32mPlayer 1\033[0m, tell me your name: ") + "\033[0m"
name2 = "\033[31m" + input("\033[31mPlayer 2\033[0m, tell me your name: ") + "\033[0m"
score1 = 0
score2 = 0
round = 0

print("Let's start the game!")
while score1 < 3 and score2 < 3:
    round+=1
    print(f"\nROUND {round}")
    play1 = inputg(f"{name1} {msg}")
    play2 = inputg(f"{name2} {msg}")
    print(f"{name1}: {play1}")
    print(f"{name2}: {play2}")
    if play1 == play2:
        print("Tie. No points.")
    elif(play1 == "scissors" and play2 == "paper") or (play1 == "paper" and play2 == "rock") or (play1 == "rock" and play2 == "scissors"):
        print(f"Point for {name1}!!")
        score1 += 1
    else:
        print(f"Point for {name2}!!")
        score2 += 1

if score1 == 3:
    print(f"{name1} won!!")
else:
    print(f"{name2} won!!")

