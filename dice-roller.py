import random
score = 0
def main():
    print("Rolling Dice !")
    print(" ")

    

    doMoreRolls = True

    while doMoreRolls == True:

        playerChoice = input("Do you want to roll again ? Y/N : ")

        if (playerChoice == "Y" or playerChoice == "y" or
            playerChoice == "Yes" or playerChoice == "yes" or
            playerChoice == "YES"):
            rollDice()
            

        else:
            doMoreRolls = False
            endRollingDiceProgram()


def rollDice():
    if score < 55:
        diceRollValue = random.randrange(1, 7)
        displayDicePicture(diceRollValue)
        print('You rolled a ' + str(diceRollValue))
        print(' ')
        print('Your score is ' + str(score))
    else:
        print('You Have Won!')
def endRollingDiceProgram():
        print(" ")
        input("Press Any Key to Exit ")
        quit()

def displayDicePicture(diceRollValue):
    global score
    if diceRollValue == 1:
        print(' ')
        print(' ----- ')
        print('|     |')
        print('|  O  |')
        print('|     |')
        print(' ----- ')
        print(' ')
        score = score + 1
    
    elif diceRollValue == 2:
        print(' ')
        print(' ----- ')
        print('|    O|')
        print('|     |')
        print('|O    |')
        print(' ----- ')
        print(' ')
        score = score + 2
    
    elif diceRollValue == 3:
        print(' ')
        print(' ----- ')
        print('|O    |')
        print('|  O  |')
        print('|    O|')
        print(' ----- ')
        print(' ')
        score = score + 3
    
    elif diceRollValue == 4:
        print(' ')
        print(' ----- ')
        print('|O   O|')
        print('|     |')
        print('|O   O|')
        print(' ----- ')
        print(' ')
        score = score + 4
    
    elif diceRollValue == 5:
        print(' ')
        print(' ----- ')
        print('|O   O|')
        print('|  O  |')
        print('|O   O|')
        print(' ----- ')
        print(' ')
        score = score + 5
    
    else:
        print(' ')
        print(' ----- ')
        print('|O   O|')
        print('|O   O|')
        print('|O   O|')
        print(' ----- ')
        print(' ')
        score = score + 6
        

main()

endRollingDiceProgram()
