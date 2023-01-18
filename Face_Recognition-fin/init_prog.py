import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from secondwindow import secondwindow
import face_recognition
import cv2
import camera
import os
import numpy as np
import Celenium
import face_recog
import glob
import pyautogui
import cryptoCode

form_main = uic.loadUiType("FaceID_UI.ui")[0]

class MainWindow(QMainWindow, form_main):
    def __init__(self) :
        super().__init__()
        self.initUI()
        self.show()
    
    def initUI(self):
        self.setupUi(self)
        
    def button_Save(self):
        self.hide()
        self.second = secondwindow()
        self.second.exec()
        self.show()
        
    def face_recog(self):
        exec(open("face_recog.py").read())
        
    def button_Terminate(self):
        os.remove("./Client.json")
        [os.remove(picture) for picture in glob.glob("./knowns/*.jpg")]
        
    def exit(self):
        # pyautogui.hotkey('alt','tab')
        # pyautogui.hotkey('ctrl','w')
        Celenium.Logout()
        self.close()
    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 

    myWindow = MainWindow()
    
    myWindow.show()

    app.exec_()