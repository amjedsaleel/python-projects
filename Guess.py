import random

secret_number = random.randrange(9)
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print(f'You won!!!\nsecret number is {secret_number}')
        break

else:
    print('Sorry, you failed ')
    print(f'Secret number is: {secret_number}')
