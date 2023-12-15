import os, sys
from PySide6 import QtCore, QtGui, QtWidgets

from frontend import lexecution_ui
from frontend.configUI import ConfigDialog
from frontend.assets.public import images_rc


class LexUi(QtWidgets.QMainWindow, lexecution_ui.Ui_MainWindow):
    def __init__(self, game=None):
        super(LexUi, self).__init__()
        self.settings = QtCore.QSettings('MitchGames', 'Lexecution')
        if game:
            self.game = game
            self.game.updated.connect(self.updateUI)
        self.setupUi(self)
        self.actionNew.triggered.connect(self.new_game)
        self.actionConfig.triggered.connect(self.config)
        self.actionFont.triggered.connect(self.font_choice)
        self.actionFontColor.triggered.connect(self.font_color)
        self.actionDefaultBG.triggered.connect(self.defaultBG)
        self.actionBGImage.triggered.connect(self.setBGImage)
        self.actionExit.triggered.connect(sys.exit)

    def updateUI(self):
        if self.game:
            self.rubrick.setText(' '.join(self.game.display))
            self.definition.setText(f'Previous Word: {self.game.prev_word}<br>Definition: {self.game.prev_definition}')
            self.used_letters.setText(f'Used Letters: {" ".join(self.game.wrong)}')
            #self.rogue.setStyleSheet(f'image: url(:/stickman/{self.game.used}.png)')
            self.rogue_recolor()

    def rogue_recolor(self):
        curr_img = QtGui.QImage(f":/stickman/{self.game.used}.png")
        color = self.settings.value('font_color')
        if not color:
            color = "#000000"
        
        curr_pm = QtGui.QPixmap.fromImage(curr_img)
        upd_pm = QtGui.QPixmap(curr_pm.size())
        upd_pm.fill(QtGui.QColor(color))
        upd_pm.setMask(curr_pm.createMaskFromColor(QtGui.QColor("transparent")))

        self.rogue.setPixmap(upd_pm)

    def font_color(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            cn = color.name()
            self.update_font(font_color = cn)
            self.settings.setValue('font_color', cn)
            self.rogue_recolor()


    def font_choice(self):
        valid, font = QtWidgets.QFontDialog.getFont(self.definition.font())
        if valid:
            self.update_font(font=font, font_size=font.pointSize())
            self.settings.setValue('font', font.family())

    def update_font(self, font=None, font_size=None, font_color=None):
        if not font:
            font = QtGui.QFont(self.settings.value('font'))

        if not font_size:
            font_size = self.settings.value('font_size')
        font_size = int(font_size)

        if not font_color:
            font_color = self.settings.value('font_color')
        
        if font_size:
            font.setPointSize(font_size)
            self.definition.setFont(font)
            font.setPointSize(font_size+4)
            self.rubrick.setFont(font)
            font.setPointSize(font_size+2)
            self.used_letters.setFont(font)
        
        if font_color:
            style = f"QLabel {{color: {font_color};}}"
            self.definition.setStyleSheet(style)
            self.rubrick.setStyleSheet(style)
            self.used_letters.setStyleSheet(style)
        self.update()

    def config(self):
        dlg = ConfigDialog()
        dlg.exec()

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