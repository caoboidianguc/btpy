import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I'm Grok 2, your game AI, and I'm thinking of a number between 1 and 20.")

    # The number to guess
    secret_number = random.randint(1, 20)
    
    # Number of tries
    tries = 0

    while True:
        # Get the player's guess
        guess = input("Take a guess, young earthling: ")
        
        # Check if the input is a number
        if not guess.isdigit():
            print("Oops! That's not a number. Try again!")
            continue

        guess = int(guess)
        tries += 1

        # The AI's witty responses based on the guess
        if guess < secret_number:
            print("Too low! Aim for the stars, or at least a bit higher!")
        elif guess > secret_number:
            print("Whoa, too high! We're not trying to reach the moon here!")
        else:
            print(f"Fantastic guessing! You've got it in {tries} tries!")
            if tries == 1:
                print("First try? Are you sure you're not telepathic?")
            elif tries < 5:
                print("You're on fire! Are you cheating, or just that good?")
            else:
                print("Persistence pays off! Well done!")
            break

        # Encouraging or teasing messages
        if tries == 3:
            print("Here's a hint: Think of your age and perhaps add or subtract a few.")

    # Ask to play again
    play_again = input("Want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_the_number()
    else:
        print("Thanks for playing! Remember, in the vast universe of numbers, you're number one at guessing!")

# Start the game
guess_the_number()