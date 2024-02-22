import sys

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTreeView, QFileSystemModel


class CustomFileSystemWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.model = QFileSystemModel()
        self.model.setRootPath('')
        self.model.setFilter(self.model.filter() | QDir.Hidden | QDir.AllDirs)

        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(''))

        layout.addWidget(self.tree_view)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_system_widget = CustomFileSystemWidget()

    window = QMainWindow()
    window.setWindowTitle("Custom File System Widget")
    window.setCentralWidget(file_system_widget)
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())
