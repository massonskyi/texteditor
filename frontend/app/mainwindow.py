import sys

from PySide6.QtCore import QUrl
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow


class CodeEditor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl.fromLocalFile('D:\project/repo/pypr/testeditor-main/frontend/assets/html/index.html'))
        self.setCentralWidget(self.browser)
        self.setWindowTitle("Code Editor")


if __name__ == "__main__":
    print(sys.argv)
    app = QApplication(sys.argv)
    editor = CodeEditor()
    editor.show()
    sys.exit(app.exec())
