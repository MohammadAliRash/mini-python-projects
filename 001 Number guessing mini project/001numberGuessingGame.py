# number guissing game

# importing
import random

# set up and initializing
min: int = 0
max: int = 10
random_number: int = random.randint(min, max)
limiter: int = 3

# user input

while limiter > 0:

    try:
        use_input = int(input('please enter a number\n'))

    except ValueError:
        print('invalid input')

    if use_input > random_number:
        print("number too big")

    elif use_input < random_number:
        print("number too small")

    else:
        print('you did it')
        break

    limiter = limiter-1
    print(f'{limiter} tries left')

if limiter == 0:
    print('you failed')

print('end of program')
