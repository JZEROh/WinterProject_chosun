import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtCore
import json
import os
import camera
from cv2 import *
import cryptoCode as CD


form_secondwindow = uic.loadUiType("save_info_v2.ui")[0]

class secondwindow(QDialog, QWidget, form_secondwindow):
    def __init__(self):
        super(secondwindow, self).__init__()
        self.initUI()
        self.show()
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
    def initUI(self):
        self.setupUi(self)
        
    def copy_text(self):
        global name
        global user_id
        global user_pw
        
        #save info of user
        name = self.lineEdit_name.text()
        user_id = self.lineEdit_id.text()
        user_pw = CD.encrypt(self.lineEdit_password.text(),user_id)
        
    def Home(self):
        self.close()
        
    def save_data(self):
        self.copy_text()
        
        cam = camera.VideoCamera()
        while True:
            frame = cam.get_frame()

            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                ad = './knowns/' + name + '.jpg'
                imwrite(ad, frame)
                break

        cv2.destroyAllWindows()

        data = { name : { "ID": user_id, "PW": user_pw }}
        file_path = "./Client.json"
    
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file)