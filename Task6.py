import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout

# Global order list
current_order = []

# Menu (item names and prices)
menu = {
    "Burger": 8.99,
    "Pizza": 12.99,
    "Salad": 6.50,
    "Fries": 3.50,
    "Drink": 2.99
}

# ---------------- METHODS ----------------
def add_to_order(item, price):
    """Add an item to the current order."""
    current_order.append((item, price))

def calculate_subtotal():
    """Return the subtotal (sum of all prices)."""
    return sum(price for _, price in current_order)

def calculate_tax(subtotal):
    """Return 6% sales tax."""
    return subtotal * 0.06

def calculate_total():
    """Return subtotal + tax."""
    subtotal = calculate_subtotal()
    tax = calculate_tax(subtotal)
    return subtotal + tax

def update_display():
    """Update the order summary, subtotal, tax, and total labels."""
    order_text = ""
    for item, price in current_order:
        order_text += f"{item}: ${price:.2f}\n"
    
    order_display.setText(order_text if order_text else "No items in order.")

    subtotal = calculate_subtotal()
    tax = calculate_tax(subtotal)
    total = calculate_total()

    subtotal_label.setText(f"Subtotal: ${subtotal:.2f}")
    tax_label.setText(f"Tax (6%): ${tax:.2f}")
    total_label.setText(f"Total: ${total:.2f}")

def clear_order():
    """Clear the order and reset the display."""
    current_order.clear()
    update_display()

# ---------------- BUTTON HANDLERS ----------------
def on_burger_clicked():
    add_to_order("Burger", menu["Burger"])
    update_display()

def on_pizza_clicked():
    add_to_order("Pizza", menu["Pizza"])
    update_display()

def on_salad_clicked():
    add_to_order("Salad", menu["Salad"])
    update_display()

def on_fries_clicked():
    add_to_order("Fries", menu["Fries"])
    update_display()

def on_drink_clicked():
    add_to_order("Drink", menu["Drink"])
    update_display()

# ---------------- UI SETUP ----------------
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Restaurant Order System")

# Create widgets
title_label = QLabel("Restaurant Menu")
title_label.setStyleSheet("font-size: 18px; font-weight: bold; text-align: center;")

order_display = QTextEdit()
order_display.setReadOnly(True)
order_display.setPlaceholderText("Your order will appear here...")

subtotal_label = QLabel("Subtotal: $0.00")
tax_label = QLabel("Tax (6%): $0.00")
total_label = QLabel("Total: $0.00")

# Menu item buttons
burger_btn = QPushButton(f"Burger - ${menu['Burger']:.2f}")
pizza_btn = QPushButton(f"Pizza - ${menu['Pizza']:.2f}")
salad_btn = QPushButton(f"Salad - ${menu['Salad']:.2f}")
fries_btn = QPushButton(f"Fries - ${menu['Fries']:.2f}")
drink_btn = QPushButton(f"Drink - ${menu['Drink']:.2f}")

clear_btn = QPushButton("Clear Order")
clear_btn.setStyleSheet("background-color: #f66; color: white; font-weight: bold;")

# Connect buttons
burger_btn.clicked.connect(on_burger_clicked)
pizza_btn.clicked.connect(on_pizza_clicked)
salad_btn.clicked.connect(on_salad_clicked)
fries_btn.clicked.connect(on_fries_clicked)
drink_btn.clicked.connect(on_drink_clicked)
clear_btn.clicked.connect(clear_order)

# ---------------- LAYOUT ----------------
layout = QVBoxLayout()
layout.addWidget(title_label)

menu_layout = QHBoxLayout()
menu_layout.addWidget(burger_btn)
menu_layout.addWidget(pizza_btn)
menu_layout.addWidget(salad_btn)
menu_layout.addWidget(fries_btn)
menu_layout.addWidget(drink_btn)
layout.addLayout(menu_layout)

layout.addWidget(order_display)
layout.addWidget(subtotal_label)
layout.addWidget(tax_label)
layout.addWidget(total_label)
layout.addWidget(clear_btn)

window.setLayout(layout)
update_display()
window.show()
sys.exit(app.exec())
