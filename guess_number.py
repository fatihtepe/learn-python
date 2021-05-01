import random
target_number, guess_number = random.randint(1, 10), 0
while target_number != guess_number:
    guess_number = int(input('Guess a number between 1 and 10: '))
print('Well guessed')    



target = 8
guess = int(input('guess a number between 1-10: '))
while target != guess:
    guess =  int(input('guess again!: '))
print('good')



