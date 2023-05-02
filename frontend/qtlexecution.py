import os, sys
from PySide6 import QtCore, QtWidgets

from frontend import lexecution2_ui
from frontend.assets.public import images_rc


class LexUi(QtWidgets.QMainWindow, lexecution2_ui.Ui_MainWindow):
    def __init__(self, game=None):
        super(LexUi, self).__init__()
        #uic.loadUi(f'{os.path.dirname(os.path.realpath(__file__))}{os.sep}lexecution2.ui', self)
        self.setupUi(self)
        self.settings = QtCore.QSettings('MitchGames', 'Lexecution')
        if game:
            self.game = game
            self.game.updated.connect(self.updateUI)
        self.actionNew.triggered.connect(self.new_game)
        self.actionExit.triggered.connect(sys.exit)
        self.actionConfig.triggered.connect(self.config)
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

    def set_game(self, game):
        self.game = game

    def new_game(self):
        if self.game:
            self.game.new_game()


class ConfigManager(QtCore.QObject):

    widget_mappers = {
        'QLineEdit': ('text', 'setText'),
    }

    config_changed = QtCore.Signal()

    def __init__(self) -> None:
        super().__init__()

        self.settings = QtCore.QSettings('MitchGames', 'Lexecution')

    def update_widgets_from_config(self, map):
        for name, widget in map.items():
            cls = widget.__class__.__name__
            getter, setter = self.widget_mappers.get(cls, (None, None))
            value = self.settings.value(name)
            if setter and value is not None:
                fn = getattr(widget, setter)
                fn(value)  # Set the widget.

    def update_config_from_widget(self, map):
        for name, widget in map.items():
            cls = widget.__class__.__name__
            getter, setter = self.widget_mappers.get(cls, (None, None))
            if getter:
                fn = getattr(widget, getter)
                value = fn()                
                if value is not None:
                    self.settings.setValue(name, value) # Set the settings.

        # Notify watcher of changed settings.
        self.config_changed.emit()

class ConfigDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.config_manager = ConfigManager()

        self.api_label = QtWidgets.QLabel("Wordnik API Key")
        self.api_key = QtWidgets.QLineEdit()
        self.api_key.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.guesses_label = QtWidgets.QLabel("Max Guesses")
        self.max_guesses = QtWidgets.QLineEdit()

        _buttons = QtWidgets.QDialogButtonBox.StandardButton
        self.button_box = QtWidgets.QDialogButtonBox(_buttons.Ok | _buttons.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        slayout = QtWidgets.QVBoxLayout()
        slayout.addWidget(self.api_label)
        slayout.addWidget(self.api_key)
        slayout.addWidget(self.guesses_label)
        slayout.addWidget(self.max_guesses)
        slayout.addWidget(self.button_box)
        self.setLayout(slayout)

        self.map = {
            'api_key': self.api_key,
            'max_guesses': self.max_guesses
        }

        self.load_settings()
        self.accepted.connect(self.save_settings)

    def load_settings(self):
        """ Reload the settings from the settings store """
        self.config_manager.update_widgets_from_config(self.map)


    def save_settings(self):
        """ Triggered when the dialog is accepted; copys settings values to the settings manager """
        self.config_manager.update_config_from_widget(self.map)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = LexUi()
    sys.exit(app.exec_())