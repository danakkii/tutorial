# https://wikidocs.net/70990

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# worker -> emit(1,2) -> mywindow
class Worker(QObject): # QObject를 상속받는 Worker라는 이름의 클래스를 정의
    user_signal = pyqtSignal(int, int) # pyqtSignal 객체를 생성할 때 타입을 명시해서 객체 생성하기
    # 클래스 변수로 pyqtSignal 객체를 바인딩
    # 변수 이름으로 user_signal이라고 했는 데 이 변수의 이름이 시그널이 됩니다.
    # 앞서 버튼에서는 clicked라는 시그널이 존재했는 데 이와 유사하게 worker 클래스에는 user_signal이라는 시그널이 생성됨
    push_signal = pyqtSignal(int, int)

    def run(self):
        self.user_signal.emit(1,2) # emit() 메서드를 호출할 때 실제 값을 인자로 넘겨주기
        self.user_signal2.emit(3,4)
        self.push_siganl.emit(5,6)
        

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        worker= Worker()
        worker.user_signal.connect(self.user_slot) # self.user_slot이라는 메서드가 콜백될 수 있도록 생성자에서 한 번 등록된다.
        worker.user_signal2.connect(self.user_slot2) # connect 시그널로 app의 quit()
        worker.run() # worker 클래스의 run() 메서드를 호출하여 user_signal 이벤트가 방출되도록 한다.
        # gui에서 run 메서드 실행

    @pyqtSlot(int,int) # 슬롯의 데코레이터에 데이터 타입 명시하기
    def user_slot(self, arg1, arg2): # 슬롯의 메서드 인자로 데이터를 받기, run에서 emit으로 1,2 을 gui로 방출
        print(arg1, arg2)

    @pyqtSlot(int,int)
    def user_slot2(self, arg3, arg4):
        print(arg3, arg4)


app = QApplication(sys.argv) # 프로그램을 만들기 위한 하나의 큰 바구니 생성
# sys.argv = qapplication이라는 객체가 실행할 파일인 파이썬 코드
window = MyWindow() # 윈도우 생성
window.show() 
app.exec_() # 무한 루프 상태 종료 = 정상종료

"""
시그널이 발출될 떄 데이터를 보내면 이벤트 루프는 이 값을 시그널을 처리하기로 한 슬롯을 호출할 때
함수 또는 메서드의 인자로 전댈하 준다. 사용자 정의 시그널에서 값을 전달하고자 할 때 필요한 부분을 정리하겠다.
"""
