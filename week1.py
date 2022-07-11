### 창 띄우기

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget


# class MyApp(QWidget):   #MyApp 클래스 선언 #QWidget 부모클래스 상속 #타이틀, 위치, 위젯 크기 설정

#     def __init__(self): 
#         super().__init__()      #다른 클래스의 속성 및 메소드 사용이 가능
#         self.initUI()   #UI 정의

#     def initUI(self):   #인터페이스 초기화 함수
#         self.setWindowTitle('My First Application')     #타이틀바에 나타나는 창의 제목을 설정
#         self.move(300, 300)     #위젯을 스크린의 x=300px, y=300px 위치로 이동
#         self.resize(400, 200)   #위젯의 크기를 너비 400px, 높이 200px로 조절
#         self.show()     #위젯을 스크린에 보여줌


# if __name__ == '__main__':      #'__name__'은 현재 모듈의 이름이 저장되는 내장 변수
#    app = QApplication(sys.argv)     #어플리케이션 객체 생성   #sys: 시스템 관련 기능을 제공하는 라이브러리 / argv: argument(값)
#    ex = MyApp()     # MyApp 클래스 객체 생성
#    sys.exit(app.exec_())     #GUI 이벤트를 핸들링 하기 위해 메인 루프 생성 (*루프: 무한반복) #메인 루프 종료시 프로그램 종료


### 타이틀 및 아이콘 설정
### mac에서는 아이콘 변화 없음 ㅠㅠ

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon   #QtGui : 어플리케이션의 그래픽, 이미지, 텍스트 등을 관리하는 모듈


class MyApp(QWidget):

  def __init__(self):
      super().__init__()
      self.initUI()

  def initUI(self):
      self.setWindowTitle('Icon')
      self.setWindowIcon(QIcon('./week2/gccd_logo.png'))    #어플리케이션 아이콘을 설정
      self.setGeometry(300, 300, 300, 200)  #move()와 resize() 메서드를 하나로 합쳐놓은 것 #(x, y, width, height)
      self.show()


if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())

