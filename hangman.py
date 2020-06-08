import random
import os


# 1st: make a list of words you would want to use
# 2nd: randomly choose a word for list to be guessed, assign it to secretword
# 3rd: prompt user for input to choose letters from (a-z)


# create the object for Hangman
class Hangman():

    ''' can crate your own list of words to be used'''


    def __init__(self, words=[
        'developer',
        'system',
        'outdoor',
        'python',
        'alphabet',
        'google',
        'amazing',
        'cowboy',
        'apple',
        'samsung',
        'hangman'
    ]):
        self.words = words
        self.chances = 8
        self.secretword = ''
        self.user = ''
        self.guessed = ''

    def setup(self):
        self.secretword = self.words[random.randint(0, len(self.words) - 1)]
        self.user = ''
        self.guessed = ''
        #creates a "userview" of underscores matching lenght of the word to guess
        self.user = '_' *len(self.secretword)
        
    
    def status(self):
        print(f'You have {self.chances} chances left.\n {self.user}')

    def prompt(self):
        guess = input('Guess a letter: ').lower()
        if guess in 'abcdefghijklmnopqrstuvwxyz' and guess not in self.guessed:
            self.guessed += guess
            if guess in self.secretword:
                print('\nNice guess')

                # replace all indices in user with matching letter
                for i, char in enumerate(self.secretword):
                    #converts string of underscores into list
                    listview = list(self.user)
                    if guess == char:
                        # replaces letters at index that match guess
                        listview[i] = guess
                        # convert user back into string
                        self.user = ''.join(listview)

                if self.user == self.secretword:
                    print(f'\nYou Win!\nYou guessed the word: {self.secretword}')
                    return True
            else:
                print('\nWrong guess')
                self.chances -= 1
                if self.chances <= 0:
                    print(f'\nSorry, You lose!\nThe word to guess was {self.secretword}...')
                    return True
        else:
            print('\nPlease choose a letter (a-z).')


def game():
    os.system('cls||clear')
    game = Hangman()
    active = True
    game.setup()

    while active:
        game.status()
        if game.prompt():
            active = False
    print(f'\nThank you for playing!')

game()