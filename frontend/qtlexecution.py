import os, sys
from PySide6 import QtCore, QtWidgets

from frontend import lexecution_ui
from frontend.configUI import ConfigDialog
from frontend.assets.public import images_rc


class LexUi(QtWidgets.QMainWindow, lexecution_ui.Ui_MainWindow):
    def __init__(self, game=None):
        super(LexUi, self).__init__()
        #uic.loadUi(f'{os.path.dirname(os.path.realpath(__file__))}{os.sep}lexecution2.ui', self)
        self.setupUi(self)
        self.settings = QtCore.QSettings('MitchGames', 'Lexecution')
        if game:
            self.game = game
            self.game.updated.connect(self.updateUI)
        self.actionNew.triggered.connect(self.new_game)
        self.actionConfig.triggered.connect(self.config)
        self.actionShow_Hide_Menubar.toggled.connect(self.menuToggle)
        self.actionExit.triggered.connect(sys.exit)

        self.show()

    def updateUI(self):
        if self.game:
            self.rubrick.setText(' '.join(self.game.display))
            self.definition.setText(f'Previous Word: {self.game.prev_word}<br>Definition: {self.game.prev_definition}')
            self.used_letters.setText(f'Used Letters: {" ".join(self.game.wrong)}')
            self.rogue.setStyleSheet(f'image: url(:/stickman/{self.game.used}.png)')

    def config(self):
        dlg = ConfigDialog()
        dlg.exec()

    def menuToggle(self):
        if self.actionShow_Hide_Menubar.isChecked():
            self.menubar.setVisible(False)
        else:
            self.menubar.setVisible(True)

    def new_game(self):
        if self.game:
            self.game.new_game()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = LexUi()
    sys.exit(app.exec_())