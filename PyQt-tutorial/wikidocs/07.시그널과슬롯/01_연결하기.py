## Ex 7-1. 연결하기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self) # lcd화면과 같이 숫자 표시
        dial = QDial(self) # 회정해서 값 조절하는 위젯
        
        vbox = QVBoxLayout() # 수직 박스 레이아웃 하나 만들어서 QLCDNumber와 QDial 위젯을 넣어줌
        vbox.addWidget(lcd) # 시그널을 받는 객체인 수신자는 ldc
        vbox.addWidget(dial) # 시그널을 보내는 객체인 송신자는 dial
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display) # valueChanged 시그널을 lcd의 display 슬롯에 연결한다
        # display 슬롯은 숫자를 받아서 QLCDNumber 위젯에 표시하는 역할 
        # slot은 시그널에 어떻게 반응할지를 구현한 메서드

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 200, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp() # MyApp 위젯의 레이아웃으로 설정 
    sys.exit(app.exec_())
