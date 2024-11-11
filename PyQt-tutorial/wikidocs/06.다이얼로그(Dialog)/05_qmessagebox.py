## Ex 6-5. QMessageBox.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


# qwidget을 종료할 때, qclosevent가 생성되어 위젯에 전달된다.
# 위젯의 동작을 수정하기 위해 closeEvent()이벤트 핸들러를 수정해야 한다.
class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QMessageBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        # 두 번째 매개변수는 타이틀바에 나타날 문자열('message'), 세 번째 매개변수는 대화창에 나타날 텍스트 
        # 네 번쨰에는 대화창에 보여줄 버튼 종류, 마지막은 디폴드로 선택될 버튼 설정
        # QMessageBox.No로 설정할 경우, 메세지 박스가 나타났을 떄 no버튼이 선택되어 있다
        # 반환값은 reply 변수에 저장
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
