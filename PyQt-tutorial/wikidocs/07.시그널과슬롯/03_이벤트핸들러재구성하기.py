
## Ex 7-3. 이벤트 핸들러 재구성하기.

"""
esc, F, N 키를 클릭하면 창이 종료되거나 최대화, 보통 크기가 되도록 이벤트 핸들러를 재구성함
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self, e): # keyPressEvent 이벤트 핸들러는 키보드의 이벤트를 입력으로 받는다
        if e.key() == Qt.Key_Escape: # e.key()는 어떤 키를 누르거나 뗐는 지를 반환한다
            self.close() # esc 키를 눌렀다면, self.close()를 통해 위젯이 종료된다
        elif e.key() == Qt.Key_F: # F 키 또는 N 키를 눌렀다면, 위젯의 크기가 최대화되거나 보통 크기가 된다. 키보드 
            self.showFullScreen()
        elif e.key() == Qt.Key_N:
            self.showNormal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
