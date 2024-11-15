import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel

# if __name__ == "__main__":
#     app = QApplication()
#     w = QLabel("This is a placeholder text")
#     w.setAlignment(Qt.AlignCenter)
#     w.show()
#     sys.exit(app.exec())

# if __name__ == "__main__":
#     app = QApplication()
#     w = QLabel("This is a placeholder text")
#     w.setAlignment(Qt.AlignCenter)
#     w.setStyleSheet("""
#         background-color: #262626;
#         color: #FFFFFF;
#         font-family: Titillium;
#         font-size: 18px;
#         """)
#     w.show()
#     sys.exit(app.exec())


if __name__ == "__main__":
    app = QApplication()

    w = Widget()
    w.show()

    with open("style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())

    