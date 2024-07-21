import os
from PyQt6.QtWidgets import QLabel,QPushButton,QTreeWidget,QWidget,QTreeWidgetItem,QLineEdit
from PyQt6.QtCore import QRect,Qt,QSize
from PyQt6.QtGui import QMovie,QPixmap,QFont
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
class Fotos():
        def prinds(self,img):
                imgs=img.parent()
                try:
                        if img.text(0)[-4:]  in ['.jpg','.png','jpeg']:
                                self.nome.setText(f'<center>{imgs.text(0)}<center>')         
                                self.fundo.setPixmap(QPixmap(f'E:\\GIFS fotos e videos\\{imgs.text(0)}\\{img.text(0)}'))
                        elif img.text(0)[-4:] in'.gif':
                                self.nome.setText(f'<center>{imgs.text(0)}<center>')
                                gif=QMovie(f'E:\\GIFS fotos e videos\\{imgs.text(0)}\\{img.text(0)}')
                                self.fundo.setMovie(gif)
                                gif.start()
                        else: 
                                if imgs.text(0):
                                        pass
                                else:
                                        self.nome.setText(f'<center>{img.text(0)}<center>')
                                        self.fundo.setPixmap(QPixmap('e:\\gifs\\Raiz\\Fundo Fotos\\Sorry.png'))
                except:
                        pass
        def twitter(self,dados='None'):
                web=webdriver.Chrome()
                if self.twitdrip.text():
                        web.get(f'https://x.com/{self.twitdrip.text()}')        
                else:        
                        web.get(f'https://x.com/{dados}') 
                while True:
                        try:
                                self.html=BeautifulSoup(web.page_source,'lxml')
                                try:
                                        i=self.html.find('div',attrs={'class':'css-146c3p1 r-bcqeeo r-qvutc0 r-37j5jr r-fdjqy7 r-1yjpyg1 r-ueyrd6 r-1vr29t4 r-5oul0u'})
                                        if i.text=='Conta suspensa':
                                                
                                                break
                                except:
                                        pass

                                i=self.html.find('div',attrs={'class':'css-146c3p1 r-dnmrzs r-1udh08x r-3s2u2q r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-a023e6 r-rjixqe r-16dba41 r-18u37iz r-1wvb978'})
                                i.text
                                osa=self.html.find('div',attrs={'class':'css-146c3p1 r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-adyw6z r-135wba7 r-b88u0q r-1awozwy r-6koalj r-1udh08x r-3s2u2q'})
                                osa.text
                                p=self.html.find('div',attrs={'class':'css-146c3p1 r-dnmrzs r-1udh08x r-3s2u2q r-bcqeeo r-1ttztb7 r-qvutc0 r-37j5jr r-n6v787 r-1cwl3u0 r-16dba41'})
                                p.text
                                break
                        except:
                                pass
                print('twiteer infos:',i.text,osa.text,p.text)
                web.get(f'https://rule34.xxx/index.php?page=post&s=list&tags={dados.replace('@','')}')
                while True:
                        try:
                                self.html=BeautifulSoup(web.page_source,'lxml')
                                try:  
                                        i=self.html.find('div',attrs={'class':'content'}).h1.text
                                        break
                                except:
                                        pass    
                                i=self.html.find('li',attrs={'class':'tag-type-artist'})
                                
                                break
                        except :
                                pass
                print('rule post:',i)                
                web.get(f'https://www.patreon.com/user?u={dados.replace('@','')}')
                while True:
                        try:
                                self.html=BeautifulSoup(web.page_source,'lxml')     
                                i=self.html.find('ul',attrs={'class':'sc-1b5vbhn-5 RzWue'})
                                break
                        except:
                                pass
                        
                
        def op(self):
                print('afsfsa')
        def coninfos(self,main):
                main.setGeometry(QRect(0,0,1325,750))
                main.setMaximumSize(QSize(1325,750))
                self.central=QWidget()
                self.central.setStyleSheet(''' 
                                        QWidget{
                                           background-color:#3b219d
                                      }
                                        QTreeWidget{
                                           background-color:white;
                                           border:5px solid black;}
                                           QPushButton{
                                           border:5px solid black;
                                           background-color:white
                                           }
                                        QLineEdit{
                                           background-color:white;
                                           padding-right:10px;}''')
 
                self.fundo=QLabel(self.central)
                self.fundo.setGeometry(QRect(150,0,650,750))
                self.fundo.setPixmap(QPixmap('e:\\gifs\\Raiz\\Fundo Fotos\\fundo.png' ))
                self.fundo.setStyleSheet('''border:15px solid black;background-color:white''')
                self.fundo.setScaledContents(True)
                self.buttons=[QPushButton(self.central),QPushButton(self.central),QPushButton(self.central)]
                try:
                        self.buttons[0].clicked.connect(lambda: self.twitter(self.lista.currentItem().text(0)))
                except:
                        pass
                self.font=QFont()
                self.font.setPointSize(15)
                self.font.setFamily('Arial')
                self.twitdrip=QLineEdit(self.central)
                self.twitdrip.setGeometry(QRect(800,150,200,35))
                self.twitdrip.setFont(self.font)
                self.twitnik=QLabel(self.central)
                self.twitnik.setGeometry(QRect(800,250,150,35))
                self.twitdvalor=QLabel(self.central)
                self.twitdvalor.setGeometry(QRect(800,350,150,35))
                self.nome=QLabel(self.central)
                self.nome.setText('<center>none<center>')
                self.font.setPointSize(50)
                self.nome.setStyleSheet('border:5px solid black;padding-top:25px;')
                self.nome.setFont(self.font)
                self.nome.setGeometry(800,0,525,150)
                
                x=800
                for button in self.buttons:
                        button.setGeometry(QRect(x,600,175,150))
                        x+=175
                self.lista=QTreeWidget(self.central)
                for name in os.listdir('E:\\GIFS fotos e videos'):
                        namea=QTreeWidgetItem([name])
                        for dir,root,files in os.walk(f'E:\\GIFS fotos e videos\\{name}'):
                                for num,file in enumerate(files):
                                        filea=QTreeWidgetItem([file])
                                        namea.setTextAlignment(0,Qt.AlignmentFlag.AlignCenter)
                                        namea.addChild(filea)
                        self.lista.addTopLevelItem(namea)
                self.lista.doubleClicked.connect(lambda: self.prinds(self.lista.currentItem()))              
                self.lista.setHeaderLabel('Nome')
                self.lista.header().setDefaultAlignment(Qt.AlignmentFlag.AlignCenter)
                self.lista.setGeometry(QRect(0,0,150,750)) 
                main.setCentralWidget(self.central)