## Ex 5-3. QCheckBox.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self) # Show title이라는 텍스트 라벨을 갖는 체크박스를 하나 만듦 
        cb.move(20, 20)
        # cb.toggle() # 없으면 기본 상태가 off된 상태임
        cb.stateChanged.connect(self.changeTitle) # 체크박스의 상태가 바뀔 때 발생하는 시그널 (statechanged)을 우리가 정의한 changetitle() 메서드에 연결

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state): # 체크박스의 상태(state)가 changeTitle() 메서드의 매개변수로 주어짐 
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
