from bleach import clean
from os import getenv
from string import punctuation
from .utils import findall
from .words import Words
from PySide6.QtCore import Signal, QObject

class Hangman(QObject):
    updated = Signal()

    def __init__(self, config=None, parent=None):
        super(Hangman, self).__init__(parent)
        if config:
            self.config = config
        else:
            self.config = {
                'api_key': getenv('WORDNIK_API_KEY', ''),
                'max_guesses': getenv('HANGMAN_MAX_GUESSES', '9')
            }

        self.guesses = int(self.config.get('max_guesses'))
        self.used = self.guesses
        self.words = Words(self.config.get('api_key'))
        self.running = True
        self.win = False
        self.word = None
        self.definition = None
        self.prev_word = None
        self.prev_definition = None
        self.wrong = []
        self.right = []

        self.new_game()

    def status(self):
        return {
            'guesses': self.guesses,
            'running': self.running,
            'win': self.win,
            'prev': self.prev_word,
            'curr': self.word,
            'prev_def': self.prev_definition,
            'rubrick': self.rubrick
        }


    def new_game(self, config=None):
        if self.prev_word:
            prev = self.prev_word
        elif self.word:
            prev = self.word
        else:
            prev = None
        try:
            self.word = self.words.get_word()
        except AttributeError as err:
            print(f'Could not get word! {err}')
            return err
        self.word_length = len(self.word)
        self.definition = self.get_definition(self.word)
        self.rubrick = '_'*len(self.word)
        self.replace_special()
        self.display = ' '.join(self.rubrick)
        self.wrong = []
        self.right = []
        self.used = self.guesses
        self.running = True
        self.updated.emit()

    def replace_special(self):
        for punct in punctuation:
            self.replace_hits(punct)

    def replace_hits(self, guess):
        hits = findall(guess, self.word.lower())
        for hit in hits:
            self.rubrick = self.rubrick[:hit] + self.word[hit] + self.rubrick[hit+1:]
        self.display = ' '.join(self.rubrick)

    def get_definition(self, word):
        return self.words.get_def(word)

    def guess(self, guess):
        if not self.running:
            message = 'No one is currently due to be hanged!'
            return message

        if not guess:
            message = 'You have to make a guess!'
            return message

        guess_length = len(guess)

        # Full word guess
        if guess_length == self.word_length:
            message = ''
            if guess.lower() == self.word.lower():
                self.rubrick = self.word
                self.display = ' '.join(self.rubrick)
                message = self.check_done()
            else:
                self.used-=1
                self.check_done()
                if not message:
                    message = f'Sorry, {guess} is not the word. Keep guessing!'
            self.updated.emit()
            return message

        if guess_length > 1:
            if guess_length < self.word_length:
                message = f'Sorry, {guess} is too short. Word is {self.word_length} long!'
            else:
                message = f'Sorry, {guess} is too long. Word is {self.word_length} long!'
            return message

        # Letter guess, force single char
        guess = guess[0]
        guess = guess.lower()

        if guess in self.right or guess in self.wrong:
            message = f'Letter {guess} was already used, try again!'
        elif guess in self.word.lower():
            self.right.append(guess)
            self.replace_hits(guess)
            message = f'You found {guess}!'
        else:
            message = f'Sorry, {guess} is not in the word. Keep guessing!'
            self.wrong.append(guess)
            self.used-=1

        done = self.check_done()

        if done:
            self.updated.emit()
            return done

        self.updated.emit()
        return message

    def check_done(self):
        message = ''
        if '_' not in self.rubrick:
            message = f'You got it! The word was {self.word}'
            self.win = True
            self.running = False
            self.prev_word = self.word
            self.prev_definition = self.definition
        elif self.used < 1:
            message = f"Oh no! We didn't get the word in time. The word was: {self.word}"
            self.running = False
            self.prev_word = self.word
            self.prev_definition = self.definition
        if message:
            message = f'{message}\n'
        return message
            
    def hangman(self):
        while self.used and not self.win:
            print(f'{self.display}\nGuesses: {self.used}  Tried Letters: {self.wrong}')
            guess = input('What is your guess?\n').lower()
            guess = clean(guess)
            message = self.guess(guess)
            print(message)
        
        
if __name__ == "__main__":
    h = Hangman()
    h.hangman()
