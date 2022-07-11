### 창 닫기
## 버튼 / 시그널(Signal) / 슬롯(Slot)

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
# from PyQt5.QtCore import QCoreApplication   
# # QtCore 모듈의 QCoreApplication 클래스: 이벤트를 제공하는 클래스


# class MyApp(QWidget):

#   def __init__(self):
#       super().__init__()
#       self.initUI()

#   def initUI(self):
#       btn = QPushButton('Quit', self)   #푸쉬버튼 생성 #(button text, Parent)
#       btn.move(50, 50)  #버튼 생성 위치 좌표
#       btn.resize(btn.sizeHint())  #resize(): 버튼 크기 조절  #btn.sizeHint(): 기본 버튼 사이즈
#       btn.clicked.connect(QCoreApplication.instance().quit) #clicked: 버튼 액션 지정
#         #QCoreApplication.instance(): 현재 객체를 의미 #.quit: 닫기 명령 
#       self.setWindowTitle('Quit Button')
#       self.setGeometry(300, 300, 300, 200)
#       self.show()


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())


### 툴팁 (버튼에 마우스를 올려두면 버튼에 대한 설명이 나오는 기능)

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtCore import QCoreApplication   
from PyQt5.QtGui import QFont
# QtCore 모듈의 QCoreApplication 클래스: 이벤트를 제공
# QtGui 모듈의 QFont 클래스: 폰트이름과 크기 지정

class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      btn = QPushButton('Quit', self)   #푸쉬버튼 생성 #(button text, Parent)
      btn.move(50, 50)  #버튼 생성 위치 좌표
      btn.resize(btn.sizeHint())  #resize(): 버튼 크기 조절  #btn.sizeHint(): 기본 버튼 사이즈
      btn.clicked.connect(QCoreApplication.instance().quit) #clicked: 버튼 액션 시그널
      #QCoreApplication.instance(): 현재 객체를 의미 #.quit: 닫기 명령
      
      QToolTip.setFont(QFont('SansSerif', 10))    #툴팁에 사용될 폰트와 크기 설정 #(폰트: 'SansSerif', 크기: 10px)
      #setToolTip() 메서드: 표시될 텍스트를 입력
      btn.setToolTip('This is a <b>Quit</b> Button')    #버튼 설명
      self.setToolTip('This is a <b>QWidget</b> widget')    #위젯 설명


      self.setWindowTitle('Quit Button')
      self.setGeometry(300, 300, 300, 200)
      self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

