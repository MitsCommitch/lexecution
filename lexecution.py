from backend import create_app
from backend.hangman import Hangman
from frontend.qtlexecution import LexUi
from PySide6.QtCore import QThread, QSettings
from PySide6.QtWidgets import QApplication
from waitress import serve

import sys

class FlaskThread(QThread):
    def __init__(self, application):
        QThread.__init__(self)
        self.application = application

    def __del__(self):
        self.wait()

    def run(self):
        serve(self.application, host="localhost", port=2749)

def createUi(qtapp):
    settings = QSettings('MitchGames', 'Lexecution')
    config = {
        'api_key': settings.value('api_key'),
        'max_guesses': settings.value('max_guesses')
    }
    window = LexUi()
    window.show()
    if not config['api_key']:
        window.config()
    game = None
    while not game:
        try:
            game = Hangman(config=config)
            window = LexUi(game)
        except ValueError as ve:
            window = LexUi()
            window.show()
            window.config()
        
    application = create_app(game)
    webapp = FlaskThread(application)
    webapp.start()
    qtapp.aboutToQuit.connect(webapp.terminate)
    window.updateUI()
    
    return qtapp.exec_()


if __name__ == '__main__':
    qtapp = QApplication(sys.argv)
    sys.exit(createUi(qtapp))