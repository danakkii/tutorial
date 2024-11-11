## Ex 5-1. QPushButton.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()                               

    def initUI(self):
        btn1 = QPushButton('&Button1', self) # QPushButton 클래스로 푸시 버튼을 하나 만듦
        # 첫 번째 파라미터로는 버튼에 나타날 텍스트, 두 번째는 버튼이 속할 부모 클래스 지정
        # 단축키 설정은 &
        btn1.setCheckable(True) # 선택되거나 선택되지 않은 상태를 유지
        btn1.toggle() # toggle() 메서드를 호출하면 버튼의 상태가 바뀐다. 따라서 이 버튼을 프로그램이 시작될 때 선택되어 있다. 

        btn2 = QPushButton(self)
        btn2.setText('Button&2') # setText() 메서드로 버튼에 표시될 텍스트를 지정
        # 단축키 alt+2
        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False) # 버튼을 사용할 수 없게됨
        
        btn4 = QPushButton(self)
        btn4.setText('Button&4')

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        # self.setGeometry(300, 300, 300, 200)
        self.setGeometry(300, 300, 100, 100)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
