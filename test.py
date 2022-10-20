def drawFigure(lives):
    print("______")
    print("|     |")
    print("|     ", end="")
    if lives > 0:
        print("O")
    else:
        print("")
        
    print("|    ", end="")
    if lives > 1:
        print("/", end="")
    else:
        print(" ", end="")
    if lives > 2:
        print("|", end="")
    else:
        print(" ", end="")
    if lives > 3:
        print("\\")
    else:
        print("")
        
    print("|     ", end="")
    if lives > 4:
        print("|")
    else:
        print("")
    
    print("|    ", end="")
    if lives > 5:
        print("/ ", end="")
    else:
        print(" ", end="")
    if lives > 6:
        print("\\")
    else:
        print("")
    
    print("|  ", end="")
    if lives > 7:
        print("|¬¬¬¬¬|")
    else:
        print("")
    print("|__________")