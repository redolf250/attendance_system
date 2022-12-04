import datetime
import time
import winsound
import cv2
import numpy as np
import pyshine as ps
from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import (Qt, QTimer)
from PySide2.QtGui import (QColor, QPixmap, QImage)
from PySide2.QtWidgets import *
from cv2 import VideoCapture

from pyzbar.pyzbar import *
from datetime import datetime as dt
import mysql.connector as connector

from alert.alert_dialog import *
from exit_camera.ui_exit_camera import Ui_Dialog

try:
    db = connector.connect(
        host="localhost",
        user = "root",
        passwd = "0552588647",
        database = "students"
        )
    my_cursor =db.cursor()
    print("Connected to database")
except:
    print("Could not connect to database")

class ExitCameraFeed(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui_exit_camera = Ui_Dialog()
        self.ui_exit_camera.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui_exit_camera.btn_close.clicked.connect(self.close)
        self.ui_exit_camera.btn_minimize.clicked.connect(self.showMinimized)
        self.fps = 0
        ##########################################################################################
        # self.ui_exit_camera.exit_comboBox.addItems([str(x) for x in return_active_cameras(3)])
        self.ui_exit_camera.btn_exit_cam_connect.clicked.connect(self.start_webcam)
        self.ui_exit_camera.btn_exit_cam_disconect.clicked.connect(self.stop_webcam)
        ##########################################################################################

        ############################################################################################
        self.ui_exit_camera.brigthness.valueChanged.connect(self.update_brigthness)
        self.ui_exit_camera.sharpness.valueChanged.connect(self.update_sharpness)
        self.ui_exit_camera.contrast.valueChanged.connect(self.update_contrast)
        self.ui_exit_camera.hsv.valueChanged.connect(self.update_average_blurring)

        self.ui_exit_camera.brigthness_value.setText(str(self.ui_exit_camera.brigthness.value()))
        self.ui_exit_camera.sharpness_value.setText(str(self.ui_exit_camera.sharpness.value()))
        self.ui_exit_camera.contrast_value.setText(str(self.ui_exit_camera.contrast.value()))

        self.ui_exit_camera.hsv_value.setText(str(self.ui_exit_camera.hsv.value()))
        ###########################################################################################

        self.ui_exit_camera.frame.mouseMoveEvent = self.MoveWindow

        ##########################################################################################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(144, 144, 144, 40))
        self.ui_exit_camera.frame.setGraphicsEffect(self.shadow)
        ##########################################################################################
        
    
    #################################################################################
    def MoveWindow(self, event):
        if self.isMaximized() == False:
            self.move(self.pos() + event.globalPos() - self.clickPosition)
            self.clickPosition = event.globalPos()
            event.accept()
            pass

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()
        pass
    ###################################################################################

    ###################################################################################
    def update_brigthness(self, value):
        self.ui_exit_camera.brigthness_value.setText(str(value))
    
    def update_sharpness(self, value):
        self.ui_exit_camera.sharpness_value.setText(str(value))
        
    def update_contrast(self, value):
        self.ui_exit_camera.contrast_value.setText(str(value))

    def update_average_blurring(self, value):
        self.ui_exit_camera.hsv_value.setText(str(value))
    ###################################################################################
    

    def log_student_out(self,reference:str):
        cursor=my_cursor.execute("SELECT id,reference FROM tb_students WHERE reference= " +reference)
        cursor= my_cursor.fetchone()
        db.commit()
        results = []
        if cursor:
            for data in cursor:
                results.append(data)
        cursor=my_cursor.execute("SELECT time_in,time_out,duration FROM tb_attendance WHERE st_reference=%s and date_stamp=%s ",(str(results[1]),dt.now().date().strftime("%Y-%m-%d")))
        cursor=my_cursor.fetchall()
        db.commit()
        details = []
        if cursor:
            for data in cursor:
                details.append(data)  
        if details:
            time_out =dt.now().time().strftime('%H:%M:%S')
            time_out_split = str(time_out).split(':')
            time_in = str(details[0][0]).split(':')
            print(time_in)
            construct_duration = (abs((int(time_out_split[0])-int(time_in[0]))),
            abs((int(time_out_split[1])-int(time_in[1]))),
            abs((int(time_out_split[2])-int(time_in[2]))))
            new_duration = str(str(construct_duration[0])+':'+str(construct_duration[1])+':'+str(construct_duration[2]))
            if str(details[0][2]) == "00:00:00":
                my_cursor.execute("UPDATE tb_attendance SET time_out=%s, duration=%s  WHERE st_reference=%s and date_stamp=%s ",(time_out,new_duration,reference,dt.now().date().strftime('%Y-%m-%d')))
                db.commit()
                print(new_duration)
                return "Hey! have successfully logged out"
            else:
                return "Oops! you are already logged out!"
        else:
            return "Oops! student details not found."

    def start_webcam(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui_exit_camera.exit_cam_ip.text()
        system_attached_camera = self.ui_exit_camera.exit_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(3)

    def create_alert(self):
        self.stop_webcam
        self.show_alert = AlertDialog() 
        self.show_alert.show()

    def update_frame(self): 
        thickness = 2
        rect_thickness = 1
        color = (255,255,0)
        # fps = int(fps * 1000)
        # print("fps: ", fps)
        
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)

        self.beta = int(self.ui_exit_camera.brigthness_value.text())
        self.apha = int(self.ui_exit_camera.contrast_value.text())*0.01
        self.kernel = (int(self.ui_exit_camera.sharpness_value.text())*0.01, int(self.ui_exit_camera.sharpness_value.text())*0.01)
        self.frame = cv2.filter2D(self.frame,-1, self.kernel)
        self.result = cv2.addWeighted(self.frame,self.apha, np.zeros(self.frame.shape, self.frame.dtype), 0, self.beta)
        self.text = str(time.strftime("%H:%M %p"))
        ps.putBText(self.result,self.text,text_offset_x=self.result.shape[1]-90,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(228,20,222),text_RGB=(255,255,255))
        self.date = datetime.datetime.now() 
        self.date = self.date.strftime("%a, %b %d, %Y")
        ps.putBText(self.result,self.date,text_offset_x=10,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(10,20,222),text_RGB=(255,255,255))

        if self.ui_exit_camera.face_auth.isChecked():
            self.display_feed(self.result,1)

        elif self.ui_exit_camera.qr_code_auth.isChecked():
            for qr_code in decode(self.result):
                qr_code_data  = qr_code.data.decode('utf-8')
                pts = np.array([qr_code.polygon], np.int)
                rect = np.array([qr_code.rect], np.int)
                pts = pts.reshape((-1, 1, 2)) 
                data = str(qr_code_data)
                # cv2.polylines(frame, [pts], True,color,1)
                for x,y,w,h in rect:
                    w , h =x+w, y+h
                    cv2.rectangle(self.result, (x,y), (w,h), color, rect_thickness)
                    cv2.line(self.result,(x,y),(x+15,y),color,thickness)
                    cv2.line(self.result,(x,y),(x,y+15),color,thickness)
                    cv2.line(self.result,(w,y),(w-15,y),color,thickness)
                    cv2.line(self.result,(w,y),(w,y+15),color,thickness)
                    cv2.line(self.result,(x,h),(x+15,h),color,thickness)
                    cv2.line(self.result,(x,h),(x,h-15),color,thickness)
                    cv2.line(self.result,(w,h),(w-15,h),color,thickness)
                    cv2.line(self.result,(w,h),(w,h-15),color,thickness)
                time.sleep(0.1) 
                n=self.log_student_out(str(data))
                print(n)
                winsound.Beep(1000,100)    
            self.display_feed(self.result,1)          
        elif self.ui_exit_camera.biometric_auth.isChecked():
            print("Starting biometric authentication!")

    def display_feed(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        procesedImage = procesedImage.rgbSwapped()
        if window == 1:
            self.ui_exit_camera.camera_feeds.setPixmap(QPixmap.fromImage(procesedImage))
            self.ui_exit_camera.camera_feeds.setScaledContents(True)
        
    def stop_webcam(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui_exit_camera.camera_feeds.setPixmap(QPixmap())
        self.ui_exit_camera.camera_feeds.setAlignment(Qt.AlignCenter)
        self.timer.stop()
    #############################################################################################