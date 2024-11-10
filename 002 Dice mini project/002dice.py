# dice program

# importing needed libraries
import random

# function for rolling dice


def rolling(number: int = 3) -> list[int]:

    # checking the input
    if number <= 0:
        print('invalid input')

    # initializing the output
    dice_list: list[int] = []

    # rolling the dice for number times
    for i in range(number):
        temp: int = random.randint(0, 6)
        dice_list.append(temp)

    # output
    return dice_list

# main function


def main():

    # asking for rolling as many times as needed
    while True:

        # getting user input
        user_input: str = str(
            input('please enter a number or write end to finish the program \n'))

        # checking to ending the loop
        if user_input.lower() == 'end':
            print('end of program')
            break

        # showing the dices
        try:
            print(rolling(int(user_input)))

        # handling the error
        except ValueError:
            print("invalid input")


# starting the program
if __name__ == '__main__':
    main()
