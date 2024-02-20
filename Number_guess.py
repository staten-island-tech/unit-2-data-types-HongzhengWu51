from random import randrange

# number_list = ['1','2','3','4','5','6','7','9','10']
# print(random.choice(number_list))

min = 1
max = 10
random_number = randrange(min, max)


user_guess = 0
guess_history = []
while True:
    user_guess = int(input(f'\nGuess an integer number between {min} and {max}: '))

    if user_guess == random_number:
        
        break
    elif user_guess > random_number:
        print('The guess is greater than the number')
    else:
        print('The guess is less than the number')

    guess_history.append(user_guess)

    print('Already guessed: ', end=' ')
    for guess in guess_history:
        print(guess, end=' ')

print('Congratulations! The guess is correct!')
print('Guess history: ', end=' ')
for guess in guess_history:
    print(guess, end=' ')
