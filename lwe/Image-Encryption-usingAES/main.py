# Import required PyQt5 modules
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# Import specific components from PyQt5
from PyQt5.QtWidgets import QFileDialog, QLabel, QAction, QMainWindow, QApplication

# Import loadUiType function from PyQt5.uic module
from PyQt5.uic import loadUiType

# Import Encrypter and Decrypter classes from custom modules
from Encrypter import Encrypter
from Decrypter import Decrypter

# Import Image module from PIL (Python Imaging Library)
from PIL import Image as Img

# Import ImageTk module from PIL (Python Imaging Library) as ImgTk
from PIL import ImageTk as ImgTk

# Import base64 module for encoding and decoding binary data
import base64

# Import AES module from Crypto.Cipher module for AES encryption
from Crypto.Cipher import AES

# Import os and sys modules
import os
import sys

# Import Qt enumeration Qt from QtCore module
Qt = QtCore.Qt

# Load UI file
ui, _ = loadUiType('ui.ui')

# Function to start the application
def start():
    global m
    m = Main_Window()
    m.show()

# Class for the encryption page
class encrypt_page():
    def __init__(self):
        # Initialize variables
        self.file = {}
        self.stri = ""
        
        # Connect signals to slots
        self.Handel_Buttons()
        self.pushButton_3.clicked.connect(self.chooseFile)
        self.pushButton_4.clicked.connect(self.onClickEncrypt)
        
    # Method to handle buttons
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        
    # Method to choose file for encryption
    def chooseFile(self):
        self.file = QFileDialog.getOpenFileName(self, 'Open File')
        pixmap = QtGui.QPixmap(self.file[0])
        self.lbl.setPixmap(pixmap.scaledToHeight(201))
        if self.file != None:
            ba = QtCore.QByteArray()
            buff = QtCore.QBuffer(ba)
            buff.open(QtCore.QIODevice.WriteOnly) 
            ok = pixmap.save(buff, "PNG")
            assert ok
            pixmap_bytes = ba.data()
            self.stri = base64.b64encode(pixmap_bytes)
        
    # Method to encrypt the chosen file
    def onClickEncrypt(self):
        myKey = self.lineEdit.text()
        x = Encrypter(self.stri, myKey)
        cipher = x.encrypt_image()
        fh = open("cipher.txt", "wb")
        fh.write(cipher)
        fh.close()

# Class for the decryption page
class decrypt_page():
    def __init__(self):
        # Initialize variables
        self.cipher = {}
        
        # Connect signals to slots
        self.Handel_Buttons()
        self.pushButton_5.clicked.connect(self.chooseFile1)
        self.pushButton_6.clicked.connect(self.onClickDecrypt)
        
    # Method to handle buttons
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        
    # Method to choose file for decryption
    def chooseFile1(self):
        file = QFileDialog.getOpenFileName(self, 'Open File')
        text = open(file[0]).read()
        self.cipher = text.encode('utf-8')
        
    # Method to decrypt the chosen file
    def onClickDecrypt(self):
        myKey = self.lineEdit_2.text()
        x = Decrypter(self.cipher)
        image = x.decrypt_image(myKey)
        ba = QtCore.QByteArray(image)
        pixmap = QtGui.QPixmap()
        ok = pixmap.loadFromData(ba, "PNG")
        assert ok        
        self.lbl_2.setPixmap(pixmap.scaledToHeight(201))

# Main window class
class Main_Window(QMainWindow, QWidget, ui, encrypt_page, decrypt_page):
    def __init__(self):
        QMainWindow.__init__(self)
        QWidget.__init__(self)
        
        # Set up the UI
        self.setupUi(self)
        
        # Initialize encryption and decryption pages
        encrypt_page.__init__(self)
        decrypt_page.__init__(self)
        
        # Connect signals to slots
        self.Handel_Buttons() 
        self.stackedWidget.setCurrentIndex(0)
        
    # Method to handle buttons
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_8.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_7.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
                
if __name__ == '__main__':
    # Create an instance of QApplication
    app = QApplication(sys.argv)
    
    # Start the application
    window = start()
    
    # Execute the application event loop
    app.exec_()
