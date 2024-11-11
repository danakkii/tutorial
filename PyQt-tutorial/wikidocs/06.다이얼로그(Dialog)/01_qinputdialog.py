## Ex 6-1. QInputDialog.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLineEdit, QInputDialog)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self) # QPushButton 위젯
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)
        # 버튼을 누리면 입력 대화창 (input dialog)이 나타나고, 텍스트를 입력받아서 줄편집 위젯에 표시

        self.le = QLineEdit(self) # QLineEdit 위젯 
        self.le.move(120, 35)

        self.setWindowTitle('Input dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:') # 입력 대화창이 나타남
        # 두 번째 매개변수는 대화창의 타이틀, 세 번째 매개변수는 대화창 안에 보여질 메세지를 의미
        # 입력 대화창은 입력한 텍스트와 불(boolean)값을 반환한다.
        # 텍스트를 입력한 후 ok를 누르면 불 값은 true, cancel을 누르면 불 값은 false가 된다 
        if ok: # 입력한 값을 settext() 메서드를 통해 줄 편집 위젯에 표시되도록 한다.
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
