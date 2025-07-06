#importing the 'random' library to generate a random pseudo number; however, this library cannot be used in a password generation project.
import random

# Set the maximum number of attempts in the game, the lower limit, and the upper limit for the randomly generated number.
lower_limit = 0
upper_limit = 20
max_attempts = 10


#Store the randomly generated number in the variable 'secret_number'
secret_number = random.randint(lower_limit, upper_limit)

#Gets the guess from the user and follows the condition required. 
# Condition is that 1) The number should be between the lower limit and the upper limit, 2) The number should be an integer and not of any other type.
def get_guess():
  while True:
      try:
        guess = int(input(f"Enter your guess between '{lower_limit}' and '{upper_limit}': "))
        if lower_limit <= guess <= upper_limit:        #check if the guess number is between the number constraints.
          return guess
        else:
           print(f"Enter a number between '{lower_limit}' and '{upper_limit}' as your guess.")
      except ValueError:      #if the guess number is anything except an integer, it is considered a ValueError.
         print("Invalid Guess. Please put a valid guess number.")

# Checks if the number is equal to, less than, or greater than the 'secret number', and gives the result accordingly.
def check_guess(guess, secret_number):
    if(guess == secret_number):
       return "Correct!"  
    elif(guess < secret_number):
       return "Too Low"
    else:
       return "Too High"           

# Add the function 'play_game' to play it as a game.
def play_game():
   attempts = 0
   won = False         #won = False because the user hasn't won yet, hence..

   while attempts < max_attempts:
      attempts += 1
      guess = get_guess()
      result = check_guess(guess, secret_number)

      if (result == "Correct!"):
         print(f"Hurray! You won the Number Guessing Game. You correctly guessed the secret number {secret_number} in {attempts} attempts!")
         won = True        #won changes to True after winning.
         break
      
      else:
         print(f"{result}. Try again!")

   if not won:               # If the value of won doesn't change, this will execute
         print(f"Sorry you ran out of attempts! The Secret Number was {secret_number}. Better Luck Next Time!")


# This will display every time we run the code
if __name__ == "__main__":
  print("Welcome to the Number Guessing Game!")
  play_game()


  #Upcoming changes which could be made in the code:-
  #1) add levels, 2) add levels according to the difficulty, 3) make a ui to make it more interactive, 4) use similar logic to make a word guessing game..  
