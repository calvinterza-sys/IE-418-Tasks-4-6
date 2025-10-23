import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QLabel, QVBoxLayout
)

def add_numbers():
    try:
        num1 = float(num1_input.text())
        num2 = float(num2_input.text())
        result_label.setText(f"Result: {num1 + num2}")
    except ValueError:
        result_label.setText("Please enter valid numbers.")

def subtract_numbers():
    try:
        num1 = float(num1_input.text())
        num2 = float(num2_input.text())
        result_label.setText(f"Result: {num1 - num2}")
    except ValueError:
        result_label.setText("Please enter valid numbers.")

def multiply_numbers():
    try:
        num1 = float(num1_input.text())
        num2 = float(num2_input.text())
        result_label.setText(f"Result: {num1 * num2}")
    except ValueError:
        result_label.setText("Please enter valid numbers.")

def divide_numbers():
    try:
        num1 = float(num1_input.text())
        num2 = float(num2_input.text())
        if num2 == 0:
            result_label.setText("Error: Cannot divide by zero.")
        else:
            result_label.setText(f"Result: {num1 / num2}")
    except ValueError:
        result_label.setText("Please enter valid numbers.")

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Simple Calculator")

# Create widgets
num1_input = QLineEdit()
num1_input.setPlaceholderText("Enter first number")

num2_input = QLineEdit()
num2_input.setPlaceholderText("Enter second number")

add_btn = QPushButton("Add")
subtract_btn = QPushButton("Subtract")
multiply_btn = QPushButton("Multiply")
divide_btn = QPushButton("Divide")
result_label = QLabel("Result will appear here")

# Connect buttons to functions
add_btn.clicked.connect(add_numbers)
subtract_btn.clicked.connect(subtract_numbers)
multiply_btn.clicked.connect(multiply_numbers)
divide_btn.clicked.connect(divide_numbers)

# Create layout
layout = QVBoxLayout()
layout.addWidget(num1_input)
layout.addWidget(num2_input)
layout.addWidget(add_btn)
layout.addWidget(subtract_btn)
layout.addWidget(multiply_btn)
layout.addWidget(divide_btn)
layout.addWidget(result_label)

window.setLayout(layout)
window.show()
sys.exit(app.exec())

