secret_word = 'rave'
guess = ''
no_of_guesses = 1
out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    guess = input('Enter guess: ')
    if guess == secret_word:
        print('You guessed correct')
    elif no_of_guesses == 3:
        print('Out of Guesses')
        out_of_guesses = True
    else:
        no_of_guesses += 1
        print('Guess again')
        print(no_of_guesses)
