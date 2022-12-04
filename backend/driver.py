################################################################################
##
## BY: Asamani Redolf
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
################################################################################
import os
import sys
import cv2
import time
import winsound
import numpy as np

import pyshine as ps
import face_recognition
from pyzbar.pyzbar import *
from datetime import datetime as dt

from PySide2 import QtCore
from PySide2.QtWidgets import *
from PySide2.QtCore import (QPoint,Qt, QTimer)
from PySide2.QtGui import (QColor, QPixmap, QImage)

from report.piechart.piechart.piechart import Canvas
from report.piechart.barchart.barchart import Barchart


from model.student import Student
from model.attendance import Attendance
import mysql.connector as connector

from launcher.ui_launcher import Ui_MainWindow
from camera_one.ui_surveillance_cam_one import *
from camera_two.surveillance_camera_two import *
from dashboard.ui_dashoboard import Ui_dashboard
from camera_four.surveillance_camera_four import * 
from exit_camera.exit_camera import ExitCameraFeed
from camera_three.surveillance_camera_three import * 
from camera_one.surveillance_camera_one import Surveilliance_One



## ==> GLOBALS
GLOBAL_STATE = 0
counter = 0

path = "test_code\\images"
images = []
image_list = os.listdir(path)

def get_names(images: list, image_list: list, path: str):
    names = []
    for item in image_list:
        current_image = cv2.imread(f'{path}/{item}')
        images.append(current_image)
        names.append(os.path.splitext(item)[0])
    return names

name_list = get_names(images, image_list, path)

def get_encodings(images):
    encodings_list = []
    for image in images:
        cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encode_face = face_recognition.face_encodings(image)[0]
        encodings_list.append(encode_face)
    return encodings_list

encode_list=get_encodings(images)

def mark_attendance(name):
    with open(r'test_code\\attendance.csv', 'r+') as f:
        data = f.readlines()
        namelist = []
        for line in data:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = dt.now()
            h = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{h}')

def load_face_images_from_db(path:str,table_name:str):
    cursor=my_cursor.execute("SELECT st_reference,image from "+table_name)
    cursor= my_cursor.fetchall()
    image_data = []
    if cursor:
        for data in cursor:
            image_data.append(data)
            with open(path+str(data[0])+'.jpeg','wb') as f:
                f.write(data[1])
        db.commit()

db = connector.connect(
        host="localhost",
        user = "root",
        passwd = "0552588647",
        database = "students"
        )
my_cursor =db.cursor()

