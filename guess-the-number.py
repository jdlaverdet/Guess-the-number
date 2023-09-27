
import random

min_number = 26
max_number = 78
max_attempts = 6  # Set the maximum number of attempts

line01 = "***********************"
line02 = "*                     *"
line03 = "*  GUESS THE NUMBER!  *"
print('') # An empty string leaves a blank line but, it isn't a good practice
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)


print("\nWelcome to 'Guess the Number' a game of numbers and guesses")
print('') 
print("\nInstructions")
print("Do you have {} attempts to guess a number between {} and {}\n".format(max_attempts, min_number, max_number))

# While loop for the random number
while True:
    random_number = random.randint(min_number, max_number)
    attempts = 0 
    
# While loop that keeps the game running    
    while attempts < max_attempts:  # Add a condition to limit the attempts
        guess = int(input("Let's play, 'Guess the Number' between {} and {}: ".format(min_number, max_number)))
        attempts += 1

        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print(
"""
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
"""
)
            print("Congratulations! You guessed the number in {} attempts.".format(attempts))
            break

    if attempts >= max_attempts:
        print("Sorry, you've reached the maximum number of attempts. The correct number was {}.".format(random_number))

    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
