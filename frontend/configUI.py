from PySide6 import QtCore, QtWidgets


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
        self.font_size_label = QtWidgets.QLabel("Base Font Size")
        self.font_size = QtWidgets.QLineEdit()
        self.font_size.setPlaceholderText("18")

        _buttons = QtWidgets.QDialogButtonBox.StandardButton
        self.button_box = QtWidgets.QDialogButtonBox(_buttons.Ok | _buttons.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        slayout = QtWidgets.QVBoxLayout()
        slayout.addWidget(self.api_label)
        slayout.addWidget(self.api_key)
        slayout.addWidget(self.guesses_label)
        slayout.addWidget(self.max_guesses)
        slayout.addWidget(self.font_size_label)
        slayout.addWidget(self.font_size)
        slayout.addWidget(self.button_box)
        self.setLayout(slayout)

        self.map = {
            'api_key': self.api_key,
            'max_guesses': self.max_guesses,
            'font_size': self.font_size
        }

        self.load_settings()
        self.accepted.connect(self.save_settings)

    def load_settings(self):
        """ Reload the settings from the settings store """
        self.config_manager.update_widgets_from_config(self.map)


    def save_settings(self):
        """ Triggered when the dialog is accepted; copys settings values to the settings manager """
        self.config_manager.update_config_from_widget(self.map)
