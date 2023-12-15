from backend import create_app
from backend.hangman import Hangman
from charset_normalizer import md__mypyc
from frontend.qtlexecution import LexUi
from PySide6.QtGui import QFont
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
    config = get_config(settings)

    while not config.get('api_key') and not config.get('max_guesses'):
        window = LexUi()
        window.show()
        window.config()
        config = get_config(settings)

    game = Hangman(config=config)
    window = LexUi(game)

    if not window.isVisible():
        window.show()
    application = create_app(game)
    webapp = FlaskThread(application)
    webapp.start()
    qtapp.aboutToQuit.connect(webapp.terminate)

    bg = settings.value("bgstylesheet")
    if bg:
        window.centralwidget.setStyleSheet(bg)
    
    return qtapp.exec_()


def get_config(settings):
    config = {
        'api_key': settings.value('api_key'),
        'max_guesses': settings.value('max_guesses'),
        'font': settings.value('font'),
        'font_size': settings.value('font_size'),
        'font_color': settings.value('font_color')
    }

    return config

if __name__ == '__main__':
    qtapp = QApplication(sys.argv)
    sys.exit(createUi(qtapp))