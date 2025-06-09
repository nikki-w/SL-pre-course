import random


# Function to ask user to guess a number
def guess():
    return input('Input your guess here: ')

# Start game
def number_game():
    print('Welcome to the guessing game. Guess the correct number (between 1 and 100) and you win!')
    # Define random secret number:
    # Use random to generate a random number in the range 1 to 100
    secret_number = random.randrange(1, 100)
    
    # Start user guess
    user_guess = guess()
    
    # Start guess counter
    guess_counter = 0
    
    while int(user_guess) is not secret_number:
        # If guess number is lower than secret number do the following
        if int(user_guess) < secret_number:
            print('Sorry, your guess was too low, please try again')
            # Ask for new guess from user
            new_user_guess = guess()
            # Only add to guess counter if the previous number and new number 
            # are different
            if new_user_guess == user_guess:
                user_guess = new_user_guess
            else:
                user_guess = new_user_guess
                guess_counter += 1
            
        # If guess number is higher than secret number do the following
        else:
            print('Sorry, your guess was too high, please try again')
            # Ask for new guess from user
            new_user_guess = guess()
            # Only add to guess counter if the previous number and the new number
            # are different
            if new_user_guess == user_guess:
                user_guess = new_user_guess
            else:
                user_guess = new_user_guess
                guess_counter += 1
            
        # If guess number is correct and equals secret number do the following
        if int(user_guess) == secret_number:
            # Add to counter to ensure their final guess is taken into account
            guess_counter += 1
            print(f'Congratulations, the secret number was {secret_number}, you win!')
            print(f'You succeeded in {guess_counter} guess(es).')

# Play the game
number_game()
