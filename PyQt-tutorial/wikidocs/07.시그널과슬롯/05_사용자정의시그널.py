## Ex 7-5. 사용자 정의 시그널.

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow


class Communicate(QObject): # communicate 클래스의 속성으로서 closeApp이라는 시그널을 하나 만듦

    closeApp = pyqtSignal() # 사용자 정의 시그널 생성, 특정 이벤트가 발생했을 때 이 시그널이 방출되도록 생성


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate() # communicate 클래스의 closeApp 시그널의 MyApp 클래스의 close() 슬롯에 연결
        self.c.closeApp.connect(self.close) # 마우스 클릭 시 발생해서 qmainwindow의 close() 슬롯에 연결되어 프로그램을 종료

        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self, e): # mousePressEvent 이벤트 핸들러를 사용해서, 마우스 클릭했을 때 closeApp시그널이 방출되도록 함 
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
