import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QTextEdit, QVBoxLayout, QPushButton, QWidget, QLabel, QGraphicsView, QGraphicsScene, QGraphicsEllipseItem, QComboBox

class JupyterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Jupyter-like App")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Code Input Area
        self.code_input = QPlainTextEdit(self)
        layout.addWidget(self.code_input)

        # Output Area
        self.output_area = QTextEdit(self)
        self.output_area.setReadOnly(True)
        layout.addWidget(self.output_area)

        # Toolbar with buttons
        toolbar = QWidget(self)
        layout.addWidget(toolbar)

        toolbar_layout = QVBoxLayout(toolbar)

        run_button = QPushButton("Run Code", self)
        run_button.clicked.connect(self.run_code)
        toolbar_layout.addWidget(run_button)

        clear_button = QPushButton("Clear Output", self)
        clear_button.clicked.connect(self.clear_output)
        toolbar_layout.addWidget(clear_button)

        # Dropdown menu to select block type
        self.block_type_combo = QComboBox(self)
        self.block_type_combo.addItems(["Text", "Code", "Graph"])
        toolbar_layout.addWidget(self.block_type_combo)

        # Button to add a block dynamically
        add_block_button = QPushButton("Add Block", self)
        add_block_button.clicked.connect(self.add_dynamic_block)
        toolbar_layout.addWidget(add_block_button)

    def run_code(self):
        # Execute code and update output area
        code = self.code_input.toPlainText()
        try:
            res = exec(code)
            self.output_area.setPlainText(str(res))
        except Exception as e:
            self.output_area.append(f"Error: {str(e)}")

    def clear_output(self):
        self.output_area.clear()

    def add_dynamic_block(self):
        selected_type = self.block_type_combo.currentText()
        content = f"Custom {selected_type} Block"

        if selected_type.lower() == "text":
            block = QLabel(content, self)
            block.setStyleSheet("background-color: #f0f0f0; padding: 5px; margin-bottom: 10px;")
        elif selected_type.lower() == "code":
            block = QPlainTextEdit(content, self)
            block.setReadOnly(True)
            block.setStyleSheet("background-color: #333; color: #fff; padding: 5px; margin-bottom: 10px;")
        elif selected_type.lower() == "graph":
            block = QGraphicsView(self)
            scene = QGraphicsScene(self)
            ellipse_item = QGraphicsEllipseItem(0, 0, 50, 50)
            scene.addItem(ellipse_item)
            block.setScene(scene)
            block.setStyleSheet("background-color: #ddd; padding: 5px; margin-bottom: 10px;")

        layout = self.centralWidget().layout()
        layout.addWidget(block)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = JupyterApp()
    window.show()

    sys.exit(app.exec())