import os, sys
from PySide6 import QtCore, QtWidgets

from frontend import lexecution_ui
from frontend.configUI import ConfigDialog
from frontend.assets.public import images_rc


class LexUi(QtWidgets.QMainWindow, lexecution_ui.Ui_MainWindow):
    def __init__(self, game=None):
        super(LexUi, self).__init__()
        self.setupUi(self)
        self.settings = QtCore.QSettings('MitchGames', 'Lexecution')
        if game:
            self.game = game
            self.game.updated.connect(self.updateUI)
        self.actionNew.triggered.connect(self.new_game)
        self.actionConfig.triggered.connect(self.config)
        self.actionDefaultBG.triggered.connect(self.defaultBG)
        self.actionBGImage.triggered.connect(self.setBGImage)
        self.actionExit.triggered.connect(sys.exit)

    def updateUI(self):
        if self.game.running:
            self.rubrick.setText(' '.join(self.game.display))
            self.definition.setText(f'Previous Word: {self.game.prev_word}<br>Definition: {self.game.prev_definition}')
            self.used_letters.setText(f'Used Letters: {" ".join(self.game.wrong)}')
            self.rogue.setStyleSheet(f'image: url(:/stickman/{self.game.used}.png)')

    def updateFont(self):
        font_size = self.settings.value('font_size')
        if not font_size:
            font_size = 18
        font_size = int(font_size)
        if font_size:
            font = self.definition.font()
            font.setPointSize(font_size)
            self.definition.setFont(font)
            font.setPointSize(font_size+6)
            self.rubrick.setFont(font)
            font.setPointSize(font_size+2)
            self.used_letters.setFont(font)
            self.update()

    def config(self):
        dlg = ConfigDialog()
        dlg.exec()
        self.updateFont()

    def setBGImage(self):
        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        if dlg.exec():
            filename = dlg.selectedFiles()
            if filename:
                        path = os.path.realpath(filename[0])
                        path = path.replace("\\", "/")
                        stylesheet = f"QWidget#centralwidget{{border-image: url(\"{path}\") 0 0 0 0 stretch stretch;}}"
                        self.settings.setValue("bgstylesheet", stylesheet)
                        self.centralwidget.setStyleSheet(stylesheet)

    def defaultBG(self):
        self.settings.setValue("bgstylesheet", None)
        stylesheet = u"QWidget#centralwidget{border-image: url(:/background/castletext.jpg);}"
        self.centralwidget.setStyleSheet(stylesheet)

    def new_game(self):
        if self.game:
            self.game.new_game()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = LexUi()
    sys.exit(app.exec_())