import sys
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QTextEdit, QLabel, QVBoxLayout

# Global shopping list
shopping_list = []
prices = []

def add_item():
    item = item_input.text().strip()
    price_text = price_input.text().strip()
    
    # Validate inputs
    if not item:
        result_label.setText("Please enter an item name.")
        return
    
    try:
        price = float(price_text)
    except ValueError:
        result_label.setText("Error: Price must be a number.")
        return

    # Add item and price
    shopping_list.append(item)
    prices.append(price)
    
    # Clear input fields
    item_input.clear()
    price_input.clear()
    
    # Update display
    update_display()

def calculate_total():
    return sum(prices)

def update_display():
    # Show all items and total
    items_text = ""
    for item, price in zip(shopping_list, prices):
        items_text += f"{item}: ${price:.2f}\n"
    text_area.setText(items_text)
    
    total = calculate_total()
    total_label.setText(f"Total: ${total:.2f}")
    result_label.setText("")  # Clear any error messages

# Create the app
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Shopping List App")

# Create widgets
item_input = QLineEdit()
item_input.setPlaceholderText("Enter item name")

price_input = QLineEdit()
price_input.setPlaceholderText("Enter item price")

add_btn = QPushButton("Add Item")
text_area = QTextEdit()
text_area.setReadOnly(True)

total_label = QLabel("Total: $0.00")
result_label = QLabel("")
result_label.setStyleSheet("color: red;")

# Connect button
add_btn.clicked.connect(add_item)

# Layout
layout = QVBoxLayout()
layout.addWidget(QLabel("Shopping List"))
layout.addWidget(item_input)
layout.addWidget(price_input)
layout.addWidget(add_btn)
layout.addWidget(text_area)
layout.addWidget(total_label)
layout.addWidget(result_label)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
