import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image
import numpy as np

class ImageRotator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Rotator")
        self.setGeometry(100, 100, 800, 600)  

        self.layout = QVBoxLayout()

        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)  
        self.layout.addWidget(self.image_label)

        self.rotate_button = QPushButton("Rotate Image", self)
        self.rotate_button.clicked.connect(self.rotate_image)
        self.layout.addWidget(self.rotate_button)

        central_widget = QWidget(self)
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        self.image_path = ""
        self.current_image = None

        self.load_image()

    def load_image(self):
        self.image_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if self.image_path:
            self.display_image(self.image_path)

    def display_image(self, path):
        self.current_image = Image.open(path)
        self.update_image_display()

    def update_image_display(self):
        if self.current_image:
            qt_image = QPixmap(self.image_path)
            self.image_label.setPixmap(qt_image) 
            self.image_label.resize(qt_image.size())

    def rotate_image(self):
        if self.current_image:
            image_array = np.array(self.current_image)
            print(f"origin image_array.shape: {image_array.shape}")
            rotated_image_array = np.rot90(image_array,k=2)
            print(f"rotation rotated_image_array.shape: {rotated_image_array.shape}")
            self.current_image = Image.fromarray(rotated_image_array)
            self.current_image.save(self.image_path)
            self.update_image_display()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ImageRotator()
    window.show()
    sys.exit(app.exec_())
