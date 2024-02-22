import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QLineEdit


class ConsoleWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PySide6 Console")

        self.console_output = QTextEdit()
        self.console_output.setReadOnly(True)

        self.console_input = QLineEdit()
        self.console_input.returnPressed.connect(self.process_command)

        layout = QVBoxLayout()
        layout.addWidget(self.console_output)
        layout.addWidget(self.console_input)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def process_command(self):
        command = self.console_input.text()
        output_message = f"Command entered: {command}\n"  # Ваша логика обработки команды
        self.console_output.append(output_message)
        self.console_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    console = ConsoleWindow()
    console.show()
    sys.exit(app.exec())
