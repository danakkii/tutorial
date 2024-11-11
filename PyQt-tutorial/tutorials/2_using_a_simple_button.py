import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

# greegins
@Slot() # decorator that identifies a function
def say_hello():
    print("button clicked, hello!")

# create the Qt Application
app = QApplication(sys.argv)

# create a button
button = QPushButton("Click me")

# Connect the button to the function
button.clicked.connect(say_hello)

# show the button
button.show()

# run the main Qt Loop
app.exec()