'''
http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
Rock Paper Scissors Game

Rock > Scissors
Scissors > Paper
Paper > Rock
'''
import random

playAgain = 1
while playAgain == 1:

    #Ask for user input
    userInput = input("Choose rock, paper or scissors! ")
    type(userInput)

    #Turn all characters into lowercase and remove spaces for error handling
    userInput = userInput.lower()
    userInput = userInput.replace(' ', '')

    #Create the computer's list and then select a random input
    computerArray = ['rock', 'paper', 'scissors']
    computerChoice = random.choice(computerArray)

    #Create dictionary
    results = {"rock":"scissors",
               "scissors":"paper",
               "paper":"rock"}
    try:
        winningResults = results[userInput]

        print("The computer used: ", computerChoice)

        if userInput == computerChoice:
            print("It's a tie!")
        elif winningResults == computerChoice:
            print("You win!")
        else:
            print("You lose!")

        tryAgain = 1
        while tryAgain == 1:
            PlayAgainInput = input("Would you like to play again? (y/n) ")
            type(PlayAgainInput)
            if PlayAgainInput == "y":
                playAgain = 1
                tryAgain = 0
            elif PlayAgainInput == "n":
                playAgain = 0
                tryAgain = 0
                print("Thanks for playing")
            else:
                print("Input not recognized!")
    except:
        print("Invalid input, try again")
