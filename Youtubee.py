import os
os.system('pip install Pyqt5 PyqtWebEngine')
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, QMenu
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl

class YouTubeViewer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("YouTube Viewer")
        self.setGeometry(100, 100, 800, 600)

        self.create_webview()
        self.create_menu()

    def create_webview(self):
        self.webview = QWebEngineView()
        self.webview.setUrl(QUrl("https://www.youtube.com/"))
        self.setCentralWidget(self.webview)

    def create_menu(self):
        menu_bar = self.menuBar()

        home_action = QAction("Home", self)
        home_action.triggered.connect(self.go_to_home)

        back_action = QAction("Back", self)
        back_action.triggered.connect(self.webview.back)

        music_action = QAction("Music", self)
        music_action.triggered.connect(self.music)

        settings_menu = QMenu("Settings", self)
        preset_options = settings_menu.addMenu("Preset Options")
        option1_action = QAction("Option 1", self)
        option1_action.triggered.connect(lambda: self.apply_preset("Option 1"))
        option2_action = QAction("Option 2", self)
        option2_action.triggered.connect(lambda: self.apply_preset("Option 2"))
        preset_options.addAction(option1_action)
        preset_options.addAction(option2_action)

        menu_bar.addAction(home_action)
        menu_bar.addAction(back_action)
        menu_bar.addAction(music_action)
        menu_bar.addMenu(settings_menu)
        #add menu setting to transfer to lightweight/heavyweight version

    def music(self):
        self.webview.setUrl(QUrl("https://zamwam.github.io/home/music.html"))

    def go_to_home(self):
        self.webview.setUrl(QUrl("https://www.youtube.com/"))

    def show_settings(self):
        msg = QMessageBox()
        msg.setWindowTitle("Settings")
        msg.setText("Customize your settings here.")
        msg.exec_()

    def apply_preset(self, preset_name):
        # Implement the logic to apply the selected preset
        print(f"Applying preset: {preset_name}")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Backspace:
            self.webview.back()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = YouTubeViewer()
    viewer.show()
    sys.exit(app.exec_())
