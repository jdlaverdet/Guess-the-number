# Statements
line01 = "***********************"
line02 = "*                     *"
line03 = "*  GUESS THE NUMBER!  *"
print('') #leave a blank line
print(line01)
print(line02)
print(line03)
print(line02)
print(line01)
print('')

#Strings
print("Welcome to 'Guess the Number' a game of numbers and guesses")
print('') 
print("Instructions")

#Triple-Quoted Strings
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

#Placeholders
attempts = 3
min_number = 1
max_number = 100
print("Do you have {} attempts to guess a number between {} and {}".format(attempts, min_number, max_number))

