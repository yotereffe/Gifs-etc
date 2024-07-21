from PyQt6 import QtCore,QtGui,QtWidgets
import sys
from Raiz import raiz
class Menu(raiz.Fotos):
       def fotos(self):
              super().__init__()
              self.app1=QtWidgets.QMainWindow()
              self.coninfos(self.app1)
              self.app1.show()
       def style(self):
              
              self.central.setStyleSheet('''
              QPushButton{
              border-width:5px;
              border-color:black;
              border-style: outset;
              background-color:white;
              }''')
       def conbutton(self):
              self.buttons={QtGui.QIcon('e:\\gifs\\Menu visual\\infos.png'):QtWidgets.QPushButton(self.central),
                            QtGui.QIcon('e:\\gifs\\Menu visual\\games.png'):QtWidgets.QPushButton(self.central)}
              y=20
              for icon,button in self.buttons.items():
                     button.setGeometry(QtCore.QRect(10,y,340,80))
                     button.setIconSize(QtCore.QSize(330,75))
                     y+=120
                     button.setIcon(icon)
                     button.clicked.connect(lambda:self.fotos())
       def conlabel(self):
              self.inicio=QtWidgets.QLabel(self.central)
              self.inicio.setPixmap(QtGui.QPixmap('e:\\gifs\\Menu visual\\HELLO.png'))
              self.inicio.setGeometry(QtCore.QRect(0,0,1000,800))
              self.inicio.setScaledContents(True)
       def Menuapp(self,main):

              main.setGeometry(QtCore.QRect(0,0,1000,800))
              self.central=QtWidgets.QWidget()
              main.setMinimumSize(QtCore.QSize(750,500))
              main.setMaximumSize(QtCore.QSize(1000,800))              
              self.conlabel()
              self.style()
              self.conbutton()
              main.setCentralWidget(self.central)

if __name__ == '__main__':
      app=QtWidgets.QApplication(sys.argv)
      app2=QtWidgets.QMainWindow()
      app3=Menu()
      app3.Menuapp(app2)
      app2.show()
      sys.exit(app.exec())