# Make a number guessing function. Your function should be able to take in a number as a user input.

# Your function should then evaluate if the user guessed the correct number.

# If the user enters a number that is above the correct number, it should output a message saying its too high
# and loop back to asking them to enter a number.

# If its below the correct number, it should output a message saying its too low and loop again.

# If they guess correct it should congratulate them and end the loop.



def guessTheNumber():
    correctumber = 8
    userGuess= int(input("guess the correct number"))
    while userGuess i= correctumber:
            userGuess= int(input("Guess the correct number"))
            print("number too high")
            userGuess= int(input("Guess the correct number"))
    else
        print("Congrats you guess correct! ")

guessTheNumber()