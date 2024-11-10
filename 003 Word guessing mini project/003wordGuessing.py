import random


def guessing():

    # setup
    word: str = random.choice(['horse', 'pen', 'zoo', 'monkey'])
    already_guessed: str = ''
    tries: int = 30

    # guessing part
    while tries > 0:
        blank: int = 0

        # blank counts the number of letters in the chosen word if its letter is not already guessed
        for char in word:
            if char in already_guessed:
                print(char)

            else:
                print('-')
                blank += 1

        # if every blank letter in word is guessed then user won the game
        if blank == 0:
            print('you won')
            break

        # getting letter from user
        user_guess: str = input('please enter a letter')

        already_guessed += user_guess

        if user_guess not in word:
            tries -= 1

        if tries == 0:
            print('you lost')
            break


if __name__ == '__main__':
    guessing()