class MainWindow(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui = Ui_dashboard()
        self.saveTimer = QTimer()
        self.ui.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.oldPosition = self.pos()
        #########################################################################################
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        qtRectangle = self.frameGeometry()
        centerPoint =QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        #########################################################################################


        #########################################################################################
        self.ui.btn_close.clicked.connect(self.close)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.btn_maximize.clicked.connect(self.maximize_restore)
        self.ui.btn_clear_label.clicked.connect(self.loadUi_file)
        #########################################################################################

        #########################################################################################################
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home))
        self.ui.btn_search.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.search))
        self.ui.btn_camera.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.camera))
        self.ui.btn_database.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.database))
        self.ui.btn_help.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings))
        self.ui.btn_report.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.report))
        ##########################################################################################################

        #########################################################################################################
        self.canvas = Canvas()
        self.ui.plot_area.setPixmap(QPixmap.fromImage(r'backend\\report\\piechart\\piechart\\pie.png'))
        self.ui.plot_area.setScaledContents(True)

        self.barchart = Barchart()
        self.ui.plot_area_2.setPixmap(QPixmap.fromImage(r'backend\\report\\piechart\\barchart\\bar.png'))
        self.ui.plot_area_2.setScaledContents(True)

        ########################################################################################################

        #########################################################################################
        self.open_exit_camera = ExitCameraFeed()
        self.ui.btn_open_exit_camera_ui.clicked.connect(lambda: self.open_exit_camera.show())
        ############################################################################################

        ############################################################################################
        self.open_surveillance_camera_one = Surveilliance_One()
        self.ui.btn_cast_cam_one.clicked.connect(lambda: self.open_surveillance_camera_one.show())

        self.surveillance_camera_two = Surveilliance_Two()
        self.ui.btn_cast_cam_one_2.clicked.connect(lambda: self.surveillance_camera_two.show())

        self.surveillance_camera_three = Surveilliance_Three()
        self.ui.btn_cast_cam_three.clicked.connect(lambda: self.surveillance_camera_three.show())

        self.surveillance_camera_four = Surveilliance_Four()
        self.ui.btn_cast_cam_four.clicked.connect(lambda: self.surveillance_camera_four.show())
        ############################################################################################

        ############################################################################################
        self.ui.btn_connect_detect.clicked.connect(self.start_webcam)
        self.ui.btn_disconnect.clicked.connect(self.stop_webcam)
        ############################################################################################

        #############################################################################################
        self.ui.btn_search_page.clicked.connect(self.get_student_details_summary)
        self.ui.calendarWidget.selectionChanged.connect(self.get_date)
        self.ui.calendarWidget_report.selectionChanged.connect(self.get_report_start_date)
        self.ui.calendarWidget_report_2.selectionChanged.connect(self.get_report_end_date)
        self.ui.btn_reload.clicked.connect(self.clear_fields)
        self.ui.btn_save.clicked.connect(self.save_report)
        ##############################################################################################

        ##############################################################################################
        self.ui.btn_search_reg.clicked.connect(self.registeration_search)
        self.ui.calendarWidget_reg.selectionChanged.connect(self.get_registration_start_date)
        self.ui.calendarWidget_reg_2.selectionChanged.connect(self.get_registration_end_date)
        self.ui.btn_register.clicked.connect(self.register_student)
        self.ui.btn_clear.clicked.connect(self.resets_fileds)
        self.ui.btn_update.clicked.connect(self.update_student)
        self.ui.btn_remove.clicked.connect(self.remove_student)
        self.ui.btn_browse_reg.clicked.connect(self.browse_image_files)
        self.ui.btn_browse_file_1.clicked.connect(self.browse_fingerprint_one)
        self.ui.btn_browse_3.clicked.connect(self.browse_fingerprint_two)
        self.ui.btn_run_check.clicked.connect(self.run_check)
        ##############################################################################################

        ###############################################################################################
        self.ui.dilation.valueChanged.connect(self.update_guasian_blur)
        self.ui.erosion.valueChanged.connect(self.update_median_blur)
        self.ui.threshold.valueChanged.connect(self.update_threshold)
        self.ui.brigthness.valueChanged.connect(self.update_brigthness)
        self.ui.average_blur.valueChanged.connect(self.update_average_blurring)
        self.ui.sharpness.valueChanged.connect(self.update_sharpness)
        self.ui.contrast.valueChanged.connect(self.update_contrast)
        self.ui.kernel.valueChanged.connect(self.update_kernel)
        self.ui.confidence_level_1.valueChanged.connect(self.update_check)

        self.ui.hsv_value.setText(str(self.ui.brigthness.value()))
        self.ui.gb_blur_value.setText(str(self.ui.sharpness.value()))
        self.ui.bb_blur_value.setText(str(self.ui.contrast.value()))
        self.ui.dilation_value.setText(str(self.ui.dilation.value()))
        self.ui.erosion_value.setText(str(self.ui.erosion.value()))
        self.ui.avg_blur_value.setText(str(self.ui.average_blur.value()))
        self.ui.thresh_value.setText(str(self.ui.threshold.value()))
        self.ui.kernel_value.setText(str(self.ui.kernel.value()))
        self.ui.score.setText(str(self.ui.confidence_level_1.value()))
        ##################################################################################################

        #################################################################################################
        self.ui.btn_camera_one_connect.clicked.connect(self.start_webcam_cam_one)
        self.ui.btn_camera_one_disconnect.clicked.connect(self.stop_webcam_cam_one)
        # self.ui.camera_one_comboBox.addItems(return_active_cameras(3))

        self.ui.btn_camera_two_connect.clicked.connect(self.start_webcam_cam_two)
        self.ui.btn_camera_two_disconnect.clicked.connect(self.stop_webcam_cam_two)
        # self.ui.camera_two_comboBox.addItems(return_active_cameras(3))

        self.ui.btn_camera_three_connect.clicked.connect(self.start_webcam_cam_three)
        self.ui.btn_camera_three_disconnect.clicked.connect(self.stop_webcam_cam_three)
        # self.ui.camera_two_comboBox.addItems(return_active_cameras(3))

        self.ui.btn_camera_four_connect.clicked.connect(self.start_webcam_cam_four)
        self.ui.btn_camera_four_disconnect.clicked.connect(self.stop_webcam_cam_four)
        # self.ui.camera_two_comboBox.addItems(return_active_cameras(3))
        ##################################################################################################

        ##################################################################################################
        for w in self.ui.frame.findChildren(QPushButton):
            w.clicked.connect(self.applyStyle)
        load_face_images_from_db(r'backend\\images\\face_images\\',"tb_images") 
        ##################################################################################################
        

    def get_student_details_summary(self):
        if self.ui.search_box.text() == "":
            cursor = my_cursor.execute("SELECT * FROM tb_attendance")
            cursor = my_cursor.fetchall()
            details = []
            if cursor:
                for item in cursor:
                    details.append(item)
                db.commit()
            self.ui.tableWidget.setRowCount(len(details))
            self.ui.tableWidget.setTabKeyNavigation(True)
            self.ui.tableWidget.setColumnWidth(1,230)
            self.ui.tableWidget.setAutoScroll(True)
            self.ui.tableWidget.setAutoScrollMargin(2)

            row_count = 0
            for data in details:
                self.ui.tableWidget.setItem(row_count,1,QtWidgets.QTableWidgetItem(str(data[1])))
                self.ui.tableWidget.setItem(row_count,2,QtWidgets.QTableWidgetItem(str(data[2])))
                self.ui.tableWidget.setItem(row_count,3,QtWidgets.QTableWidgetItem(str(data[3])))
                self.ui.tableWidget.setItem(row_count,4,QtWidgets.QTableWidgetItem(str(data[4])))
                self.ui.tableWidget.setItem(row_count,5,QtWidgets.QTableWidgetItem(str(data[5])))
                self.ui.tableWidget.setItem(row_count,0,QtWidgets.QTableWidgetItem(str(data[6])))
                row_count = row_count+1
                pass   
        else:
            pass
       

    def get_date(self):
        date = self.ui.calendarWidget.selectedDate()
        if self.ui.start_date.isChecked():
            self.ui.db_start_date.setText(str(date.toPython()))
        elif self.ui.end_date.isChecked():
            self.ui.db_end_date.setText(str(date.toPython()))

    def clear_fields(self):
        self.ui.db_firstname.setText("")
        self.ui.db_middlename.setText("")
        self.ui.db_lastname.setText("")
        self.ui.db_college.setText("")
        self.ui.db_refrence.setText("")
        self.ui.db_index.setText("")
        self.ui.db_nationality.setText("")
        self.ui.db_programe.setText("")
        self.ui.db_validity.setText("")
        self.ui.db_year.setText("")
        pass

    def get_report_start_date(self):
        date =self.ui.calendarWidget_report.selectedDate()
        self.ui.report_start_date.setText(str(date.toPython()))
    
    def get_report_start_date(self):
        date =self.ui.calendarWidget_report.selectedDate()
        self.ui.report_start_date.setText(str(date.toPython()))

    def get_report_end_date(self):
        date =self.ui.calendarWidget_report_2.selectedDate()
        self.ui.report_end_date.setText(str(date.toPython()))

    def filename(self):
        if self.ui.file_name is None:
            return False
        return self.ui.file_name.text()

    def save_report(self):
        print(self.filename())   


    def registeration_search(self):
        reference = self.ui.search_reg.text()
        return reference

    def get_registration_start_date(self):
        date = self.ui.calendarWidget_reg.selectedDate()
        self.ui.reg_start_date.setText(str(date.toPython()))

    def get_registration_end_date(self):
        date = self.ui.calendarWidget_reg_2.selectedDate()
        self.ui.reg_end_date.setText(str(date.toPython()))

    def insert_face_image(self, student):
        if self.ui.image_file_reg.text(): 
            with open(self.ui.image_file_reg.text(), 'rb') as image:
                data = image.read()
                my_cursor.execute("INSERT INTO tb_images(st_reference,image) VALUES(%s,%s)",(student,data))
                db.commit()
                self.alert_builder("Hey! Student data saved successfully.")
        else:
            self.alert_builder("Oops! select image file.")

    def insert_biometric_image(self,student):
        if self.ui.image_file_1.text():   
            with open(self.ui.image_file_1.text(), 'rb') as image:
                data = image.read()
                my_cursor.execute("INSERT INTO tb_biometric_images(st_reference,image) VALUES(%s,%s)",(student.reference,data))
                db.commit()
                self.alert_builder("Hey! Student data saved successfully.")
        else:
            self.alert_builder("Oops! select image file.")

    def register_student(self):    
        if self.ui.reg_student_ref.text() and self.ui.reg_student_ref.text():
            student = Student(
                int(self.ui.reg_student_ref.text()),
                int(self.ui.reg_index.text()),
                self.ui.reg_firstname.text()+" "+self.ui.reg_middlename.text(),
                self.ui.reg_lastname.text(),
                self.ui.reg_college_2.currentText(),
                self.ui.reg_programs.currentText(),
                self.ui.reg_nationality.text(),
                self.ui.reg_start_date.text(),
                self.ui.reg_end_date.text(),
            )
            if self.ui.reg_face_auth.isChecked() and self.ui.image_file_reg.text():
                my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date))
                db.commit()   
                self.insert_face_image(student.reference)
                self.show_alert = AlertDialog()
                self.show_alert.content("Student registered successfully")  
                self.show_alert.show()
            elif self.ui.reg_biometric_auth.isChecked() and self.ui.image_file_1.text():
                my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date))
                db.commit()
                self.insert_biometric_image(student.reference)
                self.show_alert = AlertDialog()
                self.show_alert.content("Student registered successfully")  
                self.show_alert.show()
            elif self.ui.reg_both.isChecked() and self.ui.image_file_reg.text() and self.ui.image_file_1.text():
                my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date))
                db.commit()
                self.insert_face_image(student.reference)
                self.insert_biometric_image(student.reference)
                self.show_alert = AlertDialog()
                self.show_alert.content("Student registered successfully")  
                self.show_alert.show()
            elif self.ui.reg_qr_auth.isChecked():
                my_cursor.execute("INSERT INTO tb_students (reference,index_,firstname,lastname,college,program,nationality,startdate,enddate) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (student.reference,student.index_,student.firstname,student.lastname,student.college,student.program,student.nationality,student.start_date,student.end_date))
                db.commit()
                self.show_alert = AlertDialog()
                self.show_alert.content("Student registered successfully")  
                self.show_alert.show()
        else:
            self.alert_builder("OopS! please input valid data.")

    def alert_builder(self, message:str):
        self.alert = AlertDialog()
        self.alert.content(message)
        self.alert.show()
          
    def fetch_data_from_db(self,reference):
        detail =my_cursor.execute("SELECT * FROM tb_students WHERE reference="+reference)
        detail= my_cursor.fetchone()
        db_data = []
        if detail:
            for data in detail:
                db_data.append(data)
            db.commit()
        return db_data

    def load_image_from_db(self,reference,label):
        cursor=my_cursor.execute("SELECT st_reference,image from tb_images WHERE st_reference="+reference)
        cursor= my_cursor.fetchone()
        image_data = []
        if cursor:
            for data in cursor:
                image_data.append(data)
            db.commit()
            if len(image_data)>0:
                with open(r'backend\\images\\assets\\image.jpeg','wb') as image_file:
                        image_file.write(image_data[1])
            label.setPixmap(QPixmap.fromImage(r'backend\\images\\assets\\image.jpeg'))
            label.setScaledContents(True)
        else:
            label.setPixmap(QPixmap.fromImage(r'backend\\images\\assets\\img.png'))
            label.setScaledContents(True)

    def search_student(self):
            if self.ui.search_reg.text():
                db_data=self.fetch_data_from_db(self.ui.search_reg.text())
                if len(db_data) > 0:
                    helper = str(db_data[3]).split(" ")
                    self.ui.reg_firstname.setText(helper[0])
                    self.ui.reg_middlename.setText(helper[1])
                    self.ui.reg_lastname.setText(db_data[4])
                    self.ui.reg_student_ref.setText(str(db_data[1]))
                    self.ui.reg_index.setText(str(db_data[2]))
                    self.ui.reg_college.setText(db_data[5])
                    self.ui.reg_nationality.setText(db_data[7])
                    self.ui.reg_start_date.setText(db_data[8])
                    self.ui.reg_end_date.setText(db_data[9])
                    self.ui.reg_programs.setCurrentText(db_data[6])
                    self.load_image_from_db(self.ui.search_reg.text(),self.ui.reg_image)
                else:
                    self.alert_builder("Student not found. Please enter\nyour details to register!")
            else:
                self.alert_builder("Oops! search field can't be empty.")

    def update_student(self):
        if self.ui.reg_student_ref.text() and self.ui.image_file_reg.text():
            with open(self.ui.image_file_reg.text(), 'rb') as image:
                data = image.read()
                my_cursor.execute("UPDATE tb_images SET image =%s WHERE st_reference=%s ",(data,self.ui.reg_student_ref.text()))
                db.commit()
            self.alert_builder("Hey! Student image updated successfully.")
        else:
            self.alert_builder("Oops! Something went wrong.")
            
    def remove_student(self):
        try:
            my_cursor.execute("DELETE FROM tb_students where reference="+self.ui.reg_student_ref.text())
            db.commit()
            self.resets_fileds()
            self.alert_builder("Student data removed successfuly!")
        except:
                self.alert_builder("Oops! internal server erro!")

    def resets_fileds(self):
        self.ui.reg_firstname.setText("")
        self.ui.reg_middlename.setText("")
        self.ui.reg_lastname.setText("")
        self.ui.reg_student_ref.setText("")
        self.ui.reg_index.setText("")
        self.ui.reg_college.setText("")
        self.ui.reg_nationality.setText("")
        self.ui.reg_start_date.setText("")
        self.ui.reg_end_date.setText("")
        self.ui.reg_college.setText("")
        self.ui.reg_image.setPixmap("")

    def browse_image_files(self):
        path= QFileDialog.getOpenFileName(self, "Select File","","JPEG Files(*.jpeg);;JPG Files(*.jpg);;PNG Files(*.png)")
        if path:
            self.ui.image_file_reg.setText(path[0])
            self.ui.reg_image.setPixmap(QPixmap.fromImage(path[0]))
            self.ui.reg_image.setScaledContents(True)
            directory_name=os.path.dirname(path[0])
            extract_base= os.path.basename(path[0] )
            get_extention = (extract_base.split('.')[1])
            os.rename(path[0], os.path.join(directory_name,self.ui.reg_student_ref.text()+"."+get_extention))
            file = os.path.join(directory_name,self.ui.reg_student_ref.text()+"."+get_extention)
            file_path = file.replace("\\", "/")
            self.ui.image_file_reg.setText(file_path)
            return file_path

    def browse_fingerprint_one(self):
        path= QFileDialog.getOpenFileName(self, "Select File","","JPEG Files(*.jpeg);;JPG Files(*.jpg);;PNG Files(*.png);;PNG Files(*.bmp)")
        if path:
            self.ui.image_file_1.setText(path[0])
            self.ui.finger_print_1.setPixmap(QPixmap.fromImage(path[0]))
            self.ui.finger_print_1.setScaledContents(True)
            directory_name=os.path.dirname(path[0])
            extract_base= os.path.basename(path[0])
            get_extention = (extract_base.split('.')[1])
            os.rename(path[0], os.path.join(directory_name,self.ui.reg_student_ref.text()+"."+get_extention))
            file = os.path.join(directory_name,self.ui.reg_student_ref.text()+"."+get_extention)
            file_path = file.replace("\\", "/")
            self.ui.image_file_1.setText(file_path)
            return file_path

    def browse_fingerprint_two(self):
        path= QFileDialog.getOpenFileName(self, "Select File","","JPEG Files(*.jpeg);;JPG Files(*.jpg);;PNG Files(*.png);;PNG Files(*.bmp)")
        if path:
            self.ui.image_file_2.setText(path[0])
            self.ui.finger_print_2.setPixmap(QPixmap.fromImage(path[0]))
            self.ui.finger_print_2.setScaledContents(True)
            directory_name=os.path.dirname(path[0])
            extract_base= os.path.basename(path[0])
            get_extention = (extract_base.split('.')[1])
            os.rename(path[0], os.path.join(directory_name,self.ui.reg_student_ref.text()+"."+get_extention))
            file = os.path.join(directory_name,self.ui.reg_student_ref.text()+"."+get_extention)
            file_path = file.replace("\\", "/")
            self.ui.image_file_2.setText(file_path)
            return file_path

    def run_check(self):
        print("Checking...")

    def update_check(self, value):
        self.ui.score.setText(str(value))

    def loadUi_file(self):
        self.ui.firstname.setText("")
        self.ui.middlename.setText("")
        self.ui.lastname.setText("")
        self.ui.refrence.setText("")
        self.ui.index.setText("")
        self.ui.coledge.setText("")
        self.ui.nationality.setText("")
        self.ui.validity.setText("")
        self.ui.program.setText("")
        self.ui.year.setText("")
        self.ui.last_in.setText("")
        self.ui.last_out.setText("")
        self.ui.image.setPixmap("")
    
    def last_seen(self,reference:str):
        list_months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July',
                     'August', 'September', 'October', 'November', 'December']
        cursor=my_cursor.execute("SELECT date_stamp,time_out,duration FROM tb_attendance WHERE st_reference = "+(reference)+" ORDER BY date_stamp DESC LIMIT 2")
        cursor= my_cursor.fetchall()
        last_seen_info = []
        if cursor:
            for data in cursor:
                last_seen_info.append(data)
            db.commit()
        if last_seen_info:
            details=str(last_seen_info[1][0]).split('-')
            year = details[0]
            month = details[1]
            day = details[2]
            time = last_seen_info[0][1]
            duration = last_seen_info[0][2]
            construct_last_seen = str(list_months[int(month)]+' '+day+' '+year+' @ '+time)
            self.ui.last_out.setText(construct_last_seen)
            self.ui.last_in.setText(duration)           
        else:
            self.ui.last_out.setText("Oops! first timer")
            self.ui.last_in.setText("00:00:00") 

    def retreive_student_details(self,data):
        if isinstance(data, str):
                self.last_seen(data)
                db_data=self.fetch_data_from_db(data)
                if len(db_data) > 0:
                    list_months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July',
                     'August', 'September', 'October', 'November', 'December']
                    start_date = (str(db_data[8])).split('-')
                    end_date=str(db_data[9]).split('-')
                    student_year=(int(dt.now().date().strftime('%Y'))-int(start_date[0]))
                      
                    if student_year <= 1:
                        level = "1st year"
                    elif student_year > 1 and student_year <= 2:
                        level = "2nd year"
                    elif student_year > 2 and student_year <= 3:
                        level = "3rd year"
                    elif student_year > 3 and student_year <= 4:
                        level = "4th year"

                    helper = str(db_data[3]).split(" ")
                    self.ui.firstname.setText(helper[0])
                    self.ui.middlename.setText(helper[1])
                    self.ui.lastname.setText(db_data[4])
                    self.ui.refrence.setText(str(db_data[1]))
                    self.ui.index.setText(str(db_data[2]))
                    self.ui.coledge.setText(db_data[5])
                    self.ui.nationality.setText(db_data[7])
                    self.ui.validity.setText(list_months[int(start_date[1])-1]+","+start_date[0]+
                    " - "+list_months[int(end_date[1])-1]+","+end_date[0])
                    self.ui.year.setText(level)
                    self.ui.program.setText(db_data[6])
                    self.load_image_from_db(data,self.ui.image)
                    self.show_info("Student details found!")
                else:
                    self.show_info("Student not found. Please register!")
                    self.loadUi_file()                

    def mark_attendance_db(self):
        attendance = Attendance(
            self.ui.refrence.text(),
            self.ui.program.text(),
            str(dt.now().date().strftime("%Y-%m-%d")),
            str(dt.now().time().strftime("%H:%M:%S")),
            str(dt.now().time().strftime("%H:%M:%S")),
            "00:00:00"
        )
        if self.ui.refrence.text() != "Reference":
            data=my_cursor.execute("SELECT st_reference,date_stamp FROM tb_attendance WHERE st_reference=%s and date_stamp=%s ",
            (self.ui.refrence.text(),dt.now().date().strftime("%Y-%m-%d")))
            data=my_cursor.fetchone()
            details = []
            if data:
                for detail in data:
                    details.append(detail)
                db.commit()
            
            if not details:
                self.show_info("")
                my_cursor.execute("INSERT INTO tb_attendance(st_reference,program,date_stamp,time_in,time_out,duration) VALUES(%s,%s,%s,%s,%s,%s)",
                (attendance.st_reference,attendance.program,attendance.date,
                attendance.time_in,attendance.time_out,attendance.duration))
                db.commit()
                self.show_info("Student details captured!")
            else:
                self.show_info("Student details already in captured!")

        
    def start_webcam(self):
        ip_address = self.ui.camera_ip.text()
        system_attached_camera = self.ui.comboBox.currentText()
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
                self.show_info("Hey! wait a second while system\ninitializes camera")
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:       
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.show_info("Hey! wait a second while system\ninitializes camera")
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

    def update_frame(self):

        thickness = 2
        rect_thickness = 1
        color = (255,255,0)

        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)

        self.beta = int(self.ui.hsv_value.text())
        self.apha = int(self.ui.bb_blur_value.text())*0.01
        self.kernel = (int(self.ui.gb_blur_value.text())*0.01)
       
        self.frame = cv2.filter2D(self.frame,-1, self.kernel)
        self.result = cv2.addWeighted(self.frame,self.apha, np.ones(self.frame.shape, self.frame.dtype), 0, self.beta)

        self.text = str(time.strftime("%H:%M %p"))
        ps.putBText(self.result,self.text,text_offset_x=self.result.shape[1]-90,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(228,20,222),text_RGB=(255,255,255))
        self.now = dt.now()
        self.now = self.now.strftime("%a, %b %d, %Y")
        ps.putBText(self.result,self.now,text_offset_x=10,text_offset_y=10,vspace=5,hspace=5, font_scale=0.5,
            background_RGB=(10,20,222),text_RGB=(255,255,255))
        cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(self.result, cv2.COLOR_BGR2GRAY)

        if self.ui.face_auth.isChecked():
            curent_frame_face = face_recognition.face_locations(gray)
            curent_frame_encode = face_recognition.face_encodings(self.result, curent_frame_face)   
            for encode_face, face_location in zip(curent_frame_encode, curent_frame_face):
                (left,bottom,right,top) = face_location
                cv2.rectangle(self.result, (top,left), (bottom,right), (255,255,0), rect_thickness)
                cv2.line(self.result,(top,left),(top+15,left),color,thickness)
                cv2.line(self.result,(top,left),(top,left+15),color,thickness)
                cv2.line(self.result,(bottom,left),(bottom-15,left),color,thickness)
                cv2.line(self.result,(bottom,left),(bottom,left+15),color,thickness)
                cv2.line(self.result,(top,right),(top+15,right),color,thickness)
                cv2.line(self.result,(top,right),(top,right-15),color,thickness)
                cv2.line(self.result,(bottom,right),(bottom-15,right),color,thickness)
                cv2.line(self.result,(bottom,right),(bottom,right-15),color,thickness)     
                matches = face_recognition.compare_faces(encode_list, encode_face)
                face_distance = face_recognition.face_distance(encode_list, encode_face)
                match_index = np.argmin(face_distance)
                if matches[match_index]:
                    get_name = name_list[match_index].upper()
                    mark_attendance(get_name)
                    (left,bottom,right,top) = face_location
                    cv2.rectangle(self.result, (top,left), (bottom,right), (255,255,0), rect_thickness)
                    print (get_name)
                elif not  matches[match_index]:
                    print("No matches found") 
            self.display_feed(self.frame,1)    

        elif self.ui.qr_code_auth.isChecked():
            for qr_code in decode(self.result):
                qr_code_data  = qr_code.data.decode('utf-8')
                pts = np.array([qr_code.polygon], np.int)
                rect = np.array([qr_code.rect], np.int)
                pts = pts.reshape((-1, 1, 2))   
                # cv2.polylines(frame, [pts], True,(255,255,0),1)
                for x,y,w,h in rect:
                    w , h =x+w, y+h
                    cv2.rectangle(self.result, (x,y), (w,h), (255,255,0), rect_thickness)

                    cv2.line(self.result,(x,y),(x+15,y),(255,255,0),thickness)
                    cv2.line(self.result,(x,y),(x,y+15),(255,255,0),thickness)

                    cv2.line(self.result,(w,y),(w-15,y),(255,255,0),thickness)
                    cv2.line(self.result,(w,y),(w,y+15),(255,255,0),thickness)

                    cv2.line(self.result,(x,h),(x+15,h),(255,255,0),thickness)
                    cv2.line(self.result,(x,h),(x,h-15),(255,255,0),thickness)

                    cv2.line(self.result,(w,h),(w-15,h),(255,255,0),thickness)
                    cv2.line(self.result,(w,h),(w,h-15),(255,255,0),thickness)
                self.retreive_student_details(qr_code_data)
                time.sleep(0.1)  
                self.mark_attendance_db()
                winsound.Beep(1000,100)    
            self.display_feed(self.result,1)         

        elif self.ui.biometric_auth.isChecked():
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
            self.ui.camera_view.setPixmap(QPixmap.fromImage(procesedImage))
            self.ui.camera_view.setScaledContents(True)
        
    def stop_webcam(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_view.setPixmap(QPixmap())
        self.ui.camera_view.setAlignment(Qt.AlignCenter)
        self.timer.stop()

    def show_info(self, content:str):
        self.ui.label_notification.setText(content)       

    def update_guasian_blur(self, value):
        self.ui.dilation_value.setText(str(value))
    
    def update_median_blur(self, value):
        self.ui.erosion_value.setText(str(value))

    def update_threshold(self, value):
        self.ui.thresh_value.setText(str(value))

    def update_brigthness(self, value):
        self.ui.hsv_value.setText(str(value))
        return value 

    def update_average_blurring(self, value):
        self.ui.avg_blur_value.setText(str(value))

    def update_sharpness(self, value):
        self.ui.gb_blur_value.setText(str(value))
        return value

    def update_contrast(self, value):
        self.ui.bb_blur_value.setText(str(value))
        return value

    def update_kernel(self, value):
        self.ui.kernel_value.setText(str(value))      


    def start_webcam_cam_one(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_one_id_ip.text()
        system_attached_camera = self.ui.camera_one_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_cam_one
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_cam_one
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_cam_one
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_cam_one)
        self.timer.start(3)

    def update_frame_cam_one(self): 
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.display_feed_cam_one(self.frame,1)
        
    def display_feed_cam_one(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 1:
            self.ui.camera_1.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_1.setScaledContents(True)
    
    def stop_webcam_cam_one(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_1.setPixmap(QPixmap())
        self.ui.camera_1.setAlignment(Qt.AlignCenter)
        self.timer.stop() 
   
    
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        # IF NOT MAXIMIZED
        if status == 0:
            self.showMaximized()
            # SET GLOBAL TO 1
            GLOBAL_STATE = 1
            # IF MAXIMIZED REMOVE MARGINS AND BORDER RADIUS
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.drop_shadow_layout.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Restore")
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            #self.resize(self.width()+1, self.height()+1)
            self.ui.drop_shadow_layout.setContentsMargins(0, 0, 0, 0)
            #self.ui.drop_shadow_layout.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.521368 rgba(28, 29, 73, 255)); border-radius: 0px;")
            self.ui.btn_maximize.setToolTip("Maximize")

    def mousePressEvent(self, event):
        self.oldPosition = event.globalPos()

    def mouseMoveEvent(self,event):
        delta = QPoint(event.globalPos() - self.oldPosition)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPosition = event.globalPos()    
 
    def applyStyle(self):
        for w in self.ui.frame.findChildren(QPushButton):
            if w.objectName()!= self.sender().objectName():
                defaultStyle = w.styleSheet().replace("border-left:3px solid rgb(35, 35, 35) ;","")
                w.setStyleSheet(defaultStyle)
        newStytle = self.sender().styleSheet()+("border-left:3px solid rgb(255, 255, 255);")
        self.sender().setStyleSheet(newStytle)
        return


    def start_webcam_cam_two(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_two_id_ip.text()
        system_attached_camera = self.ui.camera_two_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_cam_two
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_cam_two
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_cam_two
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_cam_two)
        self.timer.start(3)

    def update_frame_cam_two(self): 
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.display_feed_cam_two(self.frame,2)
        
    def display_feed_cam_two(self, image, window=2):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 2:
            self.ui.camera_2.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_2.setScaledContents(True)
    
    def stop_webcam_cam_two(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_2.setPixmap(QPixmap())
        self.ui.camera_2.setAlignment(Qt.AlignCenter)
        self.timer.stop() 


    def start_webcam_cam_three(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_three_id_ip.text()
        system_attached_camera = self.ui.camera_three_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_cam_three
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_cam_three
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_cam_three
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_cam_three)
        self.timer.start(3) 
    
    def update_frame_cam_three(self):  
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.display_feed_cam_three(self.frame,window=1)
        
    def display_feed_cam_three(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 1:
            self.ui.camera_3.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_3.setScaledContents(True)
    
    def stop_webcam_cam_three(self):    
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_3.setPixmap(QPixmap())
        self.ui.camera_3.setAlignment(Qt.AlignCenter)
        self.timer.stop() 


    def start_webcam_cam_four(self):
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\ninitializes camera")  
        self.show_alert.show()
        ip_address = self.ui.camera_four_id_ip.text()
        system_attached_camera = self.ui.camera_four_comboBox.currentText()
        camera_id = int(system_attached_camera)
        self.system_capture = VideoCapture(camera_id)
        self.network_capture = VideoCapture(ip_address)
        if ip_address:
            if self.network_capture is None or not self.network_capture.isOpened():    
                self.stop_webcam_cam_four
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera ip address connetion\nor is already in use.") 
                self.show_alert.show()
            else:
                self.capture = VideoCapture(ip_address)
                
        elif system_attached_camera:
            if self.system_capture is None or not self.system_capture.isOpened():    
                self.stop_webcam_cam_four
                self.show_alert = AlertDialog()
                self.show_alert.content("Oops! check the camera for connetion\nor is already in use.")  
                self.show_alert.show()
            else:
                self.capture = VideoCapture(camera_id) 
                        
        elif self.system_capture.isOpened() and self.network_capture.isOpened():
                self.stop_webcam_cam_four
                self.show_alert = AlertDialog()
                self.show_alert.content() 
                self.show_alert.show()

        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,300)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame_cam_four)
        self.timer.start(3) 
    
    def update_frame_cam_four(self):  
        ret,self.frame = self.capture.read()
        self.frame = cv2.flip(self.frame,1)
        self.display_feed_cam_four(self.frame,window=1)
        
    def display_feed_cam_four(self, image, window=1):
        qformate = QImage.Format_Indexed8
        if len(image.shape) == 3:
            if image.shape[2] == 4:
                qformate = QImage.Format_RGBA8888
            else:
                qformate = QImage.Format_RGB888
        self.procesedImage = QImage(image,image.shape[1],image.shape[0],image.strides[0],qformate)
        self.procesedImage = self.procesedImage.rgbSwapped()
        if window == 1:
            self.ui.camera_4.setPixmap(QPixmap.fromImage(self.procesedImage))
            self.ui.camera_4.setScaledContents(True)
    
    def stop_webcam_cam_four(self):    
        self.show_alert = AlertDialog()
        self.show_alert.content("Hey! wait a second while system\release camera")  
        self.show_alert.show()
        self.ui.camera_4.setPixmap(QPixmap())
        self.ui.camera_4.setAlignment(Qt.AlignCenter)
        self.timer.stop()    


class Splash_screen(QMainWindow):
    def __init__(self, **kwargs):
        QMainWindow.__init__(self, **kwargs)
        self.ui_splash = Ui_MainWindow()
        self.ui_splash.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 70))
        self.ui_splash.main.setGraphicsEffect(self.shadow)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.progress)
        self.timer.start(40)
        self.show()

    def progress(self):
        global counter
        self.ui_splash.progressBar.setValue(counter)
        if counter > 100:
            self.timer.stop()
            self.main = MainWindow()
            self.main.show()
            self.close()
        counter +=1

if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = Splash_screen()  
    sys.exit(application.exec_()) 